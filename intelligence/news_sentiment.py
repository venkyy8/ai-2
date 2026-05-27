import requests

def get_news_sentiment(symbol):

    try:
        # GDELT free endpoint (no key needed)
        url = f"https://api.gdeltproject.org/api/v2/doc/doc?query={symbol}&mode=ArtList&format=json"

        res = requests.get(url, timeout=5)
        data = res.json()

        articles = data.get("articles", [])

        if not articles:
            return "NEUTRAL"

        positive_words = ["gain", "rise", "profit", "surge", "upgrade"]
        negative_words = ["fall", "loss", "crash", "downgrade", "fear"]

        score = 0

        for a in articles[:10]:
            text = (a.get("title", "") + " " + a.get("seendate", "")).lower()

            for w in positive_words:
                if w in text:
                    score += 1

            for w in negative_words:
                if w in text:
                    score -= 1

        if score > 2:
            return "BULLISH"

        if score < -2:
            return "BEARISH"

        return "NEUTRAL"

    except:
        return "NEUTRAL"