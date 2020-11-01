
from django.contrib import admin
# import Projects model in order to register it
from projects.models import Project

# Register your models here.
# pass in the name of the imported model ("Project")
admin.site.register(Project)