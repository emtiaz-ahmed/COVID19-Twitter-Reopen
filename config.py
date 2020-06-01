
ROOT_PATH = "/Users/mdrafiqulrabin/Desktop/COVID19/COVID19-Twitter-Reopen/"
DATA_PATH = ROOT_PATH + "Data/"

RX_SPACE   = r'\s+'
RX_EMAIL   = r'[a-zA-Z0-9+_\-\.]+@[0-9a-zA-Z][.-0-9a-zA-Z]*.[a-zA-Z]+'
RX_URL     = r'http\S+'
RX_HASHTAG = r'#(\w+)'
RX_MENTION = r'@(\w+)'
RX_ONLY_AB = r'[^A-Za-z]'

ALL_DATA = DATA_PATH + "covid19_all.csv"
US_DATA = DATA_PATH + "covid19_us.csv"
US_REOPEN_DATA = DATA_PATH + "covid19_us_reopen.csv"
US_REOPEN_EMOTION = DATA_PATH + "covid19_us_reopen_emotion.csv"

US_STATES = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'United States of America': 'USA'
}

def get_ibm_tone_format_tweet(tweet):
    tweet = tweet.replace('\n\n','; ') #newlines
    if (tweet.startswith("RT ")): tweet = ' '.join(tweet.split()[2:]) #re-tweet
    tweet = re.sub(cf.RX_MENTION, '', tweet) #mention
    tweet = re.sub(cf.RX_HASHTAG, '', tweet) #hashtag
    tweet = re.sub(cf.RX_URL, '', tweet) #url
    tweet = re.sub(cf.RX_EMAIL, '', tweet) #email
    tweet = re.sub(r"[^A-Za-z0-9,;-_/]", ' ', tweet) #non-char ,;'-_/
    tweet = ' '.join(tweet.split()) #white spaces
    tweet = (tweet if tweet[-1].isalnum() else tweet[:-1]) + " ." #dot
    tweet = "{}{}".format(tweet[0].upper(),tweet[1:])
    return tweet.strip()

