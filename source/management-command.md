# Management Commands

To smooth your development flow, please get familiar with these commands to help ensure your nxtbn development success:

1. `python manage.py nxtbn_init`
   - This command initializes the nxtbn environment by generating some predefined categories and collections. It internally calls `python manage.py populate_predefined_category` and `python manage.py populate_predefined_collection`.

2. `python manage.py populate_predefined_category`
   - Generates categories that are defined in a JSON file. This helps in setting up the initial category structure for your e-commerce site.

3. `python manage.py populate_predefined_collection`
   - Generates collections that are hard-coded into the system. These collections can be used to group products in various ways for display on the site.

4. `python3 manage.py generate_nxtbn_api_docs`
   - Generates OpenAPI documentation in YAML format. This is useful for developers who need to understand and interact with the nxtbn API.

5. `python manage.py fake_populate_product`
   - Generates fake product data. This is useful for testing and development purposes when real product data is not yet available.

6. `python manage.py fake_populate_order`
   - Generates fake order data. This helps in testing order processing and management workflows without using real customer data.

7. `python manage.py populate_fake_users`
   - Generates fake user accounts. You can specify the number of fake users you want to generate by passing an argument to the command. This is useful for testing user-related features.

For other commands based on Django, please check this documentation: [Django Admin Commands](https://docs.djangoproject.com/en/5.0/ref/django-admin/). These are not related to nxtbn but are good for handling things smartly.





