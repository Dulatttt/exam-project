from django.urls import path
from . import views

app_name = "radmin"

urlpatterns = [

	path("radmin/", views.IndexView, name="radmin"),
	#path("radmin/", views.IndexView, name="radmin"),

]
