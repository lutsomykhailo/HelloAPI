from pydantic_settings import BaseSettings
from pydantic import Field, SecretStr

class Settings(BaseSettings):
    app_name: str = Field(alias="name")
    api_version: str = Field()
    api_key: SecretStr = Field()


settings = Settings(
    name="Hello API",
    os.environ.get()
)