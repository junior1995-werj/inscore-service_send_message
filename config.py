import os
from prettyconf import config

class Settings:

    SELLERS_API = os.environ["SELLERS_API"]
    TOKEN_SELLERS = os.environ["TOKEN_SELLERS"]
    SCHEDULE_API = os.environ["SCHEDULE_API"]
    TOKEN_SCHEDULE = os.environ["TOKEN_SCHEDULE"]

settings = Settings()