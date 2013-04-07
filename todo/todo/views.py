from resource import Resource
import models 
from django.core import serializers
from django.http import HttpResponse


class Tasks(Resource):
	def do_GET(self):
		tasks = models.Task.objects.all()
		return HttpResponse(serializers.serialize('json', tasks))

class Task(Resource):
	def do_GET(self):
		pass