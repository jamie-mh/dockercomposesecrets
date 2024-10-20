from . import BaseConfig


class DevelopmentConfig(BaseConfig):
    URL = "http://localhost:5000"
    SECRET_KEY = "development"

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg://dcs:dcs@localhost:5432/dcs"

    RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
