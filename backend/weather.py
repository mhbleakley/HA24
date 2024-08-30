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
def get_weather():
    meteo = mgr.get_data(3, 1, './data/weather')
    