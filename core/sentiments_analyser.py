#!/usr/bin/env python

from textblob import TextBlob

class SentimentsAnalyser:

    POSITIVE = "Positive"
    NEUTRAL = "Neutral"
    NEGATIVE = "Negative"

    def analyze(self, text=u""):
        text_blob = TextBlob(text)
        text_blob_en_traslation = text_blob.translate(to='en')
        polarity = text_blob_en_traslation.polarity
        subjectivity = text_blob_en_traslation.subjectivity
        self.log(text, text_blob_en_traslation)
        if (polarity > 0.3 and subjectivity < 0.7):
            return self.POSITIVE
        elif (0 <= polarity <= 0.3):
            return self.NEUTRAL
        else:
            return self.NEGATIVE

    def log(self, text, text_blob_en_traslation):
        print("Result ### Polarity=%s Subjectivity=%s Text=%s " % (
        text_blob_en_traslation.polarity, text_blob_en_traslation.subjectivity, text))
