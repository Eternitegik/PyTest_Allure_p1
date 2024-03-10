import os
from dotenv import load_dotenv

load_dotenv()


class Data:

    USER_LOGIN = os.getenv("USER_LOGIN")
    USER_PASSWORD = os.getenv("USER_PASSWORD")
