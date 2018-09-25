# philly_transactions
Philadelphia Election finance data scraped from my citizensunited repo

Storing here since the data is relatively static and it's a little more accessible to everyone than a database (also free).

The raw .csv files are stored in `philly_transactions{year}.csv`, and the combined data set is in `philly_transactions.csv`. The file used to clean and compile the raw data is in `philly_clean.py`.

Issues:
The year-to-date data for the year 2010 gets cut off and throws errors. I added a `"` at the end of the last line to make the .txt readable. May go back and get data by cycle.


