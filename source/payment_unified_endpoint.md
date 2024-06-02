# Payment Integration Order API

### Overview

The Unified Payment Gateway Architecture is designed to streamline the integration of various payment gateways into a single, cohesive system. This architecture allows developers to easily add and manage different payment gateways such as Stripe, PayPal, 2Checkout, Razorpay, Authorize.net, Squareup, and thousands of other payment gateways by following a standardized plugin approach.

> The architecture is simple: Single API for all payment gateways.

### Guest User Endpoint

`API: POST /order/storefront/api/guest-user-order-create/`

### Returning User Endpoint

`API: POST /order/storefront/api/user-order-create/`

Use this API if you allow only authenticated users to place orders. The payload and URL arguments are the same as those for the guest order API.

### Payment

`API: POST /payment/storefront/api/start-payment/{payment_plugin_id}/`

When you send a request to this URL, you will receive a URL from the payment gateway to complete the payment.

### Webhook & IPN

`API: POST /payment/storefront/api/webhook-view/{payment_plugin_id}/`

Once you have integrated the API and are accepting payments, the webhook listener helps your store backend identify which user paid for what. This single webhook listener works for all APIs.

### Definition

`payment_plugin_id` is a URL argument representing the name of the payment plugin you installed. For example, if you have installed or built a payment plugin for Stripe, it will be located at `nxtbn.payment.plugins.stripe`. Here, `stripe` is your `payment_plugin_id`. Similarly, for PayPal or Authorize.Net, the plugins will be located at `nxtbn.payment.plugins.paypal` and `nxtbn.payment.plugins.authorize_net`, respectively, making `'paypal'` or `'authorize_net'` your `payment_plugin_id`. The same applies to other payment gateways as well.
