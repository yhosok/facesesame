import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SESAME_KEY = os.environ.get("SESAME_KEY")
SESAME_UUID = os.environ.get("SESAME_UUID")
