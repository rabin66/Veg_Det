from datetime import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://kalimatimarket.gov.np/lang/en'
html_content = requests.get(url).text
r = requests.get(url)

def scrap():
    soup = BeautifulSoup(r.content, "html.parser")
    table = soup.find('table')
    rows = table.find_all('tr')
    row_list = list()

    for tr in rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        row_list.append(row)

    df_bs = pd.DataFrame(row_list, columns=['Commodity', 'Unit', 'Miniumum', 'Maximum', 'Average'])
    d1 = datetime.now()
    filename1 = d1.strftime("%Y%m%d")
    df_bs.to_csv(filename1 + '.csv')
    print("Scrapping to get the price......... Completed")
