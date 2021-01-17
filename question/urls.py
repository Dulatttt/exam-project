from django.urls import path
from . import views

app_name = "question"

urlpatterns = [

    path('add-question-answer/<int:exam_id>/', views.AddQuestionAnswerView, name='add_qa')

]
