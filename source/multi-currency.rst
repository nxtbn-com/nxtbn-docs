Multicurrency Support
=====================

nxtbn offers robust support for multiple currencies, enabling your e-commerce platforms to seamlessly handle international transactions. This feature is designed to provide flexibility in how currency conversion is implemented, tailored to different use cases and preferences.

Implementing Multicurrency
--------------------------

There are two main methods for implementing multicurrency in nxtbn:

1. **Client-side Currency Conversion** (Not Recommended):
   This approach converts currencies directly in the client's browser. It is generally less secure and can lead to discrepancies due to fluctuating exchange rates not being updated in real-time.

2. **Backend Currency Conversion with Plugins** (Recommended):
   This method uses server-side logic to convert currencies, ensuring consistency and reliability. nxtbn supports this through a variety of plugins, making it easy to adapt to different APIs and exchange rate providers.

Using Backend Currency Conversion with Plugins
----------------------------------------------

To facilitate effective multicurrency support, nxtbn offers plugins such as the `Free Currency API plugin <https://github.com/nxtbn-com/freecurrencyapi>`_. This plugin is a good starting point, but you are encouraged to integrate any other currency API that meets your specific needs.

**Pre-requisites**

Before you begin, ensure that multicurrency support is activated within your nxtbn environment.

**Configuring Currency Conversion**

Currency conversion is primarily managed through the ``Accept-Currency`` header in API requests. This approach allows the middleware to process the desired currency seamlessly.

- **Setting the Header**: Include the ``Accept-Currency`` header with the desired currency code when making API requests. This can be done using any standard HTTP client like axios or fetch.

- **Alternative Methods**: While the header is recommended, currency can also be specified through query parameters or directly in the payload.

**Accessing Currency Information in the Backend**

Currency information can be accessed in backend processes as follows:

- **In Views**: Use ``self.request.currency`` to retrieve the currency code directly from the request object.
- **In Serializers**: Access it through ``self.context['request'].currency`` in Django serializers.

Example Serializer for Currency Conversion
------------------------------------------

Here's how you can implement a serializer that handles currency conversion:

.. code-block:: python

    from nxtbn.core.currency.backend import CurrencyBackend
    from rest_framework import serializers
    from nxtbn.product.models import Product, ProductVariant

    class ImageSerializer(serializers.ModelSerializer):
        # Assume an existing ImageSerializer implementation

    class ProductVariantSerializer(serializers.ModelSerializer):
        variant_image = ImageSerializer(many=True, read_only=True)
        price_in_target_currency = serializers.SerializerMethodField()

        class Meta:
            model = ProductVariant
            fields = '__all__'

        def get_price_in_target_currency(self, obj):
            if not settings.IS_MULTI_CURRENCY:
                return obj.price
            else:
                currency_code = self.context.get('request').currency
                converted_price = CurrencyBackend().to_target_currency(currency_code, obj.price)
                return converted_price

This example demonstrates fetching the currency from the API request and using it to convert the price of a product variant.

Handling Currency Precision
----------------------------

nxtbn handles various global currencies by standardizing to three decimal points. This level of precision addresses the needs of currencies with different decimal requirements:

- JPY (0 decimal points)
- KWD (3 decimal points)
- USD (2 decimal points)
- BHD (1 decimal point)

Currency Storage Considerations
-------------------------------

nxtbn can store currency values in different formats (main units or subunits) to minimize rounding errors. This strategy is defined in the ``money_validator_map`` within our models, ensuring accuracy and precision across financial transactions.

This enhanced documentation provides comprehensive information and guidance on setting up and managing multicurrency support in nxtbn, making it easier for developers to implement and customize according to their needs.
