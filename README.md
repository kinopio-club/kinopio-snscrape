# Kinopio-Twitter

A python3 micro-service that retrieves twitter conversation threads

# Install

    pip3 install -r requirements.txt

# Run
    export FLASK_APP=app
    export FLASK_DEBUG=true
    flask run
    http://127.0.0.1:5000

# Update Scraper

Occassionally, if threads aren't being returned, [snscraper](https://github.com/JustAnotherArchivist/snscrape) might need to be updated

    pip3 install --upgrade snscrape

Then test and redeploy
