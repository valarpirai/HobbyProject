from django.db import models

# Create your models here.

class Query(models.Model):
	"""docstring for Query"""
	request = models.CharField(max_length=200)
	response = models.CharField(max_length=200)

	created = models.DateTimeField('created date')
		