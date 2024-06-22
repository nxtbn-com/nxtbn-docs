Plugin Basics
==============

Getting Started
----------------

A nxtbn plugin is essentially a Python file with plugin metadata in its header. It's recommended to organize your plugin's files within a directory for better organization.

Creating a New Plugin
~~~~~~~~~~~~~~~~~~~~~~

To create a new plugin, follow these steps:

1. Navigate to the ``nxtbn/plugins/sources/`` directory in your nxtbn installation.
2. Create a new directory named after your plugin (e.g., ``plugin-name``).
3. Open the newly created plugin directory.
4. Inside the directory, create two Python files: ``__init__.py`` and ``your_plugin_name.py``.

Example (Unix Command Line)
::::::::::::::::::


.. code-block:: bash

   cd nxtbn/plugins/sources
   mkdir xpay
   touch xpay/__init__.py
   touch xpay/somename_xpay.py

Initialization (Example ``__init__.py``)
::::::::::::::::::


.. code-block:: python

   metadata = {
       "plugin_name": "xpay",  # Must be unique to your plugin
       "plugin_type": "PAYMENT_PROCESSOR",  # Plugin type
       "plugin_uri": "https://example.com",
       "version": "1.0.0",
       "author": "John Doe",
       "author_uri": "http://example.com",
       "description": "Plugin to handle payments via xpay.",
       "license": "MIT",
       "nxtbn_version_compatibility": ">=1.0.0"
   }

   from .somename_xpay import SomePaymentGateway

   plugin = SomePaymentGateway

   __all__ = ['plugin']
