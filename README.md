# GBI_Scraper
Utilities to scrape Giant Bomb Infinite's Twitter feed

# Getting Started

## Prerequisites
Install [Python](https://www.python.org/) and [Tweepy](http://www.tweepy.org/)

Go to https://apps.twitter.com/ and create a new App (you only need read permissions).

Copy `gbi_conf.py.template` to `gbi_conf.py` and edit it as directed to include the API Key and Secret for the Twitter App previously created.

# Usage

Run `update_gbi_history.py` to fetch all Tweets since the most recent one from the local JSON file (default file name: `gbi_history.json`).

Run `rank.sh` to update local JSON history list and generate ranked list of most played videos (default file name: `gbi_most_played.txt`).

# License

MIT
