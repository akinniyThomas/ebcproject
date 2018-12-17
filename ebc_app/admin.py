from django.contrib import admin
from .models import *

# Register your models here.
class upload_admin(admin.TabularInline):
	model = my_upload
	extra = 1
	fields = ["file_title", "file_description", "file_link", "series"]


class speaker_admin(admin.ModelAdmin):
	list_display = ("name", "ministry_or_church")
	inlines = [upload_admin]
	list_filter = ["name", "ministry_or_church"]
	search_fields = ["name", "ministry_or_church"]


class serie_admin(admin.ModelAdmin):
	list_display = ("theme", "program", "date_held")
	list_filter = ["theme", "program", "date_held"]
	search_fields = ["theme", "program", "date_held"]

admin.site.register(Serie, serie_admin)
admin.site.register(Speaker, speaker_admin)