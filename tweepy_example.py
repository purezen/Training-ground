#!/usr/bin/env python

import tweepy

public_tweets = tweepy.api.public+timeline()
for tweet in public_tweets:
	print tweet.text
