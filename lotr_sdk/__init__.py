from .movie import MovieAPI

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
