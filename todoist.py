import os
from time import sleep
from datetime import datetime, timedelta
from todoist_api_python.api import TodoistAPI

class Todoist:
	def __init__(self, key, name, destination_folder):
		self.api = TodoistAPI(key)
		self.name = name
		self.destination_folder = destination_folder
		self.update()
	
	def update(self):
		try:
			print(f'updating from {self.name}\'s todoist')
			self.projects = self.api.get_projects()
			print('got projects...', end=' ')
			sleep(1)
			self.tasks = self.api.get_tasks()
			print('got tasks...', end=' ')
			sleep(1)
			self.labels = self.api.get_labels()
			print('got labels...', end=' ')
			sleep(1)
			self.sections = self.api.get_sections()
			print('got sections...')
			print(f'completed {self.name}\'s todoist update.\n')
		except Exception as e:
			print(e)

	def get_project_by_name(self, p_name):
		for project in self.projects:
			if project.name == p_name:
				return project.id
		return None

	def get_project_by_id(self, id):
		for project in self.projects:
			if project.id == id:
				return project.name
		return None

	def get_section_by_name(self, s_name):
		for section in self.sections:
			if section.name == s_name:
				return section.id
		return None

	def get_currently_due(self):
		tasks = [] # collect tasks that are due 'today' and put their content here
		today = datetime.today().strftime('%Y-%m-%d')
		for task in self.tasks:
			if task.due != None:
				if task.due.date <= today:
					tasks.append(task.content)

		self.write_task_list(self.name + '_currently_due.txt', tasks)

		return tasks

	def get_section_tasks(self, s_name):
		s_id = self.get_section_by_name(s_name)
		tasks = []
		for task in self.tasks:
			if task.section_id == s_id:
				tasks.append(task.content)

		sanitized_s_name = s_name.replace(' ', '_')

		self.write_task_list(self.name + '_' + sanitized_s_name + '_section.txt', tasks)

		return tasks

	def write_task_list(self, f_name, tasks):
		tl_dest = self.destination_folder + '/data/'
		if not os.path.exists(tl_dest):
			os.mkdir(tl_dest)
			print(f'making directory {tl_dest}')
		else:
			print(f'directory {tl_dest} already exists')

		html_tasks = self.list_to_html(tasks)

		with open(tl_dest + f_name, 'w') as f:
			f.writelines(task + '\n' for task in html_tasks)
			f.close()

	def list_to_html(self, lst):
		new = ['<ul class=\'bullet_list\'>']
		for item in lst:
			new.append('<li class=\'bullet\'>' + item + '</li>')
		new.append('</ul>')
		return new