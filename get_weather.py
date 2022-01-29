#!/usr/bin/env python3
import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://api.weatherstack.com/current?access_key=cce43aa3a3de500cc32c5df0e67c9408&query=Cairo"
html = urllib.request.urlopen(url, context=ctx).read()

try:
        data = json.loads(html)
except:
        data = None

weather = data['current']['weather_descriptions']
humidity = data['current']['humidity']
visibility = data['current']['visibility']
pressure = data['current']['pressure']
wind = data['current']['wind_speed']

file = open("weather.csv", 'w')
file.write("'weather', 'humidity', 'visibility', 'pressure', 'wind_speed'")
file.write('\n')

for i in range(10):
	row_string = "'{}', '{}', '{}', '{}', '{}'".format(weather[0], humidity,visibility,pressure,wind)
	file.write(row_string)
	file.write('\n')

file.close()
