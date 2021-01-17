from django.urls import path
from . import views

app_name = "sadmin"

urlpatterns = [

	path("sadmin/", views.IndexView, name="sadmin"),

]
