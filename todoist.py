import os
from time import sleep
from datetime import datetime, timedelta
from todoist_api_python.api import TodoistAPI

class Todoist:
	def __init__(self, key, name):
		self.api = TodoistAPI(key)
		self.name = name
		self.update()
	
	def update(self):
		try:
			print('updating from todoist')
			# self.projects = self.api.get_projects()
			# print('got projects')
			# sleep(1)
			self.tasks = self.api.get_tasks()
			print('got tasks')
			# sleep(1)
			# self.labels = self.api.get_labels()
			# print('got labels')
			# sleep(1)
			# self.sections = self.api.get_sections()
			# print('got sections')
			print('todoist update complete')
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

	def get_currently_due(self):
		tasks = [] # collect tasks that are due 'today' and put their content here
		today = datetime.today().strftime('%Y-%m-%d')
		for task in self.tasks:
			if task.due != None:
				if task.due.date <= today:
					tasks.append(task.content)

		self.write_task_list(self.name + '_currently_due.txt', tasks)

		return tasks

	def write_task_list(self, f_name, tasks):
		if not os.path.exists('./data/'):
			os.mkdir('./data')

		html_tasks = self.list_to_html(tasks)
		
		f = open('./data/' + f_name, 'w')
		f.writelines(task + '\n' for task in html_tasks)
		f.close()

	def list_to_html(self, lst):
		new = ['<ul class=\'bullet_list\'>']
		for item in lst:
			new.append('<li class=\'bullet\'>' + item + '</li>')
		new.append('</ul>')
		return new