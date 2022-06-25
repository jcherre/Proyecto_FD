from cgitb import html
from googleapiclient.discovery import build
import json
import requests
import urllib.request
import re
import sys

api_key = "AIzaSyDf6DxDoA3FcEWmu1z3tH9Zu5xeiflOybo" # Replace this dummy api key with your own.

youtube = build('youtube', 'v3', developerKey=api_key)

ID = "AR8ENakle9s" # Replace this YouTube video ID with your own.


def scrape_comments_with_replies(name,id):
    data = youtube.commentThreads().list(part='snippet', videoId=id, maxResults='100', textFormat="plainText").execute()
    with open(name,'w') as f:
        json.dump(data, f, indent=4)
    return

def videoSearch(key, search, maxResults):
    query = search.strip("\"").replace(" ","+")
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query='+query)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    return video_ids[0:maxResults]

video_ids = videoSearch(api_key,'utec opinion',2)
for i in video_ids:
    scrape_comments_with_replies('youtube_comments_'+str(i)+'.json',i)

# data['items'][0]["snippet"]['topLevelComment']["snippet"]["textDisplay"]
