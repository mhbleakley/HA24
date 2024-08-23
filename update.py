import os
from dotenv import load_dotenv

load_dotenv()

from todoist import Todoist

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

mb_td = Todoist(mb_td_key)

# inbox_id = mb_td.get_project_by_name('Inbox')
# print(inbox_id)


# inbox_name = mb_td.get_project_by_id(inbox_id)
# print(inbox_name)

# in_td = Todoist(in_td_key)

# inbox_id = in_td.get_project_by_name('Inbox')
# print(inbox_id)


# inbox_name = in_td.get_project_by_id(inbox_id)
# print(inbox_name)

# in_inbox = in_td.get_inbox()
# for item in in_inbox:
#     print(item)

mb_inbox = mb_td.get_inbox()
for item in mb_inbox:
    print(item)