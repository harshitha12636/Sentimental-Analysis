# Import necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download required NLTK data
nltk.download('vader_lexicon')

# Initialize sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    if scores['compound'] > 0:
        return "Positive"
    elif scores['compound'] < 0:
        return "Negative"
    else:
        return "Neutral"

# Test the function
text = "I love this product!"
print(analyze_sentiment(text))  

text = "I hate this product!"
print(analyze_sentiment(text))  

text = "This product is okay."
print(analyze_sentiment(text)) 