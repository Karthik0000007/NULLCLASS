import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.3:
        return "positive"
    elif compound <= -0.3:
        return "negative"
    else:
        return "neutral"

# Testing

print(analyze_sentiment("I'm really disappointed in this service."))
print(analyze_sentiment("Thanks, it was very helpful!"))


