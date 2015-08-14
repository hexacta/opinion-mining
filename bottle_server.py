#!/usr/bin/env python

from bottle import route, run, hook, response
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

run(host='0.0.0.0', port=9001, reloader=True)
