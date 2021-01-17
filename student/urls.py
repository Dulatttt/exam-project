from django.urls import path
from . import views

app_name = "student"

urlpatterns = [

    path('add-student/', views.AddStudentView, name='add_student'),
    path('student-detail/<int:id>/', views.StudentDetailView, name='student_detail'),
    path('edit-student/<int:id>/', views.EditStudentView, name='edit_student'),
    path('all-student/', views.AllStudentView, name='all_student'),

]
