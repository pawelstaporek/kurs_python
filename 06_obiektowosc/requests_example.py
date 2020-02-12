import requests

resp = requests.get("https://www.metaweather.com/api/location/search/?query=warsaw")
print(resp.status_code)
print(resp.content)
print(resp.json()[0]['woeid'])

id_ = resp.json()[0]['woeid']
resp1 = requests.get(f"https://www.metaweather.com/api/location/{id_}/")
print(resp1.status_code)
temp = resp1.json()['consolidated_weather'][0]['the_temp']
p = resp1.json()['consolidated_weather'][0]['air_pressure']
rh = resp1.json()['consolidated_weather'][0]['humidity']
print(f"""
temperatura {temp} C 
cisnienie {p} hPa 
wilgotność {rh}%
""")
