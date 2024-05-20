# Unified Payment Gateway Architecture

## Overview

The Unified Payment Gateway Architecture is designed to simplify the integration of various payment gateways into a single, cohesive system. This architecture allows developers to easily add and manage different payment gateways such as Stripe, PayPal, 2Checkout, Razorpay, Authorize.net, Squareup, thousand + other payment gateway by following a standardized plugin approach. 

>The architecture is simple: Single API for all payment gateways

## Key Components

### Abstract Base Class for Payment Gateways
```{admonition} file
:class: note

nxtbn/nxtbn/payment/base_payment_gateway.py
```

All payment gateways should inherit from the `BasePaymentGateway` abstract base class. This class defines the interface that each payment gateway must implement.



```python
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Optional, Any, Dict
from dataclasses import dataclass
from rest_framework import serializers
from nxtbn.core.models import SiteSettings
from nxtbn.payment.models import Payment

@dataclass
class PaymentResponse:
    success: bool
    transaction_id: Optional[str] = None
    message: Optional[str] = None
    raw_data: Optional[Any] = None
    meta_data: Optional[Any] = None

class BasePaymentGateway(ABC):
    def __init__(self, context: dict = None):
        self.context = context or {}

    @abstractmethod
    def authorize(self, amount: Decimal, order_id: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def capture(self, amount: Decimal, order_id: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def cancel(self, order_id: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def refund(self, amount: Decimal, order_id: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def normalize_response(self, raw_response: Any) -> PaymentResponse:
        raise NotImplementedError

    @abstractmethod
    def special_serializer(self):
        raise NotImplementedError

    @abstractmethod
    def public_keys(self):
        raise NotImplementedError

    def payment_url_with_meta(self, order_alias: str, **kwargs) -> Dict[str, Any]:
        raise NotImplementedError

    def handle_webhook_event(self, request_data: Dict[str, Any]) -> PaymentResponse:
        raise NotImplementedError

    def create_payment_instance(self, payment_payload: Dict[str, Any], **kwargs):
        serializer = BasePaymentSerializer(data=payment_payload)
        if serializer.is_valid():
            serializer.save()
        return serializer.data

    def get_currency_code(self, **kwargs) -> str:
        return SiteSettings.objects.all().first().base_currency

    def total_unit_amount(self, **kwargs) -> int:
        return self.get_unit_amount(self.context['request'].data.get('total_price'))

    def get_unit_amount(self, amount, **kwargs) -> int:
        return int(float(amount) * 100)

    def normalize_amount(self, amount, **kwargs) -> Decimal:
        return int(amount) / 100
```

## Payment Manager
```{admonition} file
:class: note
nxtbn/nxtbn/payment/payment_manager.py
```

The PaymentManager class is responsible for managing the different payment gateways. It dynamically loads the appropriate gateway based on the payment_plugin_id.

```
import os
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ValidationError
from importlib import import_module
import logging
from nxtbn.payment.utils import check_plugin_directory, get_plugin_path, security_validation

logger = logging.getLogger(__name__)

class PaymentManager:
    def __init__(self, payment_plugin_id: str, context: dict = {}):
        self.payment_plugin_id = payment_plugin_id
        self.context = context
        self.gateway = self.select_gateway(payment_plugin_id)

    def select_gateway(self, payment_plugin_id: str):
        security_validation(payment_plugin_id)
        
        if not check_plugin_directory(payment_plugin_id):
            raise ValidationError("No gateway class found")
        
        gateway_path = get_plugin_path(payment_plugin_id)
        module_name, class_name = gateway_path.rsplit(".", 1)
        module = import_module(module_name)
        gateway_class = getattr(module, class_name)

        return gateway_class(context=self.context)

    def authorize_payment(self, amount: Decimal, order_id: str, **kwargs):
        return self.gateway.authorize(amount, order_id, **kwargs)

    def capture_payment(self, amount: Decimal, order_id: str, **kwargs):
        return self.gateway.capture(amount, order_id, **kwargs)

    def cancel_payment(self, order_id: str, **kwargs):
        return self.gateway.cancel(order_id, **kwargs)

    def refund_payment(self, payment_id: str, amount: str, **kwargs):
        return self.gateway.refund(payment_id, amount, **kwargs)

    def special_serializer(self):
        return self.gateway.special_serializer()

    def public_keys(self):
        return self.gateway.public_keys()

    def payment_url_with_meta(self, order_alias, **kwargs):
        return self.gateway.payment_url_with_meta(order_alias, **kwargs)

    def handle_webhook_event(self, request_data, **kwargs):
        return self.gateway.handle_webhook_event(request_data, self.payment_plugin_id, **kwargs)

    def create_payment_instance(self, payload, **kwargs):
        return self.gateway.create_payment_instance(payload, **kwargs)

    def currency_code(self, context, **kwargs) -> str:
        return self.gateway.get_currency_code()

    def total_unit_amount(self, context, **kwargs) -> int:
        return self.gateway.total_unit_amount()

```

