from django.db import models
import datetime

# Create your models here.
class Speaker(models.Model):
	name = models.CharField(max_length = 50)
	ministry_or_church = models.CharField(max_length = 50)

	def __str__(self):
		return self.name

class Serie(models.Model):
	theme = models.CharField(max_length = 100)
	program = models.CharField(max_length = 100)
	date_held = models.DateField(default = datetime.datetime.now)

	def __str__(self):
		return self.theme

class my_upload(models.Model):
	file_description = models.CharField(max_length = 300)
	file_link = models.CharField(max_length = 500)
	date_of_file_upload = models.DateTimeField(auto_now_add = True)
	file_title = models.CharField(max_length = 40)
	speaker = models.ForeignKey(Speaker, models.SET_NULL, blank = True, null = True, related_name = "uploads")
	series = models.ForeignKey(Serie, models.SET_NULL, blank = True, null = True, related_name = "s_uploads")

	def __str__(self):
		return self.file_title
		
		

