from prettyconf import config

class Settings:

    SELLERS_API = config("SELLERS_API")
    TOKEN_SELLERS = config("TOKEN_SELLERS")
    SCHEDULE_API = config("SCHEDULE_API")
    TOKEN_SCHEDULE = config("TOKEN_SCHEDULE")

settings = Settings()