## Example Integration: Stripe

```{admonition} file
:class: note
nxtbn/nxtbn/payment/plugins/{YOUR-PAYMENT-PLUGIN-DIRECTORY}/your_file_name.py
```
Here is an example implementation of the `StripePaymentGateway`.

```
import stripe
from decimal import Decimal
from django.conf import settings
from nxtbn.payment.base_payment_gateway import BasePaymentGateway, PaymentResponse
from rest_framework import serializers
from nxtbn.settings import get_env_var

stripe.api_key = get_env_var('STRIPE_SECRET_KEY', '')

class StripePayloadSerializer(serializers.Serializer):
    stripe_payment_method_id = serializers.CharField(max_length=500, required=True)

class StripePaymentGateway(BasePaymentGateway):
    gateway_name = 'stripe'

    def authorize(self, amount: Decimal, order_id: str, **kwargs):
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),
                currency='usd',
                payment_method=kwargs.get("payment_method_id"),
                confirmation_method='manual',
                confirm=True,
                metadata={'order_id': order_id},
            )
            return self.normalize_response(intent)
        except stripe.error.StripeError as e:
            return PaymentResponse(success=False, message=str(e))

    def capture(self, amount: Decimal, order_id: str, **kwargs):
        payment_intent_id = kwargs.get("payment_intent_id")
        try:
            intent = stripe.PaymentIntent.capture(payment_intent_id)
            return self.normalize_response(intent)
        except stripe.error.StripeError as e:
            return PaymentResponse(success=False, message=str(e))

    def cancel(self, order_id: str, **kwargs):
        payment_intent_id = kwargs.get("payment_intent_id")
        try:
            intent = stripe.PaymentIntent.cancel(payment_intent_id)
            return self.normalize_response(intent)
        except stripe.error.StripeError as e:
            return PaymentResponse(success=False, message=str(e))

    def refund(self, amount: Decimal, order_id: str, **kwargs):
        charge_id = kwargs.get("charge_id")
        try:
            refund = stripe.Refund.create(
                charge=charge_id,
                amount=int(amount * 100),
            )
            return self.normalize_response(refund)
        except stripe.error.StripeError as e:
            return PaymentResponse(success=False, message=str(e))

    def normalize_response(self, raw_response):
        return PaymentResponse(
            success=raw_response.get("status") in ["succeeded", "canceled", "refunded"],
            transaction_id=raw_response.get("id"),
            message=raw_response.get("status"),
            raw_data=raw_response,
        )

    def special_serializer(self):
        return StripePayloadSerializer()

    def public_keys(self):
        keys = {
            'STRIPE_PUBLIC_KEY': get_env_var('STRIPE_PUBLIC_KEY', '')
        }
        return keys

```

> important
The plugin you add/build, you must put the class in `gateway` variable here in `__init__.py` of your root plugin root file.


```{admonition} file
:class: note
nxtbn/nxtbn/payment/plugins/{YOUR-PAYMENT-PLUGIN-DIRECTORY}/__init__.py
```

```
from . stripe_gateway import StripePaymentGateway

gateway = StripePaymentGateway

__all__ = ['gateway']

```

## API Endpoints (built-in)
```{admonition} file
:class: note
nxtbn/nxtbn/order/api/storefront/views.py
```


Two API endpoints are provided for creating orders: one for guest users and one for authenticated users. The serializer used for order creation is dynamically determined based on the payment gateway ID provided in the URL.

