from django.http import HttpResponseNotAllowed, HttpResponseBadRequest
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response, render
from django.core import serializers
from django.forms.models import model_to_dict
import models
import json

import logging
logger = logging.getLogger('django')

class Resource:
	def __call__(self, request):
		self.request = request

		try:
			callback = getattr(self, "do_%s" % request.method)
		except AttributeError:
			allowed_methods = [ m.lstrip("do_") for m in dir(self) if m.startswith("do_") ]

			return HttpResponseNotAllowed(allowed_methods)


		return callback()

class Index(Resource):
	def do_GET(self):
		return render(self.request, 'home.html')

class Tasks(Resource):
	def do_GET(self):
		tasks = [model_to_dict(m) for m in models.Task.objects.all()]
		return HttpResponse(json.dumps(tasks), mimetype='application/json')

	def do_POST(self):
		data = json.loads(self.request.body)
		name = data.get('name', '')
		
		if name:
			task = models.Task(name=name)
			task.save()
			return HttpResponse(json.dumps(model_to_dict(task)), mimetype='application/json')
		else:
			return HttpResponseBadRequest("name of task should not be empty.")

class Task(Resource):
	def __call__(self, request, id):
		self.id = id
		return Resource.__call__(self, request)

	def do_GET(self):
		task = get_object_or_404(models.Task, id = self.id)
		json_data = serializers.serialize('json', [task])
		return HttpResponse(json_data, mimetype="application/json")

	def do_PUT(self):
		data = json.loads(self.request.body)
		task = get_object_or_404(models.Task, id = self.id)
		task.name = data.get('name', '')
		task.done = data.get('done', False)
		task.save()
		return HttpResponse(json.dumps(model_to_dict(task)), mimetype='application/json')

	def do_DELETE(self):
		task = get_object_or_404(models.Task, id = self.id)
		task.delete()
		return HttpResponse()
