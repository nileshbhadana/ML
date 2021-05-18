#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:42:58 2019

@author: nilesh
"""
import tweepy
import textblob

consumer_key = "HtWbEX5fjAAKM6" 
consumer_secret = "2dXvLlGCvlhwkS6YDNtmwoSyAQaMit0"
access_key = "CVnY1e5cf0qYe4RSQoJPXHNL7"
access_secret = "rQLhO6X=IGSfzj458YsF32bPQbis"


def getting_tweets(query):
    auth= tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_key,access_secret)
    api=tweepy.API(auth)
    number_of_tweets=10
    #tweets=api.user_timeline(screen_name=username,count=number_of_tweets)
    tweets=api.search(q=query,count=number_of_tweets,lang='en')
    temp=[]
    tweets_for_csv=[tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        temp.append(j)
        print(j)
    #print(temp)
    analysis=textblob(temp)
    print(len(temp))

if __name__=='__main__':
    query=input("Enter topic:")
    getting_tweets(query)
