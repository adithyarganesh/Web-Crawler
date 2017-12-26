import tweepy
from textblob import TextBlob

consumer_key = '0SFAmbuyz0CABDsW8Z3Rig4jH'
consumer_secret = 'tAoRZy8Z24A7hHZ2VDoB83uiuBR6SvY2aD9roQnOn1VH0JYSjs'

access_token = '804723237410181121-Gh0lgnhuHpzJ1oiDRywcP9tuG4uVx09'
access_token_secret = 'HzaflNZlt3FGYFo3qux11tPFG598iiC4VfPd6Sx3tGP6K'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

topic = input("Enter word")
public_tweets = api.search(topic)

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
