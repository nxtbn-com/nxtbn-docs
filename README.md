🚧 **The project is under development, please check back after one month for a stable version.** ⏳

# Next Billion Native Commerce - nxtbn documentation

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
```sh
sphinx-autobuild source build/html
