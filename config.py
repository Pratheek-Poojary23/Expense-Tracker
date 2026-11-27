
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key") # Development secret key

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",
        "sqlite:///expenses.db"
    )                                                       # Development database URI (SQLite)

    SQLALCHEMY_TRACK_MODIFICATIONS = False           #Disables unnecessary modification tracking.
