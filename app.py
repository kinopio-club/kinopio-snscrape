from flask import Flask, request
from snscrape.modules.twitter import snscrape

app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello, World!'

@app.route('/tweets')
def tweets():
  # https://github.com/JustAnotherArchivist/snscrape/issues/552
  scraper = snscrape.modules.twitter.TwitterUserScraper('textfiles')
  print(scraper)
  # for tweet in scraper.get_items():
  #   print(tweet.url)
  return 'yolo'