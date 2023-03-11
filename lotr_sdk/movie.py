import requests
from .utils.logger import get_logger
logger = get_logger(__name__)

class MovieAPI:

    def __init__(self, host: str, custom_headers: dict, **kwargs) -> None:
        """
        Construct the object for the movie endpoints group
        """
        self.host = host
        self.custom_headers = custom_headers


    def _construct_params(self, *args, **kwargs):
        """Helper method to constructs a parameter string to append to the URL
        """
        param_string = "?"
        # Add all positional arguments
        for arg in args:
            param_string += str(f"{arg}&")
        # Add all keyword arguments
        for key, value in kwargs.items():
            param_string += str(f"{key}={value}&")
        return param_string

    def getMovies(self, *filters, **queries) -> dict:
        """Implementation of the `/movie` endpoint

        Args:
            limit (int, optional): The number of records returned per page. Defaults to 1000.
            page (int, optional): The page number to return. Defaults to 1.
            offset (int, optional): _description_. Defaults to 0.
        """
        # Construct the URL string
        url = "{}/movie".format(self.host)
        # Get the params
        params = ""
        if filters or queries:
            params = self._construct_params(*filters, **queries)
        logger.info(f"Requesting list of movies from the endpoint: {url}{params}")

        # Add a try block to catch any errors that we may not be aware of yet
        try:
            # Send the API request and parse the response to a python dict object
            response = requests.get(f"{url}{params}", headers=self.custom_headers).json()
            return response
        except Exception as e:
            logger.error(f"Request failed with error: {e}")
