# Payment Integration Order API


### Overview

The Unified Payment Gateway Architecture is designed to simplify the integration of various payment gateways into a single, cohesive system. This architecture allows developers to easily add and manage different payment gateways such as Stripe, PayPal, 2Checkout, Razorpay, Authorize.net, Squareup, thousand + other payment gateway by following a standardized plugin approach. 

>The architecture is simple: Single API for all payment gateways



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