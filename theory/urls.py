from django.urls import path
from . import views

app_name = "theory"

urlpatterns = [

    path('add-theory/<int:exam_id>/', views.AddTheoryView, name='add_theory'),
    path('all-theory/', views.AllTheoryView, name='all_theory'),

]
