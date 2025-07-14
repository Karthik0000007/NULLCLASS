from analyzer import analyze_sentiment

test_cases = [
    "I'm so happy with the help I received today!",
    "The issue was resolved, but it took too long.",
    "Why is your service always terrible? I'm so frustrated.",
    "Thank you, everything works perfectly now.",
    "This is fine, I guess.",
    "Absolutely the worst experience I've ever had.",
    "Nothing special, just okay.",
    "Love the support team! Very responsive.",
    "I can't believe how bad this is.",
    "Appreciate the quick response!"
]

for i, text in enumerate(test_cases, 1):
    sentiment = analyze_sentiment(text)
    print(f"{i:02d}. '{text}' → {sentiment}")
