# import django models in order to inherit from the model class
from django.db import models

# Create your models here.
# we want to model projects
# render a Model class called "Project" (Django automatically creates id in table)
class Project(models.Model):
    # define table rows and what type of data is permitted
    title = models.CharField(max_length=100)
    # use TextField() to allow more text
    description = models.TextField()
    # limit character field size
    technology = models.CharField(max_length=20)
    # FilePathField() is a string with certain restrictions --used for a user selecting from a list of files in a form field 
    # use Charfield() instead
    image = models.CharField(max_length=100) 
    # path is /projects/img b/c of double folder structure
