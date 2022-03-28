from datetime import datetime
import re

def top_retweets(dataset):
  retweets_dict = {}
  for tweet in dataset:
    retweets_dict[tweet['url']] = tweet['retweetCount']
  sorted_retweets = sorted(retweets_dict.items(), key=lambda item: item[1], reverse=True)
  return sorted_retweets[:10]

def top_users(dataset):
  users_dict = {}
  for tweet in dataset:
    users_dict[tweet['user']['username']] = tweet['user']['statusesCount']
  sorted_users = sorted(users_dict.items(), key=lambda item: item[1], reverse=True)
  return sorted_users[:10]

def top_days(dataset):
  days_dict = {}
  for tweet in dataset:
    date = datetime.strptime(tweet["date"][:-5], '%Y-%m-%dT%H:%M:%S+').date()
    if date not in days_dict.keys():
      days_dict[date] = 1
    else:
      days_dict[date] += 1
  sorted_days = sorted(days_dict.items(), key=lambda item: item[1], reverse=True)
  return sorted_days[:10]

def top_hashtags(dataset):
  hashtags_dict = {}
  for tweet in dataset:
    hashtags = re.findall(r"#(\w+)", tweet["content"])
    for hashtag in hashtags:
      if "#"+hashtag not in hashtags_dict.keys():
        hashtags_dict["#"+hashtag] = 1
      else:
        hashtags_dict["#"+hashtag] += 1
  sorted_hashtags = sorted(hashtags_dict.items(), key=lambda item: item[1], reverse=True)
  return sorted_hashtags[:10]
