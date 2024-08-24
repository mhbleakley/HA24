import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()

from todoist import Todoist

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

mb_td = Todoist(mb_td_key, 'martin')
# in_td = Todoist(in_td_key, 'izzy')

mb_td.get_currently_due()