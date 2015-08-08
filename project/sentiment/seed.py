# from sentiment.secret import * (pull in API credentials)
from twython import Twython
from sentiment.models import Tweet
import time

candidate_list = ["Trump", "Bush", "Walker", "Huckabee", "Carson", "Cruz", "Rubio", "Paul", "Christie", "Kasich"]

def seed(query, starting_max_id, ending_max_id, count, number_of_queries):
    id_range = ending_max_id - starting_max_id
    iteration = id_range // number_of_queries
    for x in range(number_of_queries):
        twitter = Twython(APP_KEY, APP_SECRET)
        search = twitter.search(q=query, max_id=starting_max_id, count=count)
        tweets = search['statuses']
        for tweet in tweets:
            for candidate in candidate_list:
                if candidate in tweet['text']:
                    try:
                        formatted_timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(tweet['created_at'],'%a %b %d %H:%M:%S +0000 %Y'))
                        tweet_object = Tweet(text =tweet['text'], date=formatted_timestamp, query_string=query, candidate=candidate)
                        tweet_object.save()
                    except:
                        continue
        starting_max_id += iteration
