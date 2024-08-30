import os
from dotenv import load_dotenv
from time import sleep
from backend.weather import get_weather
import threading
import sys

load_dotenv()

from backend.todoist import Todoist

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

mb_td = Todoist(mb_td_key, 'martin', './public')
in_td = Todoist(in_td_key, 'izzy', './public')

def todoist_update():
    mb_td.update()
    mb_td.get_currently_due()

    in_td.update()
    in_td.get_currently_due()
    in_td.get_section_tasks('GROCERY LIST')

td_timer = threading.Timer(60, todoist_update)
td_timer.start()

from backend.background_change import BackgroundManager

backgrounds_dir = './public/resources/backgrounds/'
bgm = BackgroundManager(backgrounds_dir)

def change_background():
    bgm.rotate()

bgm_timer = threading.Timer(3600, change_background)
bgm_timer.start()

from backend.spotify import Spotify

mb_spotify_id = os.environ.get('MB_SPOTIPY_CLIENT_ID')
mb_spotify_secret = os.environ.get('MB_SPOTIPY_CLIENT_SECRET')
mb_spotify = Spotify('martin', './public', mb_spotify_id, mb_spotify_secret)

def update_spotify():
    mb_spotify.get_playback()

spotify_timer = threading.Timer(1.0, update_spotify)

while True:
    try:
        sleep(1)
        if not td_timer.is_alive():
            td_timer = threading.Timer(td_timer.interval, td_timer.function)
            td_timer.start()

        if not bgm_timer.is_alive():
            bgm_timer = threading.Timer(bgm_timer.interval, bgm_timer.function)
            bgm_timer.start()

        if not spotify_timer.is_alive():
            spotify_timer = threading.Timer(spotify_timer.interval, spotify_timer.function)
            spotify_timer.start()

    except Exception as e:
        print(e)
        sys.exit()