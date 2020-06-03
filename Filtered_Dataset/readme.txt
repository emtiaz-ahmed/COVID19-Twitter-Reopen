File: covid_data_reopen.csv

 	(1) id  : Unique id of tweet
	(2) created_at : Tweet date and time
	(3) sentiment  : Sentiment of the tweet
	(4) lang : Language used in tweet

File: tune_usa_reopen.csv
	(1) id  : Unique id of tweet
	(2) created_at : Tweet date and time
	(3) lang : Language used in tweet
	(4) emotions: IBM tone analyzer json response
	(5) key_emo: Tone types

File: time_series_covid_19_confirmed_US.csv
	We collected this file from  Johns Hopkins dataset (https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data)
	(1) UID : Unique Identifier for each row entry.
	(2) Province_State: The name of the State within the USA.
	(3) Country_Region:  The name of the Country (US).
	(4) Dates (1/22/20) to (5/19/20): Daily Confirmed cases 