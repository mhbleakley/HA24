import os
from dotenv import load_dotenv
from time import sleep
from weather import get_weather
from timer import Timer

load_dotenv()

from todoist import Todoist

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

mb_td = Todoist(mb_td_key, 'martin')
in_td = Todoist(in_td_key, 'izzy')

td_timer = Timer(60)
td_timer.start()
weather_timer = Timer(60)
weather_timer.start()

while True:
    if td_timer.is_expired():
        print('timer expired')
        sleep(2)
        mb_td.update()
        mb_td.get_currently_due()

        in_td.update()
        in_td.get_section_tasks('GROCERY LIST')
        in_td.get_currently_due()

        td_timer.start()
