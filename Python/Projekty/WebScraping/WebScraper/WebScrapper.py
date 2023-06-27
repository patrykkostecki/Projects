import requests
from bs4 import BeautifulSoup
import csv
import urllib.request

www = "https://www.w3schools.com/sql/sql_exists.asp"

#zapytanie do strony www oraz pobranie elementów html do zmiennej obiekt
obiekt = urllib.request.urlopen(www)

soup = BeautifulSoup(obiekt, 'html.parser')

table = soup.find('table', {'class', 'ws-table-all notranslate'})
ilosc_wierszy = table.find_all('tr')

print('Tabela: ', len(ilosc_wierszy)-1)

wiersze = []
wiersze.append(['ProductID','ProductName','SupplierID', 'Unit','Price'])
for wiersz in ilosc_wierszy:
    data = wiersz.find_all('td')

    if len(data) == 0:
        continue

    pid = data[0].getText()
    pn = data[1].getText()
    sid = data[2].getText()
    cid = data[3].getText()
    unit = data[4].getText()
    price = data[5].getText()

    wiersze.append([pid, pn, sid, cid, unit, price])

with open('sql.csv', 'w', newline='') as plik_wynikowy:
    csv_output = csv.writer(plik_wynikowy)
    csv_output.writerow(wiersze)

print(wiersze)




