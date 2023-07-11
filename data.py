from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
data = requests.get(url).text
soup = bs(data, "html.parser")
table = soup.find('table', class_='wikitable sortable')

headers = table.find_all('th')
columns = [header.text.strip() for header in headers]

rows_data = []

rows = table.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    if row_data:
        rows_data.append(row_data)

print("\t".join(columns))

for row_data in rows_data:
    print("\t".join(row_data))

df = pd.DataFrame(rows_data, columns=columns)

print("exporting to dataframe...")

print(df)
print("exported data to dataframe")

df.to_csv("billionaires_data.csv", index=False)
print("CSV file exported successfully.")

download_link = '<a href="billionaires_data.csv" download>Download CSV</a>'
print(f"Click the link to download the CSV file: {download_link}")