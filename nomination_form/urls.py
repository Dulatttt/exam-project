from django.urls import path
from . import views

app_name = "nomination_form"

urlpatterns = [

    path('add-nomination-form/<int:exam_id>/', views.AddNominationFormView, name='add_nomination_form'),
    path('all-nomination-form/', views.AllNominationFormView, name='all_nomination_form'),

]
