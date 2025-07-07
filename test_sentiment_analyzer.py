import unittest
from sentiment_analyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):
    
    def setUp(self):
        self.analyzer = SentimentAnalyzer()

    def test_clean_text(self):
        text = "Hello @user! Visit http://example.com #amazing"
        cleaned = self.analyzer.clean_text(text)
        self.assertNotIn("@", cleaned)
        self.assertNotIn("#", cleaned)
        self.assertNotIn("http", cleaned)

    def test_analyze_sentiment_positive(self):
        result = self.analyzer.analyze_sentiment("I love it")
        self.assertEqual(result["sentiment"], "Positive")

if __name__ == '__main__':
    unittest.main()
