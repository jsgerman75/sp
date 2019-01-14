from bs4 import BeautifulSoup
import requests
import pandas as pd
df = pd.DataFrame()
with  open('axiomatic.html') as html_file:
    soup = BeautifulSoup(xml)

match = soup.find('table',{'class':'card-table items'}).text.strip()
print(match)



