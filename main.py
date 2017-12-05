import settings as env
from twitterFunctions import TwitterFunctions as Twitter
import weighted_simulator as Simulator
import sys


if __name__ == '__main__':
    Twitter.get_all_tweets(screen_name=sys.argv[1])
    Simulator.gen_from_twitter_api_json(file_name=sys.argv[1] + "_tweets")
