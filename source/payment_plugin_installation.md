# Payment Plugin Installation

In nxtbn Commerce, you have the flexibility to install a payment gateway of your choice or even build your own. This guide will walk you through the process of installing built-in payment gateways developed by nxtbn, as well as provide you with examples of available gateways.

### Installing a Custom Payment Gateway

If you want to install a custom payment gateway or build your own, follow the detailed instructions in our documentation: `[We will add it soon] https://docs.nxtbn.com/payment-gateway`.

### Installing Built-In Payment Gateways

nxtbn Commerce offers built-in payment gateways developed by nxtbn for easy integration. You can install these gateways in two ways:

1. **Via nxtbn Dashboard**:
   - **Step 1**: Navigate to the **Dashboard**.
   - **Step 2**: Go to **Settings > Plugins**.
   - **Step 3**: Here, you have two options:
     - **Upload a Plugin**: If you have a plugin file, you can upload it here. During the upload, ensure you select the correct payment process option.
     - **Choose an Existing Built-In Gateway**: You can select from the list of available built-in gateways and install them directly.

2. **Manually**:
   - **Step 1**: Download or develop your payment gateway plugin.
   - **Step 2**: Place your plugin directory into the `nxtbn.payment.plugin` directory in your project.

### Example Payment Gateways Developed by nxtbn

Here are a few example payment gateways developed by nxtbn. Note that we are not associated with these platforms and do not endorse any. These plugins are provided to give you ideas and help you get started.

- **Stripe Payment Link**: This plugin allows you to pay via a Stripe payment link and listen for payments via webhook.
  - `GitHub Repository https://github.com/nxtbn-com/stripe-payment-link`_

- **Stripe Hosted Checkout Form**: This plugin integrates Stripe's hosted checkout form for seamless payment processing.
  - `GitHub Repository https://github.com/nxtbn-com/stripe`_

- **Cash on Delivery**: This plugin supports cash on delivery payments.
  - `GitHub Repository https://github.com/nxtbn-com/cod`_

- **Square**: This plugin integrates Square payment processing.
  - `GitHub Repository https://github.com/nxtbn-com/squareup-payment-link`_

- **PayPal**: This plugin integrates PayPal payment processing.
  - `GitHub Repository https://github.com/nxtbn-com/paypal`_

- **SSLCommerz**: This plugin integrates SSLCommerz payment processing.
  - `GitHub Repository https://github.com/nxtbn-com/sslcommerz`_

### Important Note

Please note that nxtbn is not associated with any of the payment processor platforms mentioned above, and we do not endorse any of them. These plugins are built to help you get started and provide you with examples. You are free to choose or build your own payment gateway plugins as per your requirements.

For more detailed instructions and additional information, refer to our comprehensive documentation linked above. Happy coding!
