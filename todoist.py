import os
from time import sleep
import datetime
from todoist_api_python.api import TodoistAPI
from dotenv import load_dotenv

load_dotenv()

mb_td_key = os.environ.get('MB_TODOIST_KEY')
in_td_key = os.environ.get('IN_TODOIST_KEY')

class Todoist:
	def __init__(self, key):
		self.api = TodoistAPI(key)
		self.update()
	
	def update(self):
		try:
			print('updating from todoist')
			self.projects = self.api.get_projects()
			print('got projects')
			sleep(1)
			self.tasks = self.api.get_tasks()
			print(self.tasks)
			print('got tasks')
			sleep(1)
			self.labels = self.api.get_labels()
			print('got labels')
			sleep(1)
			self.sections = self.api.get_sections()
			print('got sections')
			print('todoist update complete')
		except Exception as e:
			print(e)

	def get_project_by_name(self, name):
		for project in self.projects:
			if project.name == name:
				return project.id

	def get_project_by_id(self, id):
		for project in self.projects:
			if project.id == id:
				return project.name

	def get_inbox(self):
		inbox_id = self.get_project_by_name("Inbox")
		tasks = []
		for task in self.tasks:
			if task.project_id == inbox_id:
				tasks.append(task.content)
		return tasks