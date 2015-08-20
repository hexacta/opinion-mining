#!/usr/bin/env python

from json import dumps

from bottle import route, run, hook, response

from core.sentiments_analyser import SentimentsAnalyser


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/')
def root():
    result = {
        "USAGE":
            [
                {"Usage and examples": "/"},
                {"Sentiments analysis": "/sentiments/text"},
            ]
    }
    return result


@route('/sentiments/<text>')
def sentiments(text):
    analyser = SentimentsAnalyser()
    analysis = analyser.analyze(text)
    result = {
        "Text": text,
        "Result": analysis
    }
    return result


@route('/example')
def example():
    data = {
        "word": "Hexacta",
        "current_positive_percentage": 44,
        "current_neutral_percentage": 32,
        "current_negative_percentage": 24,
        "history": {
            "positve": [
                {"date": "2015-08-01", "value": 55},
                {"date": "2015-08-02", "value": 57},
                {"date": "2015-08-03", "value": 64},
            ],
            "neutral": [
                {"date": "2015-08-01", "value": 25},
                {"date": "2015-08-02", "value": 23},
                {"date": "2015-08-03", "value": 31},
            ],
            "negative": [
                {"date": "2015-08-01", "value": 20},
                {"date": "2015-08-02", "value": 10},
                {"date": "2015-08-03", "value": 5},
            ]
        }
    };
    response.content_type = 'application/json'
    return dumps(data)


run(host='0.0.0.0', port=9001, reloader=True)
