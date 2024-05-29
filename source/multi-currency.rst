Multicurrency Support
===========================

nxtbn facilitates robust multicurrency functionalities, allowing for global e-commerce transactions. The platform supports multicurrency through backend conversion mechanisms that ensure accuracy and consistency.

Implementing Multicurrency
--------------------------

nxtbn provides two main methods to implement multicurrency:

1. **Client-side Currency Conversion** (Not Recommended):
   This approach handles conversion at the client level but is less secure and prone to inconsistencies due to fluctuating exchange rates.

2. **Backend Currency Conversion with Plugins** (Recommended):
   This method involves server-side currency conversion, using various plugins for flexibility and accuracy. 
   
   We added example currency plugin here, please read readme.md file of this repo: https://github.com/nxtbn-com/freecurrencyapi (We are not affiliated with this freecurrencyapi provider, it is just an example plugin to show how to integrate currency conversion plugin with nxtbn. You can use any other plugin as well.)

Setup and Configuration
-----------------------

**Activating Multicurrency**:
   Ensure that multicurrency support is enabled in your nxtbn settings.

**Currency Conversion Handling**:
   Manage currency conversions through the ``Accept-Currency`` HTTP header in API requests, which allows middleware to process the desired currency seamlessly.

**Backend Currency Access**:
   In your backend logic, access the currency specified in requests as follows:
   - **In Views**: Use ``self.request.currency``
   - **In Serializers**: Use ``self.context['request'].currency``

   If no specific currency is requested, the system defaults to the `BASE_CURRENCY` from settings.

Example: Currency Conversion in Serializers
------------------------------------------

Here’s how you can handle currency conversion within serializers:

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

This serializer demonstrates applying currency conversion based on the currency code provided in API requests.

Currency Storage Strategies
----------------------------

nxtbn employs strategic storage methods to minimize rounding errors by storing currency values as either main units or subunits. The specific approach for each currency is outlined in the ``money_validator_map`` within our models.
