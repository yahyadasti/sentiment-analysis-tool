# sentiment_web.py — Streamlit Web App for Sentiment Analysis
"""
A simple web interface for the SentimentAnalyzer using Streamlit.
Users can paste multiple lines of text, upload .txt/.csv files, and view sentiment analysis
results with summary statistics and CSV export.
"""

import streamlit as st
import pandas as pd
from sentiment_analyzer import SentimentAnalyzer

analyzer = SentimentAnalyzer()

st.set_page_config(page_title="AI Sentiment Analyzer", layout="centered")
st.title("📊 AI-Powered Sentiment Analysis Tool")

mode = st.radio("Choose input mode:", ["Paste Text", "Upload File"])

results = []

if mode == "Paste Text":
    user_input = st.text_area("Paste one or more lines of text (each line will be analyzed):")
    if st.button("Analyze Text"):
        lines = [line.strip() for line in user_input.strip().split('\n') if line.strip()]
        for line in lines:
            result = analyzer.analyze_sentiment(line)
            results.append(result)

elif mode == "Upload File":
    uploaded_file = st.file_uploader("Upload a .txt or .csv file", type=["txt", "csv"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".txt"):
            lines = uploaded_file.read().decode("utf-8").splitlines()
        else:
            df = pd.read_csv(uploaded_file)
            lines = df.iloc[:, 0].dropna().astype(str).tolist()
        for line in lines:
            if line.strip():
                result = analyzer.analyze_sentiment(line)
                results.append(result)

if results:
    df_results = pd.DataFrame(results)
    st.subheader("🔍 Individual Results")
    st.dataframe(df_results[["text", "sentiment", "confidence"]])

    st.subheader("📊 Summary")
    summary = df_results["sentiment"].value_counts().to_dict()
    st.write(f"✅ Positive: {summary.get('Positive', 0)}")
    st.write(f"❌ Negative: {summary.get('Negative', 0)}")
    st.write(f"⚠️ Neutral: {summary.get('Neutral', 0)}")

    st.download_button(
        label="📥 Download Results as CSV",
        data=df_results.to_csv(index=False).encode('utf-8'),
        file_name="sentiment_results.csv",
        mime="text/csv"
    )
