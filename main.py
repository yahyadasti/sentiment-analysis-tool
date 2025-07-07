# main.py
import argparse
import sys
from sentiment_analyzer import SentimentAnalyzer

def get_multiline_input() -> str:
    print("Paste your text (press Enter twice to submit):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return " ".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Sentiment Analysis Tool"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-t', '--text',
        type=str,
        help='Analyze a single text input'
    )
    group.add_argument(
        '-f', '--file',
        type=str,
        help='Analyze text from a .txt or .csv file'
    )
    args = parser.parse_args()

    analyzer = SentimentAnalyzer()

    try:
        if args.text:
            result = analyzer.analyze_sentiment(args.text)
            print(f"\nText: {result['text']}")
            print(f"Sentiment: {result['sentiment']} (Confidence: {result['confidence']:.2f})")
        elif args.file:
            results = analyzer.analyze_file(args.file)
            for item in results:
                print(f"\nText: {item['text']}")
                print(f"Sentiment: {item['sentiment']} (Confidence: {item['confidence']:.2f})")
                print('-' * 40)
        else:
            pasted = get_multiline_input()
            result = analyzer.analyze_sentiment(pasted)
            print(f"\nText: {result['text']}")
            print(f"Sentiment: {result['sentiment']} (Confidence: {result['confidence']:.2f})")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
