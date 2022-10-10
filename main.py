from flask import Flask, request
import snscrape.modules.twitter
import os

app = Flask(__name__)

@app.route('/')
def hello():
  return {
    'message': 'kinopio-twitter is online',
    'docs': 'https://github.com/kinopio-club/kinopio-twitter'
  }

@app.route('/twitter-thread', methods = ['POST'])
def searchTweets():
  # init params
  body = request.json
  username = body['username']
  conversationId = body['conversationId']
  print('🍋',username, conversationId)
  if (not username or not conversationId):
    return "request body missing fields", 400
  conversationTweet = {
    "conversationId": conversationId,
    "text": body['text'],
    "url": body['url']
  }
  tweets = []
  # search
  search = f'conversation_id:{conversationId} from:{username} to:{username}'
  print('🕊',search)
  scraper = snscrape.modules.twitter.TwitterSearchScraper(search)
  items = scraper.get_items()
  for tweet in scraper.get_items():
    tweets.append({
      "conversationId": tweet.conversationId,
      "text": tweet.content,
      "url": tweet.url
    })
  tweets.reverse()
  tweets.insert(0, conversationTweet)
  return tweets


# print(dir(tweet))
# ['__annotations__',
# '__class__', '__dataclass_fields__', '__dataclass_params__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cashtags',
#  'content', 'conversationId', 'coordinates', 'date', 'hashtags', 'id', 'inReplyToTweetId', 'inReplyToUser', 'json', 'lang', 'likeCount',
#  'media', 'mentionedUsers', 'outlinks', 'outlinksss', 'place', 'quoteCount', 'quotedTweet', 'renderedContent', 'replyCount', 'retweetCount', 'retweetedTweet', 'source', 'sourceLabel', 'sourceUrl', 'tcooutlinks', 'tcooutlinksss', 'url', 'user', 'username']

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
