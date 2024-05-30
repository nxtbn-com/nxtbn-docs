🚧 **The project is under development. Please check back in one month for a stable version.** ⏳

# Next Billion Native Commerce - nxtbn Documentation

We use Sphinx for our documentation. To build the documentation in HTML format, follow these steps:

1. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Build the HTML documentation:
    ```sh
    make html
    ```

## Live Server

To run a live server that rebuilds the documentation upon changes, use the following command:
    ```
    sphinx-autobuild source build/html
    ```

## OpenAPI Info Generation

In the nxtbn project, run the following command to generate the OpenAPI documentation:
    ```
    python3 manage.py generate_nxtbn_api_docs
    ```
This will generate two separate YAML files:
- `dashboard_openapi.yaml`
- `storefront_openapi.yaml`
