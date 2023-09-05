import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    if sentiment['compound'] >= 0.05:
        print(sentiment['compound'])
        return "Positive"
    elif sentiment['compound'] <= -0.05:
        print(sentiment['compound'])
        return "Negative"
    else:
        print(sentiment['compound'])
        return "Neutral"

text_to_analyze = "Hospitals are incentivized to have more sick people"
result = analyze_sentiment(text_to_analyze)
print("Sentiment:", result)