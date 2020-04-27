from flask import render_template, request
from . import main
from newsapi import NewsApiClient
import os

newsapi = NewsApiClient(os.environ.get("NEWS_API_KEY"))
all_sources = newsapi.get_sources()['sources']


@main.route('/')
def index():
    """ View root page function that returns the index page and it's data """

    headlines = newsapi.get_top_headlines(country='us')['articles']
    title = "Up to date news headlines"
    return render_template('index.html', title=title, headlines=headlines, all_sources=all_sources)


@main.route('/source/<source_id>')
def source_articles(source_id):
    """ View root page function that returns articles from a source """

    source_results = newsapi.get_everything(sources=source_id)['articles']
    title = f'Source: {source_id}'
    return render_template('results.html', title=title, results=source_results, all_sources=all_sources)


@main.route('/category/<category>')
def category_articles(category):
    """ View root page function that returns articles of a given category """

    category_results = newsapi.get_top_headlines(category=category, country='us')['articles']
    title = category
    return render_template('results.html', title=title, results=category_results, all_sources=all_sources)


@main.route('/search')
def query_articles():
    """ View root page function that returns the index page and it's data """

    query = request.args.get('q')
    search_results = newsapi.get_everything(q=query, language='en')['articles']
    title = query
    return render_template('results.html', title=title, results=search_results, all_sources=all_sources)
