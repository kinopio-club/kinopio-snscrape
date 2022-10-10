# Kinopio-Twitter

A python3 micro-service that retrieves twitter conversation threads

Hosted on [railway.app](https://railway.app/project/84754a18-6964-4798-89b4-d97afe29497b)

# Install

    pip3 install -r requirements.txt

# Run
    python3 main.py
    http://127.0.0.1:5000

# Routes

    http://127.0.0.1:5000/twitter-thread (body: text, username, conversationId, url)

# Update Scraper

Occassionally, if threads aren't being returned, [snscraper](https://github.com/JustAnotherArchivist/snscrape) might need to be updated

    pip3 install --upgrade snscrape

Then test and redeploy
