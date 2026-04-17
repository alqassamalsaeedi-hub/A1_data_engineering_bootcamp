import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os

def scrape_finance_to_csv():
    url = "https://www.x-rates.com/table/?from=USD&amount=1"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', class_='tablesorter')
        rows = table.find_all('tr')[1:16]
        
        currencies = []
        rates = []
        
        for row in rows:
            cols = row.find_all('td')
            currencies.append(cols[0].text.strip())
            rates.append(cols[1].text.strip())
            
        # إنشاء DataFrame (جدول بيانات)
        df = pd.DataFrame({
            'Currency': currencies,
            'Rate': rates,
            'Last_Updated': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        # حفظ البيانات في ملف CSV
        df.to_csv('finance_data.csv', index=False, encoding='utf-8-sig')
        print(f" file updated at : finance_data.csv  {df['Last_Updated'].iloc[0]}")
        
    except Exception as e:
        print(f" error {e}")

if __name__ == "__main__":
    scrape_finance_to_csv()