```{admonition} Attention
:class: attention
We recommend not updating the API endpoint as we have tested with over 40 payment gateways worldwide. The same API works for every payment gateway that loads automatically based on the `payment_plugin_id`. 

You can customize the API endpoint directly from your plugin class. No API endpoint update is required. Modifying the API endpoint may disrupt the system.
```

```
class GuestUserOrderCreateAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = GuestOrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        payment_plugin_id = self.kwargs.get('payment_plugin_id')
        if payment_plugin_id:
            context['payment_plugin_id'] = payment_plugin_id
        return context

    def dispatch(self, request, *args, **kwargs):
        payment_plugin_id = self.kwargs.get('payment_plugin_id')
        if payment_plugin_id:
            if not check_plugin_directory(payment_plugin_id):
                raise Http404(f"Payment gateway '{payment_plugin_id}' is not installed plugin.")
        return super().dispatch(request, *args, **kwargs)

class OrderCreateAPIView(generics.CreateAPIView):
    serializer_class = AuthenticatedUserOrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        payment_plugin_id = self.kwargs.get('payment_plugin_id')
        if payment_plugin_id:
            context['payment_plugin_id'] = payment_plugin_id
        return context

    def dispatch(self, request, *args, **kwargs):
        payment_plugin_id = self.kwargs.get('payment_plugin_id')
        if payment_plugin_id:
            if payment_plugin_id.lower() not in getattr(settings, 'PAYMENT_GATEWAYS'):
                raise Http404(f"Payment gateway '{payment_plugin_id}' is not implemented.")
        return super().dispatch(request, *args, **kwargs)

```

```{admonition} file
:class: note
nxtbn/nxtbn/order/api/storefront/urls.py
```

```
from django.urls import path
from nxtbn.order.api.storefront import views as order_views

urlpatterns = [
    ....
    path('guest-user-order-create/<str:payment_plugin_id>/', order_views.GuestUserOrderCreateAPIView.as_view(), name='guest-user-order-create'),
    path('user-order-create/<str:payment_plugin_id>/', order_views.OrderCreateAPIView.as_view(), name='user-order-create'),
    .....
]
```

## API endpoint for webhook & IPN
```{admonition} file
:class: note
nxtbn/nxtbn/payment/api/storefront/views.py
```

The `WebhookAPIView` class listens for webhooks and IPNs (Instant Payment Notifications) from various payment gateways. It uses the `PaymentManager` to handle the events.

```
from django.http import Http404
from rest_framework import generics, status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from rest_framework.permissions  import AllowAny
from rest_framework.exceptions import APIException
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from nxtbn.payment.payment_manager import PaymentManager
from nxtbn.payment.utils import check_plugin_directory


class WebhookAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, payment_plugin_id):
        return self.dispatch_hook(request, payment_plugin_id)

    @method_decorator(csrf_exempt)
    def post(self, request, payment_plugin_id):
        return self.dispatch_hook(request, payment_plugin_id)

    def dispatch_hook(self, request, payment_plugin_id):
        return PaymentManager(payment_plugin_id).handle_webhook_event(request)
```

```{admonition} file
:class: note
nxtbn/nxtbn/payment/api/storefront/urls.py
```

```
from django.urls import path
from nxtbn.payment.api.storefront import views as payment_views

urlpatterns = [
    ....
    path('webhook-view/<str:payment_plugin_id>/', payment_views.WebhookAPIView.as_view(), name='webhook_view'),
]
```

```{admonition} Note Again
:class: Caution
We recommend not updating the API endpoint as we have tested with over 40 payment gateways worldwide. The same API works for every payment gateway that loads automatically based on the `payment_plugin_id`. 

You can customize the API endpoint directly from your plugin class. No API endpoint update is required. Modifying the API endpoint may disrupt the system.
```

## Adding a New Payment Gateway

To add a new payment gateway:

1. Create a new file in nxtbn.payment.plugin/ for the new gateway.
2. Implement the gateway by inheriting from BasePaymentGateway.
3. Ensure the gateway class follows the structure and implements all the abstract methods.

For example, to add PayPal:

Create `paypal_gateway.py` in `nxtbn.payment.plugin/paypal`.
Implement the class `PayPalPaymentGateway` inheriting from `BasePaymentGateway`.