from openmeteo_py import Hourly, Daily, Options, OWmanager
import json

# Latitude, Longitude for Boston, MA
latitude = 42.3601
longitude = -71.0589

hourly = Hourly()
daily = Daily()
options = Options(latitude,longitude)

mgr = OWmanager(options,
    hourly.all(),
    daily.all())

# Download data
meteo = mgr.get_data(3, 1, './data/weather')

# f = open('weather.json', 'r')
# data = json.load(f)

# units = []
# for i in data['hourly_units']:
#     units.append(i)

# print(units)

# for i, time in enumerate(data['hourly']['time']):
    