from django.urls import path
from . import views

app_name = "exam"

urlpatterns = [

    path('add-exam/', views.AddExamView, name='add_exam'),
    path('exam-detail/<int:id>/', views.ExamDetailView, name='exam_detail'),
    path('edit-exam/<int:id>/', views.EditExamView, name='edit_exam'),
    path('all-exam/', views.AllExamView, name='all_exam'),

]
