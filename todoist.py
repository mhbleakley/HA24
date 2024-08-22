
import os
from time import sleep
import datetime
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv

load_dotenv()

# APIs ###########################################################################
td_api = TodoistAPI(os.environ.get(MB_TODOIST_KEY)) # get todoist API

print('here')
while True:

	print('lol')
	sleep(1)

izzy_td_api = TodoistAPI('a4080445392a6ed9007a9dd2f5f9d9db71fc1497')


# TODOIST ###########################################################

def todoist_loop():
	todoist_inbox = [] # clear out list
	izzy_inbox = []
	grocery_list = []
	try:
		projects = td_api.get_projects()
		z_projects = izzy_td_api.get_projects()
		z_sections = izzy_td_api.get_sections()
		
		inbox_id = None
		z_inbox_id = None
		grocery_list_id = None
		for project in projects:
			if project.name == 'Inbox':
				inbox_id = project.id
		for project in z_projects:
			if project.name == 'Inbox':
				z_inbox_id = project.id
		for section in z_sections:
			if section.name == 'GROCERY LIST':
				grocery_list_id = section.id

		tasks = td_api.get_tasks() # get all tasks
		z_tasks = izzy_td_api.get_tasks()
		for t in tasks:
			if t not in todoist_inbox and t.project_id == inbox_id:
				todoist_inbox.append(t)
		for t in z_tasks:
			if t not in izzy_inbox and t.project_id == z_inbox_id:
				izzy_inbox.append(t)
			if t not in grocery_list and t.section_id == grocery_list_id:
				grocery_list.append(t)

	except Exception as error:
		print(error)

	for i, task in enumerate(todoist_inbox):
		offset = 1
		task_id = 'task{}'.format(i)
		due_id = 'due{}'.format(i)
		content = ' - ' + task.content
		due_date = task.due.date
		try: # if label i already exists, change it
			app.setLabel(task_id, content)
		except: # elif label does not exist, create it
			app.addLabel(task_id, content, row=i + offset, column=0)
			app.setLabelAlign(task_id, 'left')

	for i, task in enumerate(izzy_inbox):
		offset = 1
		task_id = 'z_task{}'.format(i)
		due_id = 'z_due{}'.format(i)
		content = ' - ' + task.content
		# due_date = task.due.date
		try: # if label i already exists, change it
			app.setLabel(task_id, content)
		except: # elif label does not exist, create it
			app.addLabel(task_id, content, row=i + offset, column=1)
			app.setLabelAlign(task_id, 'left')

	for i, task in enumerate(grocery_list):
		offset = 1
		task_id = 'g_task{}'.format(i)
		due_id = 'g_due{}'.format(i)
		content = ' - ' + task.content
		# due_date = task.due.date
		try: # if label i already exists, change it
			app.setLabel(task_id, content)
		except: # elif label does not exist, create it
			app.addLabel(task_id, content, row=i + offset, column=2)
			app.setLabelAlign(task_id, 'left')

	# if there are any labels greater than i, destroy them
	old_tasks_exist = True
	count = 0
	while old_tasks_exist:
		try:
			app.removeLabel('task{}'.format(count + len(todoist_inbox)))
			count += 1
		except:
			old_tasks_exist = False

	z_old_tasks_exist = True
	count = 0
	while z_old_tasks_exist:
		try:
			app.removeLabel('z_task{}'.format(count + len(izzy_inbox)))
			count += 1
		except:
			z_old_tasks_exist = False

	g_old_tasks_exist = True
	count = 0
	while g_old_tasks_exist:
		try:
			app.removeLabel('g_task{}'.format(count + len(grocery_list)))
			count += 1
		except:
			g_old_tasks_exist = False

# CLOCK ###########################################################################
def clock_loop():
	t = datetime.datetime.now().strftime('%m/%d %H:%M')
	app.setLabel('time', t + '  ')

# MAIN LOOP #######################################################################
def main_loop():
	clock_loop()
	todoist_loop()
	
app.registerEvent(main_loop)
app.setPollTime(30000) # in ms
app.go()
