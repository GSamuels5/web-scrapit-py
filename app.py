# app.py
from flask import Flask, render_template, request
from scraper import scrape_quotes

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', quotes=None)

@app.route('/run-scraper', methods=['POST'])
def run_scraper():
    quotes = scrape_quotes()
    return render_template('index.html', quotes=quotes)

if __name__ == '__main__':
    app.run(debug=True)
