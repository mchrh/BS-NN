from bs4 import BeautifulSoupimport
import requests


def main():  print(“Hello World!”)if __name__ == “__main__”:  main()
data_url = “https://finance.yahoo.com/quote/SPY/options"data_html = requests.get(data_url).contentprint(data_html)


content = BeautifulSoup(data_html, “html.parser”)
options_tables = content.find_all(“table”)

options_tables = [] tables = content.find_all(“table”) for i in range(0, len(content.find_all(“table”))):   options_tables.append(tables[i])
print(options_tables)

expiration = datetime.datetime.fromtimestamp(int(datestamp)).strftime(“%Y-%m-%d”)
calls = options_tables[0].find_all(“tr”)[1:] # first row is header
itm_calls = []otm_calls = []

for call_option in calls:    if “in-the-money” in str(call_option):  itm_calls.append(call_option)  else:    otm_calls.append(call_option)
itm_call = itm_calls[-1]otm_call = otm_calls[0]
print(str(itm_call) + “ \n\n “ + str(otm_call))

itm_call_data = [] for td in BeautifulSoup(str(itm_call), “html.parser”).find_all(“td”):   itm_call_data.append(td.text)
