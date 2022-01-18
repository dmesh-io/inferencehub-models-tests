from pycognito import Cognito
from pydantic import BaseSettings


class Access(BaseSettings):
    USER_POOL_ID: str
    APP_CLIENT_ID: str
    CICD_USER_NAME: str
    CICD_PASSWORD: str

    class Config:
        env_file = 'config/.env'
        env_file_encoding = 'utf-8'

    def get_access_token(self):
        u = Cognito(
            user_pool_id=self.USER_POOL_ID,
            client_id=self.APP_CLIENT_ID,
            username=self.CICD_USER_NAME,
        )

        u.authenticate(password=self.CICD_PASSWORD)
        return u.id_token


if __name__ == "__main__":
    settings = Access()
    id_token = settings.get_access_token()
    print(id_token)
