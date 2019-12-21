from news.GoogleParser import GoogleParser
from news.YahooParser import YahooParser

if __name__ == "__main__":
    google = GoogleParser()
    yahoo = YahooParser()

    print("Google: \n", google.print_top_news())
    print("Yahoo: \n", yahoo.print_top_news())
