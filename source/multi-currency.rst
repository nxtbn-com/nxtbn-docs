nxtbn Multicurrency Support
===========================

nxtbn supports robust multicurrency functionalities, enabling global e-commerce transactions through secure backend currency conversion.

Implementing Multicurrency
--------------------------

**Backend Currency Conversion with Plugins**:
   Utilize backend currency conversion for accuracy and consistency. nxtbn supports various currency conversion plugins, including the recommended `Free Currency API plugin <https://github.com/nxtbn-com/freecurrencyapi>`_. You may integrate any other suitable currency API as needed.

Setup and Configuration
-----------------------

**Activating Multicurrency**:
   Ensure multicurrency is enabled in your nxtbn settings.

**Currency Conversion Handling**:
   Manage currency conversions using the ``Accept-Currency`` HTTP header in API requests. This approach allows middleware to seamlessly process the desired currency.

**Backend Currency Access**:
   Access the currency specified in requests within your backend logic:
   - **In Views**: Use ``self.request.currency``
   - **In Serializers**: Use ``self.context['request'].currency``

   The default currency is the ``BASE_CURRENCY`` specified in settings if no currency is specified in the request.

Example: Currency Conversion in Serializers
------------------------------------------

Here is how to implement a serializer for currency conversion:

.. code-block:: python

    from nxtbn.core.currency.backend import CurrencyBackend
    from rest_framework import serializers
    from nxtbn.product.models import Product, ProductVariant

    class ProductVariantSerializer(serializers.ModelSerializer):
        price_in_target_currency = serializers.SerializerMethodField()

        class Meta:
            model = ProductVariant
            fields = '__all__'

        def get_price_in_target_currency(self, obj):
            if not settings.IS_MULTI_CURRENCY:
                return obj.price
            currency_code = self.context.get('request').currency
            return CurrencyBackend().to_target_currency(currency_code, obj.price)

This example demonstrates how to apply currency conversion to product prices based on the currency code provided in API requests.

Currency Storage Strategies
----------------------------

To prevent rounding errors, nxtbn supports storing currency values as main units or subunits. The approach is detailed in the ``money_validator_map`` within our models, ensuring accurate financial data handling.

This README provides a concise guide for developers on implementing and managing multicurrency functionalities in nxtbn.
