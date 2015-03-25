from tornado import web
from tornado.escape import json_encode
import json
from bson import json_util
from bson.objectid import ObjectId
from etc.config import db

class IndexHandler(web.RequestHandler):
	def get(self):
		self.render("index.html")

class StoriesHandler(web.RequestHandler):
	def get(self):
		stories = db.stories.find()
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps(list(stories),default=json_util.default))
		

	def post(self):
		story_data = json.loads(self.request.body)
		story_id = db.stories.insert(story_data)
		print('story created with id ' + str(story_id))
		self.set_header("Content-Type", "application/json")
		self.set_status(201)
		

class StoryHandler(web.RequestHandler):
	def get(self , story_id):
		story = db.stories.find_one({"_id":ObjectId(str(story_id))})
		self.set_header("Content-Type", "application/json")
		self.write(json.dumps((story),default=json_util.default))
