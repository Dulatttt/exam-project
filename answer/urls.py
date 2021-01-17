from django.urls import path
from . import views

app_name = "answer"

urlpatterns = [

    path('add-answer/', views.AddAnswerView, name='add_answer'),

]
