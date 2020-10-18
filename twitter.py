import tweepy
import time

auth = tweepy.OAuthHandler('J0UjmyOsjZ7zYSpYnWrXNEOva',
                           'Kv2tI5Vv2NDPA0J4HI3RfbJCXr8XvJRYfx6byJOIxXecAXbZWD')
auth.set_access_token('1256998173513601025-a66icjGaHBv1JvuJiLKhhkVz9ShEqG',
                      '0KT5p6UZIH7ULjN6Zv9nYnXwjwd77SAqzGAvg8PV4Zv7z')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

print(user.screen_name)

for friends in tweepy.Cursor(api.friends).items():
    print(friends.name)


search = 'Lakers'
nrTweets = 1
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet was liked')
        tweet.retweet()
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
