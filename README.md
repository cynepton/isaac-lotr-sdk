# Lord of the Rings Python SDK

SDK Implementing [the-one-api](https://the-one-api.dev/) API to serve information on LOTR.

## Getting Started

> Source code: https://github.com/cynepton/isaac-lotr-sdk

> **Requirements:**
> - [Python version 3.5 or later](https://www.python.org/downloads/)
> - A **[the-one-api.dev](https://the-one-api.dev/sign-up)** account access_token. (If you only wish to use the `/book` endpoint you would not need this to use the API, but at the moment it is required by the SDK.)

1. To use the module, first install with pip:

    ```sh
    pip install isaac-lotr-sdk
    ```

2. If you haven't already, **[create a the-one-api.dev account](https://the-one-api.dev/sign-up)** and get an access token.

3. The access token is private, so it is recommended that this is stored in the environment variables and not in version control.

    ```sh
    export THE_ONE_API_ACCESS_TOKEN=your_access_token_value
    ```
    The name `THE_ONE_API_ACCESS_TOKEN` is arbitrary and this SDK does not impose any rules on what the environment value name should be.

4. In your python script/application, import the API client and start making requests:
    ```python
    # Import the API client
    from lotr_sdk import LotrSDK
    # Import the python os module to get the environment variable
    import os

    # Get the API access token from the environment variables.
    ACCESS_TOKEN = os.getenv("THE_ONE_API_ACCESS_TOKEN")

    # Initialize the API client
    the_one_api_client = LotrSDK(access_token=ACCESS_TOKEN)

    # Start making requests
    all_movies = api_client.movie.getMovies()
    # Most endpoints allow for declaring multiple parameters and custom queries
    low_budget_movies = api_client.movie.getMovies("budgetInMillions<100", limit=2)
    ```

## SDK Documentation