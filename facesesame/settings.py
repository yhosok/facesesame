import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SESAME_KEY = os.environ.get("SESAME_KEY")
SESAME_UUID = os.environ.get("SESAME_UUID")
GMAIL_USER = os.environ.get("GMAIL_USER")
GMAIL_PASS = os.environ.get("GMAIL_PASS")
GMAIL_TO = os.environ.get("GMAIL_TO")
SEND_EMAIL = os.environ.get("SEND_EMAIL") == "True"
