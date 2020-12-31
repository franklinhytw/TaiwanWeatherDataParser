import requests
from datetime import datetime

AUTH_TOKEN = "CWB"

if __name__ == '__main__':
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%dT%H:%M:%S")
    
    # try less 10 times
    for x in range(10):
        d = requests.get("https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-069?Authorization=" + AUTH_TOKEN + "&"
                         "format=JSON&elementName=WeatherDescription&sort=time&timeFrom=" + dt_string)
        if d.status_code == 200:
            data = d.json()
            try:
                local = data['records']['locations'][0]['location']
                for l in local:
                    if l['locationName'] == "永和區":
                        y_time = l['weatherElement'][0]['time'][0]
                        desc = y_time['elementValue'][0]['value']
                        print(desc)
                        break #break for loop
            except Exception as e:
                continue
            break #break for loop
