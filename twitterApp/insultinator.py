#!/usr/bin/env python3

import tweepy

consumer_key = '4DU1DCjvRhBgJaPvqHXsN9MFp'
consumer_secret = '45v2o4wcprknOswYdpwSr5BcwKQlwKaVXSXPPVhOHuuEWLMmj'
access_token = '1178793206693191680-MM65wnNEVPFetXKBl0yYcOO1E8mf4I'
access_token_secret = 'Ncb26c2YPpLBAA66PB74ydhZTHvb1RjK6rt2Aw0QttZQw'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token.strip(), access_token_secret.strip())

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
	print(tweet.text)
