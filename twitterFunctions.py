import tweepy
import json
import settings as env

class TwitterFunctions:
    @staticmethod
    def get_all_tweets(screen_name):
        #Taken from https://gist.github.com/yanofsky/5436496

        #Twitter only allows access to a users most recent 3240 tweets with this method

        #authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(env.TWITTER_CONSUMER_API_KEY, env.TWITTER_CONSUMER_API_SECRET)
        auth.set_access_token(env.TWITTER_ACCESS_TOKEN, env.TWITTER_ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)

        #initialize a list to hold all the tweepy Tweets
        alltweets = []

        #make initial request for most recent tweets (200 is the maximum allowed count)
        new_tweets = api.user_timeline(screen_name = screen_name,count=200)

        for tweet in new_tweets:
            alltweets.extend({json.dumps(tweet._json)})

        #save the id of the oldest tweet less one
        oldest = json.loads(alltweets[-1])['id'] - 1

        #keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
            print("getting tweets before {0}".format(oldest))

            #all subsiquent requests use the max_id param to prevent duplicates
            try:
                new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
            except KeyError:
                pass

            #save most recent tweets
            for tweet in new_tweets:
                alltweets.extend({json.dumps(tweet._json)})

            #update the id of the oldest tweet less one
            oldest = json.loads(alltweets[-1])['id'] - 1

            print("...{0} tweets downloaded so far".format(len(alltweets)))

        #outtweets = json.dumps(alltweets)

        #write the csv
        with open('{0}_tweets.json'.format(screen_name), 'w') as f:
            json.dump(alltweets, f)

        pass
