from bs4 import BeautifulSoup
import urllib2
source_page = urllib2.urlopen('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies').read()
soup = BeautifulSoup(source_page, 'html.parser')
table = soup.find("table", { "class" : "wikitable sortable" })

# Fail now if we haven't found the right table
header = table.findAll('th')
if header[0].string != "Ticker symbol" or header[1].string != "Security":
    raise Exception("Can't parse wikipedia's table!")

# Retreive the values in the table
records = []
rows = table.findAll('tr')
for row in rows:
    fields = row.findAll('td')
    if fields:
        symbol = fields[0].string
        records.append(symbol)

f = open("tickers.txt",'w')
# Sorting ensure easy tracking of modifications
records.sort(key=lambda s: s.lower())
for t in records:
	f.write(t + "\n") 
