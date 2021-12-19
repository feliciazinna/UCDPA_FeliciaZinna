# FELICIA UCDPA Project
# Import pandas as pd
import pandas as pd

# Import the data from CSV: VaccinationItaly
df = pd.read_csv("italian_vaccination.csv")
print(df.describe())
print(df.info)
print(type(df))

# understand data of CSV - dati puliti e completi devo tagliarne qualcuno - uso dei dizionari
VaccinationItaly = pd.read_csv("italian_vaccination.csv")
print(VaccinationItaly.head())
print((VaccinationItaly.shape))
print(VaccinationItaly.info())
print(VaccinationItaly.isnull())

# Importing flat files from the web - web scraping
import bs4, requests, webbrowser
from urllib.request import urlretrieve

# assign URL of the file: URL
url = "https://github.com/pcm-dpc/COVID-19/raw/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"
urlretrieve(url, 'dpc-covid19-ita-andamento-nazionale.csv')
df = pd.read_csv('dpc-covid19-ita-andamento-nazionale.csv', sep=',')
print(df.head())
response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# Import main library
import pandas as pd
# Just a workaround to globally set chart sizes
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [35, 15]

# Import data from official open data by Protezione Civile
data = pd.read_csv(
    "https://github.com/pcm-dpc/COVID-19/raw/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv",
    index_col = "data",
    parse_dates = True
)

# Data preview
data

# Line chart of `totale_positivi`
data.plot.line(y = "totale_positivi")

# Weekly moving average of `nuovi_positivi`
data["nuovi_positivi_avg"] = data["nuovi_positivi"].rolling(7).mean()

# Double lines chart of `totale_positivi` (daily and weekly)
data.plot.line(y = ["nuovi_positivi", "nuovi_positivi_avg"])

# Importing flat files from the web - web scraping
# import bs4, requests
# url = "https://www.worldometers.info/coronavirus/country/italy/"
# response = requests.get(url)
# response.raise_for_status()
# response.status_code
# html_page = bs4.BeautifulSoup(requests.text, 'html.parser')

# element_html = '.tab-pane active'
# sel_element = html_page.select(element_html)
# text_element = sel_element[0].getText()
# with open('text.txt', 'w') as texthmtl
# texthmtl.write(texthmtl)
# print('file updated')

# count missing values in columns: data clen
missing_values_count = VaccinationItaly.isnull().sum()
print(missing_values_count)
print(VaccinationItaly.isnull().sum())

cleaned_data = VaccinationItaly.dropna()
print(VaccinationItaly.shape, cleaned_data.shape)

cleaned_data = VaccinationItaly.dropna(axis=1)

cleaned_data = VaccinationItaly.fillna('*')
print(cleaned_data.isnull().sum())

cleaned_data = VaccinationItaly.fillna(method='bfill')
cleaned_data = VaccinationItaly.fillna(method='ffill').fillna(method='bfill')
