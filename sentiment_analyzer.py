"""
Defines the SentimentAnalyzer class for cleaning text, performing sentiment analysis,
 and processing text from files using TextBlob and regular expressions.
"""
import re
import os
import csv
from typing import List, Dict, Union
from textblob import TextBlob

class SentimentAnalyzer:
    """
    Provides methods for text preprocessing, sentiment analysis, and file-based analysis.

    Methods:
        clean_text(text: str) -> str
        analyze_sentiment(text: str) -> Dict[str, Union[str, float]]
        analyze_file(path: str) -> List[Dict[str, Union[str, float]]]
    """

    def __init__(self):
        """
        Initializes the SentimentAnalyzer. No external setup is required.
        """
        pass

    def clean_text(self, text: str) -> str:
        """
        Cleans input text by removing URLs, mentions, hashtags, special characters,
        and converting to lowercase.

        Args:
            text (str): Raw text input.
        Returns:
            str: Cleaned text.
        """
        # Remove URLs, hashtags, mentions
        text = re.sub(r"http\S+|#\S+|@\S+", "", text)
        # Remove non-alphanumeric characters (except spaces)
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        # Normalize whitespace and lowercase
        return text.lower().strip()

    def analyze_sentiment(self, text: str) -> Dict[str, Union[str, float]]:
        """
        Analyzes sentiment of a single text string using TextBlob.

        Args:
            text (str): Input text to analyze.
        Returns:
            Dict[str, Union[str, float]]: A dictionary with keys:
                'text' (original text),
                'sentiment' (Positive/Negative/Neutral),
                'polarity' (-1.0 to 1.0),
                'confidence' (0.0 to 1.0).
        """
        if not isinstance(text, str) or not text.strip():
            raise ValueError("Input text must be a non-empty string.")

        cleaned = self.clean_text(text)
        blob = TextBlob(cleaned)
        polarity = blob.sentiment.polarity
        # Confidence as absolute polarity
        confidence = abs(polarity)

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        return {
            'text': text,
            'sentiment': sentiment,
            'polarity': polarity,
            'confidence': confidence
        }

    def analyze_file(self, path: str) -> List[Dict[str, Union[str, float]]]:
        """
        Processes a text or CSV file line by line for sentiment analysis.

        Args:
            path (str): File path (.txt or .csv).
        Returns:
            List[Dict[str, Union[str, float]]]: List of sentiment results per line.
        """
        if not os.path.isfile(path):
            raise FileNotFoundError(f"File not found: {path}")

        ext = os.path.splitext(path)[1].lower()
        results: List[Dict[str, Union[str, float]]] = []

        # Read .txt as plain lines
        if ext == '.txt':
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        # Read .csv, assuming each row's first column is the text
        elif ext == '.csv':
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                lines = [row[0] for row in reader if row]
        else:
            raise ValueError("Unsupported file format. Use .txt or .csv files.")

        for line in lines:
            if not line.strip():
                continue
            result = self.analyze_sentiment(line)
            results.append(result)

        return results
