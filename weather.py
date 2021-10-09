import csv
import requests
from datetime import date
import datetime
d0 = date(2013, 1, 1)

file=csv.writer(open('2021-9.csv','a'))
file.writerow(["date","sunrise","sunset","moonrise","moonset","moon_phase","moon_illumination","maxtempC","maxtempF","mintempC","mintempF","avgtempC","avgtempF",
            "totalSnow_cm","sunHour","uvIndex"])
for i in range(1,400):
    api_url = "http://api.worldweatheronline.com/premium/v1/past-weather.ashx?key=89ee2286c25c45a6bc7233339210810&q=Chicago&format=json"+"&date="+str(d0)+"&enddate=2021-10-01"
    d0 = d0 + datetime.timedelta(days=35)
    response = requests.get(api_url)
    data = response.json()
    for value in data["data"]["weather"]:
        file.writerow([value["date"], value["astronomy"][0]["sunrise"], value["astronomy"][0]["sunset"],
                       value["astronomy"][0]["moonrise"], value["astronomy"][0]["moonset"],
                       value["astronomy"][0]["moon_phase"], value["astronomy"][0]["moon_illumination"],
                       value["maxtempC"], value["maxtempF"], value["mintempC"], value["mintempF"],
                       value["avgtempC"], value["avgtempF"], value["totalSnow_cm"], value["sunHour"], value["uvIndex"]])







