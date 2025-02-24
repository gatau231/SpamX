import os
from os import getenv as env
from SpamX.functions.logger import LOGS
from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

API_ID = int(env("API_ID", None))
if API_ID is None:
    LOGS.error("26689028")
    quit(1)

API_HASH = str(env("API_HASH", None))
if API_HASH is None:
    LOGS.error("34d0c2bd1992f199a8b8f9d5e01d5feb")
    quit(1)

ASSISTANT_TOKEN = str(env("ASSISTANT_TOKEN", None))
if ASSISTANT_TOKEN is None:
    LOGS.error("7751492434:AAGouUbYBdmpdCo5KNL49PkPmgoacNyXmCU")
    quit(1)

OWNER_ID = int(env("OWNER_ID", None))
if OWNER_ID is None:
    LOGS.error("7438166703")
    quit(1)

DATABASE_URL = str(env("DATABASE_URL", None))
if DATABASE_URL is None:
    LOGS.error("Please set your DATABASE_URL!")
    quit(1)

LOGGER_ID = str(env("LOGGER_ID", None))
if LOGGER_ID is None:
    LOGS.error("Please set your LOGGER_ID! (make a private group add assistant in that group & promote as Admin!)")
    quit(1)

# --- ETC
HANDLER = env("HANDLER", ".")
PING_MSG = env("PING_MSG", None)
ALIVE_MSG = env("ALIVE_MSG", None)
ALIVE_MEDIA = env("ALIVE_MEDIA", None)
MULTITASK = env("ALIVE_MEDIA", False)
