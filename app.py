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
  tweets = []
  userName = request.args.get('userName', '')
  conversationId = request.args.get('conversationId', '')
  print('💖',userName, conversationId)
  if (not userName or not conversationId):
    return "Query params missing", 400



  # search for every tweet by the user, and filter for tweets with the right conversation id

  # https://github.com/JustAnotherArchivist/snscrape/issues/552
  print('🍋',snscrape.modules.twitter)

  scraper = snscrape.modules.twitter.TwitterUserScraper(userName)
  items = scraper.get_items()

  print('🍅', next(items))

  for tweet in scraper.get_items():
    # print(dir(tweet))

    print('🌷',tweet.conversationId, tweet.content, tweet.url)

    # // filter for tweets where tweet.conversationId === conversationId
    # // create object {}
    # // push into tweets

  return {
    'tweets': tweets
  }


  # add error / 500 returns when scraper fails (eg userid is wrong or something)


# http://127.0.0.1:5000/tweets?userId=234&conversationId=234234

# conversationId
# quotedTweet
# inReplyToTweetId
# inReplyToUser

# ['__annotations__',
# '__class__', '__dataclass_fields__', '__dataclass_params__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cashtags',
#  'content', 'conversationId', 'coordinates', 'date', 'hashtags', 'id', 'inReplyToTweetId', 'inReplyToUser', 'json', 'lang', 'likeCount',
#  'media', 'mentionedUsers', 'outlinks', 'outlinksss', 'place', 'quoteCount', 'quotedTweet', 'renderedContent', 'replyCount', 'retweetCount', 'retweetedTweet', 'source', 'sourceLabel', 'sourceUrl', 'tcooutlinks', 'tcooutlinksss', 'url', 'user', 'username']
