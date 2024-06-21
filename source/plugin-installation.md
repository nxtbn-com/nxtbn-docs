# Plugin Installation

In nxtbn Commerce, you can install plugins in three ways:

## 1. Via nxtbn Commerce Dashboard
1. **Login** to your dashboard.
2. Navigate to **Plugins**.
3. Search for your desired plugin and install it.
4. If you have a plugin file, click on **Add Plugin** and upload the plugin file.
5. Once uploaded/installed, the plugin will be automatically registered.

**Note:** After installation, the plugin will be registered but not activated. To activate it:
- Go to **Plugins > Installed Plugins > Inactive Plugins** and activate the plugin.

## 2. Via CLI
If you are a developer, you can install a plugin via the CLI using the following command:

```bash
python3 manage.py install_plugin_via_zip_url <plugin_zip_url>

```

Example:

```
python3 manage.py install_plugin_via_zip_url www.example.com/someplugin.zip
```

To activate the plugin, run:

```
python3 manage.py toggle_plugin_status activate <YOUR_PLUGIN_NAME>

```

To deactivate, use the deactivate flag:

```
python3 manage.py toggle_plugin_status deactivate <YOUR_PLUGIN_NAME>

```

## 3. Manual Installation

If you have a plugin file:

Move your plugin to nxtbn/plugins/source/.

***Note***: The plugin will not be registered automatically if you do manually. To register it, run:
```
python3 manage.py register_plugin <YOUR_PLUGIN_NAME>
```

Alternatively, you can register the plugin via the Django admin panel or the nxtbn dashboard.

