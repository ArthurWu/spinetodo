from django.db import models

class Task(models.Model):
	name = models.CharField(max_length = 100)
	done = models.BooleanField(default = False)