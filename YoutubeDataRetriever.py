'''
Created on Dec 18, 2016

@author: DucTruong
'''
#!/usr/bin/python

import httplib2
import os
import sys
import csv
import json
import re

from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from oauth2client.contrib.xsrfutil import DELIMITER




# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google Developers Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secret.json"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

# This OAuth 2.0 access scope allows for read-only access to the authenticated
# user's account, but not other types of account access.
YOUTUBE_READONLY_SCOPE = "https://www.googleapis.com/auth/youtube.readonly"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"



flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
  message=MISSING_CLIENT_SECRETS_MESSAGE,
  scope=YOUTUBE_READONLY_SCOPE)

storage = Storage("%s-oauth2.json" % sys.argv[0])
credentials = storage.get()

if credentials is None or credentials.invalid:
  flags = argparser.parse_args()
  credentials = run_flow(flow, storage, flags)

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
  http=credentials.authorize(httplib2.Http()))

# Retrieve the contentDetails part of the channel resource for the
# authenticated user's channel.

# writer = csv.DictWriter(b, fieldnames=header, delimiter = ',')
# writer.writeheader()

#a.writerows(header)
with open('allcurrentvideos.csv', 'w') as csvfile:
    header = ['video_id','categoryId','channelId','channelTitle','video_title','description','publishedAt','videoQuality','videoDuration','tags',
                'commentCount','favoriteCount','likeCount','dislikeCount','viewCount']
#     writer = csv.DictWriter(csvfile, fieldnames=header)
#     writer.writeheader()
    writer = csv.writer(csvfile)
    writer.writerow(header)
    video_response = youtube.videos().list(
      #id=playlist_item["snippet"]["resourceId"]["videoId"],
      chart = "mostPopular",
      part='snippet,recordingDetails,statistics,contentDetails'
      #regionCode="NA"
    ).execute()
    
    for video_result in video_response.get("items", []):
        if 'tags' in video_result['snippet']:
            tagStringify = ':'.join(video_result['snippet']['tags'])
        else:
            tagStringify = ''
          
        emoji_pattern = re.compile("["
                          u"\U0001F600-\U0001F64F"  # emoticons
                          u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                          u"\U0001F680-\U0001F6FF"  # transport & map symbols
                          u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                             "]+", flags=re.UNICODE)
        
        cleanedTitle = emoji_pattern.sub(r'', video_result['snippet']['localized']['title'])
        cleanedDescription = emoji_pattern.sub(r'', video_result['snippet']['localized']['description'])
        if 'commentCount' in video_result['statistics']:
            commentCount = video_result['statistics']['commentCount']
        else:
            commentCount = '-1'
        
        if 'favoriteCount' in video_result['statistics']:
            favoriteCount = video_result['statistics']['favoriteCount']
        else:
            favoriteCount = '-1'
            
        if 'likeCount' in video_result['statistics']:
            likeCount = video_result['statistics']['likeCount']
        else:
            likeCount = '-1'
            
        if 'dislikeCount' in video_result['statistics']:
            dislikeCount = video_result['statistics']['dislikeCount']
        else:
            dislikeCount = '-1'
          
        if 'viewCount' in video_result['statistics']:
            viewCount = video_result['statistics']['viewCount']
        else:
            viewCount = '-1'
              
        rowString = [
                      video_result['id'],
                      video_result['snippet']['categoryId'],
                      video_result['snippet']['channelId'],
                      video_result['snippet']['channelTitle'].encode("utf-8"),
                      cleanedTitle.encode("utf-8"),
                      cleanedDescription.encode("utf-8"),
                      video_result['snippet']['publishedAt'],
                      video_result['contentDetails']['definition'],
                      video_result['contentDetails']['duration'],
                      tagStringify.encode("utf-8"),
                      commentCount,
                      favoriteCount,
                      likeCount,
                      dislikeCount,
                      viewCount
                  ]
        writer.writerow(rowString)
    