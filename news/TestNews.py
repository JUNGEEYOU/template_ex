from news.GoogleParser import GoogleParser
from news.YahooParser import YahooParser

if __name__ == "__main__":
    google = GoogleParser()
    yahoo = YahooParser()

    print("Google:")
    google.print_top_news()
    print("Yahoo:")
    yahoo.print_top_news()
