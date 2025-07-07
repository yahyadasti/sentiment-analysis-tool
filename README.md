AI-Powered Sentiment Analysis Tool 
A versatile sentiment analysis tool built with Python. It analyzes text from direct input, .txt files, or .csv files and categorizes it as Positive, Negative, or Neutral. Features both a command-line interface and a Streamlit web app.

Features
Multiple Input Modes: Analyze text pasted directly, from a single command-line argument, or from entire files.

File Support: Batch process sentiment analysis for each line in a .txt or .csv file.

Text Cleaning: Automatically removes URLs, mentions, hashtags, and special characters before analysis.

Dual Interfaces: Choose between an interactive web application and a flexible command-line tool.
Export Results: Download analysis results as a .csv file from the web interface.

# How to Use
# 1. Installation
First, clone the repository and install the necessary dependencies.


# Clone this repository
git clone https://github.com/your-username/sentiment-analysis-tool.git

# Navigate to the project directory
cd sentiment-analysis-tool

# Install required libraries
pip install -r requirements.txt
# 2. Running the Web App 
The most user-friendly way to use the tool is via the Streamlit web interface.
streamlit run sentiment_web.py
This will open a new tab in your browser where you can paste text or upload files for analysis.

# 3. Using the Command-Line Interface (CLI) 
The CLI provides several ways to analyze text.

# - Analyze a single string:
python main.py --text "This is a wonderful experience."


# - Analyze a file:
The tool can process .txt and .csv files. It will analyze each line or the first column of each row.
python main.py --file sample_reviews.txt

# - Analyze pasted text directly:
Run the script without any arguments to enter an interactive mode.
python main.py
Paste your text, and then press Enter on an empty line to see the result.

# 4. Running Tests
The project includes unit tests to ensure the core analyzer is working correctly.

python -m unittest test_sentiment_analyzer.py
