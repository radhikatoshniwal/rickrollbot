from flask import Flask, render_template, request
import config
import praw
import time
from random import randrange


reddit=praw.Reddit(client_id=config.client_id,client_secret=config.client_secret,user_agent='Python rick roll bot v1.0 (by /u/tobllorkcir)',username=config.username,password=config.password)


# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      
    
def rickroll():

    list_of_comments=['[Found it!](https://www.youtube.com/watch?v=HPk-VhRjNI8&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx)','[You might find this useful](https://www.youtube.com/watch?v=HPk-VhRjNI8&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx)','[Found the link you been looking for](https://www.youtube.com/watch?v=HPk-VhRjNI8&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx)','[This might help](https://www.youtube.com/watch?v=HPk-VhRjNI8&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx)']
    for comment in reddit.subreddit('all').stream.comments():
        if 'link' in comment.body.lower() and comment.over_18==False and comment.author.name.lower()!='automoderator' and 'bot' not in comment.author.name.lower():
          print("yep")
          try:
            comment.reply(list_of_comments[randrange(4)])
          except:
            #countdown(600)
            continue
    return "kay bruh done"

rickroll()
