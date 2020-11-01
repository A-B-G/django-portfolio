from django.urls import path, include
from projects import views
""" note: can also write from . import views to indicate you're importing from the current project"""


# define app_name variable, which will be used in the URL string
app_name = "projects" 
# create a urlpattern variable and add a path that directs to Views (must import views)
urlpatterns = [
    # point to logic in Views--uniquely ID Views pointing to with "name" key arg
    # the ' ' path points to the all_projects View
    path('', views.all_projects, name="all_projects"),
    # add second path that captures URL with < > (int is a path converter that checks for an integer; <> captures parts of the URL and passes it forward into the app)
    # add "name=project_detail" third keyword argument to path
    path('<int:pk>', views.project_detail, name="project_detail"),
]
