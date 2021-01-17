from django.urls import path
from . import views

app_name = "result"

urlpatterns = [

    path('add-result/', views.AddResultView, name='add_result'),
    path('result-detail/<int:result_id>/<int:student_id>/', views.ResultDetailView, name='result_detail'),
    path('edit-result/<int:result_id>/<int:student_id>/', views.EditResultView, name='edit_result'),
    path('all-result/', views.AllResultView, name='all_result'),

]
