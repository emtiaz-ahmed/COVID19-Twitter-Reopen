
ROOT_PATH = "/Users/mdrafiqulrabin/Desktop/COVID19-Twitter-Sentiment/"
DATA_PATH = ROOT_PATH + "Data/"

RX_SPACE   = r'\s+'
RX_EMAIL   = r'[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+'
RX_URL     = r'http\S+'
RX_HASHTAG = r'#(\w+)'
RX_MENTION = r'@(\w+)'
RX_ONLY_AB = r'[^A-Za-z]'

ALL_DATA = DATA_PATH + "covid19.csv"
US_DATA = DATA_PATH + "covid19_us.csv"
US_REOPEN_DATA  = DATA_PATH + "covid19_us_reopen.csv"

