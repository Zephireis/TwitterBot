import os
import tweepy
from time import sleep
import sys
import time
import uuid
import mysql.connector

mydb = mysql.connector.connect(host="",
user="division_",
passwd="!",
database="d") #use environment variables for security


auth = tweepy.OAuthHandler("hidden") #use enviroment variables for security
auth.set_access_token("hidden")#use enviroment variables for security
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()
print (user.name)
#followers = api.followers_ids("hypedgaminghgo")
#friends = api.friends_ids("hypedgaminghgo")

#for f in friends:
 #   if f not in followers:
  #      print ("Unfollow {0}?".format(api.get_user(f).screen_name))
   #     api.destroy_friendship(f)

#list of specific strings we want to check for in Tweets
already_answered = []
games = ["MCC", "ROCO"]
def reply_bot():
    mycursor = mydb.cursor(buffered=True)
    x = uuid.uuid4()
    #id = (str(x)[:4])//uuid for creating match id's
    for i in games:
        search = api.search(q=f'@hypedgaminghgo match? {i} ')
        for tweet in search:
            #tweettable = "tweeter"//database
            print (f'UserName: {tweet.user.screen_name}')
            name = tweet.user.screen_name
            print (f'Tweet: {tweet.text}')
            substring_in_list = any(tweet.text in games for tweet.text in games)
            print(substring_in_list)

            if tweet.id not in already_answered:
                print (f'Tweet: {tweet.text}')
                text = (f'@{name} match challenge sent {i}')
                try:
                    api.update_status(status=text)
                except tweepy.TweepError as error:
                    op = f'{tweet.id}' + f'{already_answered}'#adds tweet id to list if its a duplicate tweet
                    already_answered.append(tweet.id)
            else:
                print ("Tweet already answered")

while True:
    reply_bot()
    time.sleep(15)
