# SDK Design Architecture

This SDK is python implementation for the [the-one-api.dev](https://the-one-api.dev/) API.

The SDK implements a **[single client object](lotr_sdk/__init__.py)** that can be instantiated and would provide access to the various endpoints.

```python
from lotr_sdk import LotrSDK
import os

ACCESS_TOKEN = os.getenv("THE_ONE_API_ACCESS_TOKEN")

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

## Contributing to the SDK

1. To contribute to the SDK, first clone the souce repository:

    ```sh
    git clone https://github.com/cynepton/isaac-lotr-sdk.git
    ```

    The dependency and package management is done using [poetry](https://python-poetry.org/) which makes it very easy to manage dependencies, package and build the module and also publish to PyPI.

2. After cloning the repository, create a virtual environment:

    > **Requirements:**
    > - [Python version 3.5 or later](https://www.python.org/downloads/)

    The `python3` command is the python executable in your development environment. It may vary depending on the development environment. In some cases it could be `python`.

    ```sh
    python3 -m venv ./venv
    ```

3. Source the virtual environment in the terminal session:

    ```sh
    source venv/bin/activate
    ```
    This could be slightly different on a windows system:
    ```sh
    source venv/Scripts/activate
    ```

4. In the virtual environment install poetry:

    ```sh
    pip install poetry==1.4.0
    ```
    Or just install from the `requirements.txt` file:
    ```sh
    pip install -r requirements.txt
    ```

    Confirm poetry is installled correctly by running:
    ```sh
    poetry --version
    ```
    You should see a response like:
    ```txt
    Poetry (version 1.4.0)
    ```

5. After installing poetry, it manages all other dependencies. To install other required dependencies, run:
    ```sh
    poetry install
    ```
    It automatically uses the dependencies defined in the [`poetry.lock`](poetry.lock) file and the `[tool.poetry.dependencies]` section in the [`pyproject.toml`](pyproject.toml) file to install all the required dependencies in your environment.

6. You can start working on the SDK now. See the [Project Architecture](#project-architecture) for details on the directory structure.

### Adding new python libraries

If you wish to add new python libraries, add them to the `[tool.poetry.dependencies]` section in the [`pyproject.toml`](pyproject.toml) and then install the new libraries with:
```sh
poetry install
```
Poetry would handle the task of install and managing this dependency and would also update the [`poetry.lock`](poetry.lock) file.

### Publishing to PyPI

1. To publish to PyPI, first update the `version` value in the `[tool.poetry]` section in the [`pyproject.toml`](pyproject.toml)file.

2. Next, do a build with:

    ```sh
    poetry build
    ```

    This would create a `.whl` and a `.tar.gz` file in the `dist` dirtectory in your development environment.

3. Next publish the package with:
    ```sh
    poetry publish -u $PYPI_USERNAME -p $PYPI_PASSWORD
    ```
    Replace the `$PYPI_USERNAME` and `$PYPI_PASSWORD` with the PYPI username and password for the package.
