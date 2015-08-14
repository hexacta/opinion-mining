#!/usr/bin/env python

from textblob import TextBlob

# https://textblob.readthedocs.org/en/dev/quickstart.html#sentiment-analysis
# The sentiment property returns a namedtuple of the form Sentiment(polarity, subjectivity).
# The polarity score is a float within the range [-1.0, 1.0].
# The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.

text_blob_us = TextBlob(u'Simple is better than complex.')
print(" ##### US #####")
print(text_blob_us)
print(text_blob_us.sentiment)
print(text_blob_us.detect_language())

print("")

text_blob_es = TextBlob(u'Simple es mejor que complejo.')
text_blob_us_traslate = text_blob_es.translate(to='en')
print(" ##### ES #####")
print(text_blob_us_traslate)
print(text_blob_us_traslate.sentiment)
print(text_blob_us_traslate.detect_language())
