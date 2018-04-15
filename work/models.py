from django.db import models

from datetime import datetime

class Todos(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_at = models.DateTimeField(default = datetime.now , blank = True)

	def __str__(self):
		return self.title
	class Meta:
		verbose_name_plural = "Todos"
		#we did this to change the plural form to Posts

# Create your models here.
