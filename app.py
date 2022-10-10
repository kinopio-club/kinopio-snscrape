from flask import Flask, request
import snscrape.modules.twitter

app = Flask(__name__)

@app.route('/')
def hello():
  return {
    'message': 'kinopio-twitter is online',
    'docs': 'https://github.com/kinopio-club/kinopio-twitter'
  }


@app.route('/tweets')
def run():
  userName = request.args.get('userName', '')
  conversationId = request.args.get('conversationId', '')
  print('💖',userName, conversationId)
  if (not userName or not conversationId):
    return "Query params missing", 400
  conversationId = int(conversationId)
  # 🕊 Search for every tweet by the user, and filter for tweets with the right conversation id
  # https://github.com/JustAnotherArchivist/snscrape/issues/552
  scraper = snscrape.modules.twitter.TwitterUserScraper(userName)
  items = scraper.get_items()
  tweets = []
  index = 0
  endIndex = None
  hasMatched = False
  for tweet in scraper.get_items():
    if index == endIndex:
      print('💣 SHOULD TERMINATE', tweets)
      break
    if tweet.conversationId == conversationId:
      tweets.append({
        "conversationId": tweet.conversationId,
        "content": tweet.content,
        "url": tweet.url
      })
      if not hasMatched:
        hasMatched = True
        endIndex = index + 100
    index += 1
  return {
    'tweets': tweets
  }


  # add error / 500 returns when scraper fails (eg userid is wrong or something)


# http://127.0.0.1:5000/tweets?userId=234&conversationId=234234

# conversationId
# quotedTweet
# inReplyToTweetId
# inReplyToUser

# print(dir(tweet))
# ['__annotations__',
# '__class__', '__dataclass_fields__', '__dataclass_params__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cashtags',
#  'content', 'conversationId', 'coordinates', 'date', 'hashtags', 'id', 'inReplyToTweetId', 'inReplyToUser', 'json', 'lang', 'likeCount',
#  'media', 'mentionedUsers', 'outlinks', 'outlinksss', 'place', 'quoteCount', 'quotedTweet', 'renderedContent', 'replyCount', 'retweetCount', 'retweetedTweet', 'source', 'sourceLabel', 'sourceUrl', 'tcooutlinks', 'tcooutlinksss', 'url', 'user', 'username']

# may not need to do
    # index: after the first convo match, search 100 more then break with what we've got
