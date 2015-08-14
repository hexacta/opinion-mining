import unittest2 as unittest

from core.sentiments_analyser import SentimentsAnalyser


class SentimentsAnalyserTests(unittest.TestCase):

    def test_analyze_text(self):
        analyser = SentimentsAnalyser()

        self.assertion(analyser, "Hola", "Hello", SentimentsAnalyser.NEUTRAL)
        self.assertion(analyser, "Bien", "Good", SentimentsAnalyser.POSITIVE)
        self.assertion(analyser, "Malo", "Bad", SentimentsAnalyser.NEGATIVE)
        self.assertion(analyser, "Terrible", "Terrible", SentimentsAnalyser.NEGATIVE)

        self.assertion(analyser,
                       "Esto es lo mejor que me paso en la vida",
                       "This is the best thing that happened to me in life",
                       SentimentsAnalyser.POSITIVE)

        self.assertion(analyser,
                       "No estoy del todo seguro, pero capaz que si",
                       "I'm not entirely sure, but if able",
                       SentimentsAnalyser.NEUTRAL)

    def assertion(self, analyser, text, text_english, expected_result):
        result = analyser.analyze(text)
        self.assertEqual(result, analyser.analyze(text_english), "Sentiment analysis - Traslation error")
        self.assertEqual(result, expected_result, "Sentiment analysis - Result and expected result doesnt match")


if __name__ == "__main__":
    unittest.main()
