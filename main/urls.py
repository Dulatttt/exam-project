from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.LoginView, name="login"),
	path("sign-up/", views.SignUpView, name="sign_up"),

	path("e/<str:exam_slug>/<str:exam_link>/", views.ExamLoginView, name="exam_login"),
	path("e/<str:exam_link>/<int:student_id>/start/", views.TakeExamView, name="take_exam"),
	path("e/<str:exam_link>/<int:student_id>/<int:result_id>/nomination_form/", views.TakeExamNView, name="take_exam_n"),
	path("e/<str:exam_link>/<int:student_id>/<int:result_id>/theory/", views.TakeExamTView, name="take_exam_t"),
	path("e/<str:exam_link>/<int:student_id>/exam-complete/", views.ExamCompleteView, name="exam_complete"),
	path("e/<str:exam_link>/<int:student_id>/error/", views.ErrorView, name="error"),

	path("e/<str:exam_slug>/exam-complete/result-checker/", views.ResultCheckerView, name="result_checker"),
	path("e/<str:exam_slug>/<int:student_id>/exam_complete/result-checker/complete/", views.StudentResultView, name="student_result"),

	path("e/time-up-submit/<str:exam_link>/<int:student_id>/r/complete-time-up-submit/", views.TimeUpSubmitView, name="time_up_submit"),
	
	path("userlogout/", views.UserLogoutView, name="userlogout"),

]
