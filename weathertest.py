import os
from pyowm import OWM

weather_api=os.getenv("WEATHERAPI")
#print(weather_api)

owm = OWM(weather_api)
mgr = owm.weather_manager()
weather = mgr.weather_at_place('Grand Rapids, US').weather
temp_dict_kelvin = weather.temperature()   # a dict in Kelvin units (default when no temperature units provided)
d = weather.temperature('fahrenheit')

#print(d)
c = d.get('temp')
h = d.get('temp_max')
lo = d.get('temp_min')
f = d.get('feels_like')

currenttemp = str(c)
high = str(h)
low = str(lo)
feels = str(f)
#print(currenttemp)

print('Good morning, the current temperature is '+currenttemp+ ' with a high of '+high+ ' and a low of '+low)
