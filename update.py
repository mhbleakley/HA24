import os
from dotenv import load_dotenv
from time import sleep
from weather import get_weather
import threading

load_dotenv()

from todoist import Todoist

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

mb_td = Todoist(mb_td_key, 'martin', './public')
in_td = Todoist(in_td_key, 'izzy', './public')

def todoist_update():
    mb_td.update()
    mb_td.get_currently_due()

    in_td.update()
    in_td.get_currently_due()
    in_td.get_section_by_name('GROCERY LIST')

td_timer = threading.Timer(5, todoist_update)
td_timer.start()

while True:
    sleep(1)
    if not td_timer.is_alive():
        td_timer = threading.Timer(td_timer.interval, td_timer.function)
        td_timer.start()