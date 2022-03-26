def top_retweets(dataset):
  retweets_dict = {}
  for tweet in dataset:
    retweets_dict[tweet['url']] = tweet['retweetCount']
  sorted_retweets = sorted(retweets_dict.items(), key=lambda item: item[1], reverse=True)
  return sorted_retweets[:10]
