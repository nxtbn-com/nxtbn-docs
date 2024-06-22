Plugin Installation
====================

In nxtbn Commerce, you can install plugins in three ways:

1. Via nxtbn Commerce Dashboard
::::::::::::::::::

Login to your dashboard and follow these steps:

1. Navigate to **Plugins**.
2. Search for your desired plugin and install it.
3. If you have a plugin file, click on **Add Plugin** and upload the plugin file.
4. Once uploaded/installed, the plugin will be automatically registered.

**Note:** After installation, the plugin will be registered but not activated. To activate it:

- Go to **Plugins > Installed Plugins > Inactive Plugins** and activate the plugin.

2. Via CLI
::::::::::::::::::

If you are a developer, you can install a plugin via the CLI using the following command:

.. code-block:: bash

   python3 manage.py install_plugin_via_zip_url <plugin_zip_url>

Example:

.. code-block:: bash

   python manage.py install_plugin_via_zip_url www.example.com/someplugin.zip

To activate the plugin, run:

.. code-block:: bash

   python manage.py toggle_plugin_status activate <YOUR_PLUGIN_NAME>

To deactivate, use the deactivate flag:

.. code-block:: bash

   python manage.py toggle_plugin_status deactivate <YOUR_PLUGIN_NAME>

3. Manual Installation
::::::::::::::::::

If you have a plugin file, manually move your plugin to ``nxtbn/plugins/source/``.

**Note:** The plugin will not be registered automatically if you do it manually. To register it, run:

.. code-block:: bash

   python manage.py register_plugin <YOUR_PLUGIN_NAME>

Alternatively, you can register the plugin via the Django admin panel or the nxtbn dashboard.
