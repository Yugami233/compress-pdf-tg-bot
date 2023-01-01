import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5231238723:AAFppyPBD3VKzj_-kHMXquwEVv1fAcOJCl4")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "5948230"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "dd19a00b085a219421a3717d0ae9c0d0")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
