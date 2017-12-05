import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_CONSUMER_API_KEY = os.environ.get("TWITTER_CONSUMER_API_KEY")
TWITTER_CONSUMER_API_SECRET = os.environ.get("TWITTER_CONSUMER_API_SECRET")

TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

TWITTER_SOURCE_ID = os.environ.get("TWITTER_SOURCE_ID")
TWITTER_DESTINATION_ID = os.environ.get("TWITTER_DESTINATION_ID")
