# Payment Gateway API & Plugin

nxtbn offers a single API for all payment gateways. We have tested with 40+ major payment gateways worldwide with our single API endpoint, thanks to nxtbn's unified orchestrated payment gateway architecture.

### API for Payment Link, Session Link, and Webhook/IPN

Single API endpoint for all payment gateways, thanks to nxtbn's unified orchestrated architecture.

### For Guest User Endpoint

`API: POST: /order/storefront/api/guest-user-order-create/{payment_plugin_id}/`

### Returning User Endpoint

`API: POST /order/storefront/api/user-order-create/{payment_plugin_id}/`

If you allow only authenticated users to place orders, then this API is for you. The payload and URL argument are the same as the guest order API.

### Webhook & IPN

`API: POST /payment/storefront/api/webhook-view/{payment_plugin_id}/`

So, you have already integrated the API and are accepting payments, but how does your store backend know which user paid for what? That is where we come with a single webhook listener for all APIs.

### Definition

`payment_plugin_id` is a URL argument that is the name of the payment plugin you installed. Let's say you have installed/built a payment plugin for Stripe. When you install or build, the plugin will be located here: `nxtbn.payment.plugins.stripe`. So here, `stripe` is your `payment_plugin_id`. Similarly, if you install PayPal or Authorize.Net, it will be located here: `nxtbn.payment.plugins.paypal`, and here, your `payment_plugin_id` is `'paypal'`. Similar work for other payment gateways too.