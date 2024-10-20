from . import BaseConfig


def _get_secret(name: str) -> str:
    with open(f"/run/secrets/{name}", "r") as file:
        return file.read()


class ProductionConfig(BaseConfig):
    URL = "https://dcs.jmh.me"

    SECRET_KEY = _get_secret("flask_secret_key")

    RECAPTCHA_PUBLIC_KEY = "6LcQ3GYqAAAAAC8CzGcAtO2AZ8wj1cyfYul8PNYc"
    RECAPTCHA_PRIVATE_KEY = _get_secret("recaptcha_private_key")

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        password = _get_secret("database_password")
        return f"postgresql+psycopg://dcs:{password}@postgres:5432/dcs"
