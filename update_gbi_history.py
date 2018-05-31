#!/usr/bin/python

import tweepy
import json
import urllib3

import gbi_conf as cfg


# Ugh, disable warning which seem to be impossible to avoid.
urllib3.disable_warnings()

statusList = []

# Read existing JSON history file and find ID for most recent Tweet
try:
  with open(cfg.history_file, 'r') as jsonfile:
    statusList = json.load(jsonfile)
except:
  pass

print("read " + str(len(statusList)) + " previous statuses")

sinceId = 0

if len(statusList) > 0:
  sinceId = statusList[-1]['id']
  print("getting new tweets since " + str(sinceId))

# Fetch newer Tweets

status_map = []

auth = tweepy.AppAuthHandler(cfg.API_key, cfg.API_secret)
api = tweepy.API(auth)

if sinceId == 0:
  statuses = tweepy.Cursor(api.user_timeline, cfg.GBI_user_ID).items(cfg.max_tweet_request_size)
else:
  statuses = tweepy.Cursor(api.user_timeline, user_id = cfg.GBI_user_ID, since_id = sinceId).items(cfg.max_tweet_request_size)

for status in statuses:
	status_map.append({"text": status.text, "time": status.created_at.isoformat(), "id": status.id})

status_map.reverse()

print("got " + str(len(status_map)) + " new tweets")

# Write updated history back to original JSON file.

statusList.extend(status_map)

with open(cfg.history_file, 'w') as jsonfile:
  json.dump(statusList, jsonfile, indent=2)
