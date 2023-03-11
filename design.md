# SDK Design Architecture

This SDK is python implementation for the [the-one-api.dev](https://the-one-api.dev/) API.

The SDK implements a **[single client object](lotr_sdk/__init__.py)** that can be instantiated and would provide access to the various endpoints.

```python
from lotr_sdk import LotrSDK
import os

ACCESS_TOKEN = os.getenv("ONE_API_ACCESS_TOKEN")

the_one_api_client = LotrSDK(access_token=ACCESS_TOKEN)
```
The main client object then exposes methods to cater for all other endpoints.
```python
response = the_one_api_client.movie.getMovies()
```

## Directory Structure

```
.
├── design.md
├── .gitignore
├── LICENSE
├── lotr_sdk
│   ├── __init__.py
│   ├── book.py
│   ├── chapter.py
│   ├── character.py
│   ├── movie.py
│   ├── quote.py
│   └── utils
│       ├── __init__.py
│       └── logger.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── requirements.txt
└── test.py
```

All python files are in the **[lotr_sdk](lotr_sdk)** directory and the root object can be imported with:
```python
from lotr_sdk import LotrSDK
```
The [the-one-api.dev](https://the-one-api.dev/documentation) API implements 5 major endpoint groups:

- `/book`
- `/movie`
- `/character`
- `/quote`
- `/chapter`

Each of these would have an class object with methods implementing the endpoints with their prefixes. See the [movie.py](lotr_sdk/movie.py) file as an example.

## Project Architecture

The [__init__.py](lotr_sdk/__init__.py) file in the [lotr_sdk](lotr_sdk) directory contains the main SDK client class. This class is responsible for storing the global SDK values such as the `access_token` and the base `url` for the API endpoints.

```python
class LotrSDK():
    """The One API client object

    Use this object to interact with the https://the-one-api.dev API.
    """

    def __init__(self, access_token: str, host: str='https://the-one-api.dev/v2') -> None:
        """
        Construct the the-one-api API object.

        Args:
            access_token (str): The access token to authenticate with. See \
                https://the-one-api.dev/documentation#3
            host (str, optional): API endpoint for the-one-api to use for all \
                requests. Defaults to `https://the-one-api.dev/v2`.
        """
        # Define the client attributes
        self._access_token = access_token
        self.host = host
        self.headers = {
            "Authorization": "Bearer {}".format(self._access_token)
        }

        # Instantiate endpoint groups
        self.movie = MovieAPI(self.host, self.headers)
```

In the individual python file for each of the endpoint groups, the endpoint group class implements the endpoints for that endpoint group. For example, the `MovieAPI` implements all endpoints with a `/movie` prefix.