#!/usr/bin/env python

from bottle import route, run, hook, response
from json import dumps
from core.sentiments_analyser import SentimentsAnalyser

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/')
def root():
    result = {
        "USAGE" :
            [
                {"Usage and examples" : "/"},
                {"Sentiments analysis" :"/sentiments/text"},
            ]
    }
    return result

@route('/sentiments/<text>')
def sentiments(text):
    analyser = SentimentsAnalyser()
    analysis = analyser.analyze(text)
    result = {
        "Text"   : text,
        "Result" : analysis
    }
    return result

@route('/example')
def example():
    example = [
        { "id": 1, "word": "Hexacta", "date": "2015-08-01", "positive": 33, "neutral": 13, "negative": 15 },
        { "id": 2, "word": "Hexacta", "date": "2015-08-02", "positive": 14, "neutral": 10, "negative": 12 },
        { "id": 3, "word": "Hexacta", "date": "2015-08-03", "positive": 25, "neutral": 4, "negative": 22 },
    ]
    response.content_type = 'application/json'
    return dumps(example)


run(host='0.0.0.0', port=9001, reloader=True)
