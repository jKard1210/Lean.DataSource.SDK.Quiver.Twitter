# 1. Download the data
# 2. Process (if required)
# 3. Output data for each to /temp-output-directory/alternative/quiver/twitter/{symbol}.csv

import requests
import os

QUIVER_API_KEY = os.environ["QUIVER_API_KEY"]
print(QUIVER_API_KEY)
base_url = "https://api.quiverquant.com/beta"

headers = {
    'Authorization': 'Token ' + QUIVER_API_KEY,
    'accept': 'application/json'
}

companies = requests.get(base_url+'/companies', headers=headers).json()
print(companies)

line_list = []
for c in companies:
    ticker = c['Ticker']
    ticker_twitter = requests.get(base_url + '/historical/twitter/' + ticker, headers=headers).json()
    print(ticker_twitter)
    for row in ticker_twitter:
        pass
    #     date = row['Date']
    #     followers = row['Followers']
    #     pct_change_day = row['pct_change_day']
    #     pct_change_month = row['pct_change_month']
    #     pct_change_year = row['pct_change_year']

    #     line = [date,followers,pct_change_day,pct_change_month,pct_change_year]
    #     line_list.append(','.join(line))
    # if len(line_list) < 1:
    #     continue
    # csv_lines = "/n".join(line_list)
    # # with open('/temp-output-directory/alternative/quiver/twitter/' + ticker.lower() + '.csv', 'w') as ticker_file:
    # #     ticker_file.write(csv_lines)
    # print(csv_lines)


