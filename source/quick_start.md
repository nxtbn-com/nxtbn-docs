# Quick Start

Ready to start? Here's what you need to do:

- **Clone the Repository:** Get the code from our GitHub repository.
- **Install Dependencies:** Follow the installation guide to set up the necessary dependencies.
- **Run the Application:** Use our step-by-step instructions to start the nxtbn application on your local environment.
- **Explore Documentation:** Learn about the different features and customization options available.



## Install Backend for Development

1. Clone the repository:

    if you set ssh key already:
    ```
    git clone git@github.com:nxtbn-com/nxtbn.git
    ```
    if no ssh key set:
    ```
    git clone https://github.com/nxtbn-com/nxtbn.git
    ```
2. Navigate to the project directory:
    ```
    cd nxtbn
    ```
3. Copy the environment variables file:
    ```
    cp env.example .env
    ```
4. Activate the virtual environment:
    ```
    pipenv shell
    ```
5. Install dependencies:
    ```
    pipenv install
    ```
6. Apply database migrations:
    ```
    python manage.py migrate
    ```
7. Start neccessary data:
    ```
    python manage.py nxtbn_init
    ```
8. Run the development server:
    ```
    python manage.py runserver
    ```


9. API Documentation

- For the index of the docs, visit: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)

- For dashboard docs in Swagger, visit: [http://127.0.0.1:8000/docs-dashboard-swagger/](http://127.0.0.1:8000/docs-dashboard-swagger/)

- For storefront API docs in Swagger, visit: [http://127.0.0.1:8000/docs-storefront-swagger/](http://127.0.0.1:8000/docs-storefront-swagger/)

## Directory Structure

.
├── nxtbn
│   ├── cart
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── checkout
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── core
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   ├── currency
│   │   ├── management
│   │   │   └── commands
│   │   └── migrations
│   ├── discount
│   │   └── migrations
│   ├── filemanager
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── gift_card
│   │   └── migrations
│   ├── home
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── invoice
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── order
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   ├── management
│   │   │   └── commands
│   │   └── migrations
│   ├── payment
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   ├── migrations
│   │   └── plugins
│   ├── plugins
│   │   ├── migrations
│   │   └── sources
│   ├── post
│   │   └── migrations
│   ├── product
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   ├── management
│   │   │   └── commands
│   │   └── migrations
│   ├── seeder_files
│   ├── seo
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── tax
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   └── migrations
│   ├── users
│   │   ├── api
│   │   │   ├── dashboard
│   │   │   └── storefront
│   │   ├── management
│   │   │   └── commands
│   │   ├── migrations
│   │   ├── tests
│   │   └── utils
│   └── vendor
│       ├── api
│       │   ├── dashboard
│       │   └── storefront
│       └── migrations
├── proxy
├── scripts
├── static
└── templates
    ├── account
    └── admin
