from django.shortcuts import render
from django.http import HttpResponse
# import Project from projects/models file
from projects.models import Project

# Create your views here.
# always pass in the REQUEST, a Django object


def project_list(request):
    """# return an HTTP response object that returns HTML
    return HttpResponse("<h1>Hello, world!</h1")
    """
    # create an HTML template with the RENDER function
    # request + template name
    return render(request, 'projects/index.html')

# create all_projects View 
# (in projects/urls.py, path is: " ", view name is "views.all_projects")
def all_projects(request):
    # query the db and return all project objects with Project.objects.all() and save to the "projects" variable
    projects = Project.objects.all()
    # access the projects returned from the db by passing in a dictionary as a third param to render

    # in the render() method, return the request and the project name "all_projects.html"
    return render(request, 'projects/all_projects.html', {'projects': projects})
    # render takes the request and the name of the template to render (all_projects.html)
    # and passes the project objects (projects) that were retrieved froom the db
    # and forwards them all to the template (the template will render these objects)

# create a second view function for the project_detail URL
# it will also take "pk" as a second arg
def project_detail(request, pk):
    # query db for one project and pass in the pk argument
    project = Project.objects.get(pk=pk)
                            # re-direct forward to the template (projects/detail.html)
    return render(request, 'projects/detail.html',
    # pass the context dictionary in and forward on the project pulled from the db
        {'project': project})
