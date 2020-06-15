# import libraries to get data in json format
import requests
import json


covid_data = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json')
js = json.loads(covid_data.content) 

# create arrays of data to plot
for i in range(len(js)):
    print("Data: ",  "Nuovi Positivi: ")
    print(js[i]["data"], js[i]["nuovi_positivi"])
