# import libraries to get data in json format
import numpy as np
import requests
import json
from matplotlib import pyplot as plt

# fetch covid data with REST API request
covid_data = requests.get('https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json')
js = json.loads(covid_data.content)


# create lists of data to plot
x=[]
y=[]

for i in range(len(js)):
    x.append(js[i]["data"])
    y.append(js[i]["nuovi_positivi"])
    
    
# plot data
plt.plot(x,y)
plt.xlabel('Data')
plt.ylabel('Nuovi Positivi')
plt.xticks(np.arange(0, len(x), step=8), rotation=90)
plt.title("Covid-19 Italy")
