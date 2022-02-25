from typing import Dict

from config.get_id_token import Access


class ApiConfig():
    """
    More info at https://pydantic-docs.helpmanual.io/usage/settings/
    """

    API_URL: str = "https://api.inferencehub.io/model"
    # API_URL: str = "https://api-dev.inferencehub.io/model"
    # API_URL: str = "http://localhost:3000/model"    # For local testing with lambda
    # API_URL: str = "http://localhost:8080/model"    # For local testing with python app

    settings: Access
    access_token: str
    headers: Dict

    def __init__(self):
        self.settings = Access()
        self.access_token = self.settings.get_access_token()
        self.headers = {
            "Authorization": f"{self.access_token}",
        }
