from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate

from .forms import UserForm

from student.models import Student
from exam.models import Exam, ExamStudentConnector
from nomination_form.models import NominationForm
from theory.models import Theory
from result.models import Result
from radmin.models import RAdmin

# Create your views here.

def SignUpView(request):
	if request.method == "POST":
		form = UserForm(request.POST or None, request.FILES or None)
		
		if request.POST.get("password2") != request.POST.get("password1"):
			return HttpResponse("Error!  -Please make sure both passwords are similar")
			
		else:
			user = form.save()
			user.set_password(request.POST.get("password1"))
			user.save()

			login(request, user)

			status = "not-verified"
			radmin = RAdmin.objects.create(user=user, name=user.username, status=status)
			radmin.save()

			return HttpResponseRedirect(reverse("main:login"))
	
	else:
		form2 = UserForm()
		return render(request, "main/sign_up.html", {"form2": form2})






def LoginView(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		status = request.POST.get("account_type")

		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse("radmin:radmin"))
			else:
				return HttpResponse("Incorrect Login!")

		else:
			return HttpResponse("Incorrect Login!")
	else:
		context = {}
		return render(request, "main/login.html", context)



def ExamLoginView(request, exam_slug, exam_link):
	exam = Exam.objects.get(id=exam_link)
	if exam.status == True:
		if request.method == "POST":
			reg_no = request.POST.get("reg_no")

			user = authenticate(username=reg_no, password=reg_no)

			try:
				student = Student.objects.get(user__pk=user.id, reg_no=reg_no)
			except:
				student = None

			if user and student:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect(reverse("main:take_exam", args=(exam_link, student.id,)))
				else:
					return HttpResponse("Incorrect Login!")

			else:
				return HttpResponse("Incorrect Login!")



		else:
			context = {}
			return render(request, "main/exam_login.html", context)

	else:
		return HttpResponse("Sorry, This Exam, either hasn't started or it's over! Contact your institution.")



def TakeExamView(request, exam_link, student_id):
	status = "off" #status check if student already wrote the exam
	exam = Exam.objects.get(id=exam_link)
	exam_title = exam.title
	exam_type = exam.exam_type
	exam_slug = exam.exam_slug
	student = Student.objects.get(id=student_id)

	#for time up shit
	time_exam_link = exam.id
	time_student_id = student.id
	#time_result_id = 9999999999999999999999999999999999

	for item in exam.students.all():
		if item.id == student_id:
			status = "on"


	if status == "off":
		questions = exam.questions.all()
		counts = exam.questions.count()
		count_list = []


		for i in range(counts):
			count_list.append(i+1)

		exam_questions = zip(questions, count_list)

		if request.method == "POST":
			score = 0
			percentage = 0
			actual_score = 0
			real_score = 0

			answers = []
			answer_list = []
			for item, count in exam_questions:
				val = "selected_answer_" + str(count)
				if request.POST.get(val):
					answers.append(request.POST.get(val))
				else:
					answers.append("x_x")

			for item in answers:
				answer_list.append(item.split("_")[1])


			for item, item2 in zip(exam.questions.all(), answer_list):
				if item.real_answer == item2:
					actual_score += 1

			percentage = (actual_score/counts)*100

			#return HttpResponse(percentage)

			
			result = Result.objects.create(student=student, exam_id=exam_link, exam_title=exam_title, exam_type=exam_type, exam_slug=exam_slug,
			 answers=answer_list, score=actual_score, total=counts, percentage=percentage)
			result.save()

			return HttpResponseRedirect(reverse("main:take_exam_n", args=(exam_link, student.id, result.id,)))


		else:
			context = {"exam": exam, "exam_questions": exam_questions, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
			return render(request, "main/take_exam.html", context)

	else:
		return HttpResponse("Sorry, You have already written this Exam!")


def TakeExamNView(request, exam_link, student_id, result_id):
	exam = Exam.objects.get(id=exam_link)
	student = Student.objects.get(id=student_id)
	result = Result.objects.get(id=result_id)

	#for time up shit
	time_exam_link = exam.id
	time_student_id = student.id
	#time_result_id = result.id

	if request.method == "POST":
		

		name_1 = request.POST.get("name_1")
		name_2 = request.POST.get("name_2")
		name_3 = request.POST.get("name_3")

		phone_1 = request.POST.get("phone_1")
		phone_2 = request.POST.get("phone_2")
		phone_3 = request.POST.get("phone_3")

		qualification_1 = request.POST.get("qualification_1")
		qualification_2 = request.POST.get("qualification_2")
		qualification_3 = request.POST.get("qualification_3")

		residental_state_1 = request.POST.get("residental_state_1")
		residental_state_2 = request.POST.get("residental_state_2")
		residental_state_3 = request.POST.get("residental_state_3")

		nomination_form = NominationForm.objects.create(name_one=name_1, phone_one=phone_1, qualification_one=qualification_1, residental_state_one=residental_state_1,
			name_two=name_2, phone_two=phone_2, qualification_two=qualification_2, residental_state_two=residental_state_2,
			name_three=name_3, phone_three=phone_3, qualification_three=qualification_3, residental_state_three=residental_state_3
			)
		result.response_nomination_form_id = nomination_form.id
		result.save()
		

		return HttpResponseRedirect(reverse("main:take_exam_t", args=(exam_link, student.id, result.id)))


	else:
		

		context = {"exam": exam, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
		return render(request, "main/take_exam_n.html", context)




def TakeExamTView(request, exam_link, student_id, result_id):
	exam = Exam.objects.get(id=exam_link)
	student = Student.objects.get(id=student_id)
	result = Result.objects.get(id=result_id)

	theorys = exam.theorys.all()
	counts = exam.theorys.count()
	count_list = []

	for i in range(counts):
		count_list.append(i+1)

	exam_theorys = zip(theorys, count_list)


	#for time up shit
	time_exam_link = exam.id
	time_student_id = student.id
	#time_result_id = result.id


	if request.method == "POST":

		response_theory = ""
		for item, count in exam_theorys:
			val = "answer_" + str(count)
			response_theory = response_theory + ("Q%s: %s(Answer: %s) | " % (count, item.title, request.POST.get(val)))

		result.response_theory = response_theory
		result.save()

		exam_student = ExamStudentConnector(exam=exam, student=student)
		exam_student.save()

		logout(request)
		return HttpResponseRedirect(reverse("main:exam_complete", args=(exam_link, student.id,)))


	else:

		context = {"exam": exam, "exam_theorys": exam_theorys, "time_exam_link": time_exam_link, "time_student_id": time_student_id}#, "time_result_id": time_result_id}
		return render(request, "main/take_exam_t.html", context)






def TimeUpSubmitView(request, exam_link, student_id):
	#request.method == "POST"
	#TakeExamView(request=request, exam_link=exam_link, student_id=student_id)

	try:
		status = "off" #status check if student already wrote the exam
		exam = Exam.objects.get(id=exam_link)
		exam_title = exam.title
		exam_type = exam.exam_type
		exam_slug = exam.exam_slug
		student = Student.objects.get(id=student_id)


		for item in exam.students.all():
			if item.id == student_id:
				status = "on"


		if status == "off":
			questions = exam.questions.all()
			counts = exam.questions.count()
			count_list = []


			for i in range(counts):
				count_list.append(i+1)

			exam_questions = zip(questions, count_list)

			score = 0
			percentage = 0
			actual_score = 0
			real_score = 0

			answers = []
			answer_list = []
			for item, count in exam_questions:
				val = "selected_answer_" + str(count)
				if request.POST.get(val):
					answers.append(request.POST.get(val))
				else:
					answers.append("x_x")

			for item in answers:
				answer_list.append(item.split("_")[1])


			for item, item2 in zip(exam.questions.all(), answer_list):
				if item.real_answer == item2:
					actual_score += 1

			percentage = (actual_score/counts)*100

			#return HttpResponse(percentage)

			
			result = Result.objects.create(student=student, exam_id=exam_link, exam_title=exam_title, exam_type=exam_type, exam_slug=exam_slug,
			 answers=answer_list, score=actual_score, total=counts, percentage=percentage)
			result.save()

		else:
			return HttpResponse("Sorry, You have already written this Exam!")


	except:
		pass


	try:
		exam = Exam.objects.get(id=exam_link)
		student = Student.objects.get(id=student_id)
		result = Result.objects.get(id=result_id)

		#for time up shit
		time_exam_link = exam.id
		time_student_id = student.id
		time_result_id = result.id

			

		name_1 = request.POST.get("name_1")
		name_2 = request.POST.get("name_2")
		name_3 = request.POST.get("name_3")

		phone_1 = request.POST.get("phone_1")
		phone_2 = request.POST.get("phone_2")
		phone_3 = request.POST.get("phone_3")

		qualification_1 = request.POST.get("qualification_1")
		qualification_2 = request.POST.get("qualification_2")
		qualification_3 = request.POST.get("qualification_3")

		residental_state_1 = request.POST.get("residental_state_1")
		residental_state_2 = request.POST.get("residental_state_2")
		residental_state_3 = request.POST.get("residental_state_3")

		nomination_form = NominationForm.objects.create(name_one=name_1, phone_one=phone_1, qualification_one=qualification_1, residental_state_one=residental_state_1,
			name_two=name_2, phone_two=phone_2, qualification_two=qualification_2, residental_state_two=residental_state_2,
			name_three=name_3, phone_three=phone_3, qualification_three=qualification_3, residental_state_three=residental_state_3
			)
		result.response_nomination_form_id = nomination_form.id
		result.save()

	except:
		pass



	try:
		exam = Exam.objects.get(id=exam_link)
		student = Student.objects.get(id=student_id)
		result = Result.objects.get(id=result_id)

		theorys = exam.theorys.all()
		counts = exam.theorys.count()
		count_list = []

		for i in range(counts):
			count_list.append(i+1)

		exam_theorys = zip(theorys, count_list)


		#for time up shit
		time_exam_link = exam.id
		time_student_id = student.id
		time_result_id = result.id


		response_theory = ""
		for item, count in exam_theorys:
			val = "answer_" + str(count)
			response_theory = response_theory + ("Q%s: %s(Answer: %s) | " % (count, item.title, request.POST.get(val)))

		result.response_theory = response_theory
		result.save()

		exam_student = ExamStudentConnector(exam=exam, student=student)
		exam_student.save()

		logout(request)
		return HttpResponseRedirect(reverse("main:exam_complete", args=(exam_link, student.id,)))

			
	except:
		logout(request)
		return HttpResponseRedirect(reverse("main:exam_complete", args=(exam_link, student.id,)))



def ExamCompleteView(request, exam_link, student_id):
	if request.method == "POST":
		pass


	else:
		exam = Exam.objects.get(id=exam_link)

		context = {"exam": exam}
		return render(request, "main/exam_complete.html", context)



def ResultCheckerView(request, exam_slug):
	if request.method == "POST":
		reg_no = request.POST.get("reg_no")

		user = authenticate(username=reg_no, password=reg_no)

		try:
			student = Student.objects.get(user__pk=user.id, reg_no=reg_no)
		except:
			student = None

		if user and student:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse("main:student_result", args=(exam_slug, student.id,)))
			else:
				return HttpResponse("Incorrect Login!")

		else:
			return HttpResponse("Incorrect Login!")



	else:
		context = {}
		return render(request, "main/result_checker.html", context)





def StudentResultView(request, exam_slug, student_id):
	if request.method == "POST":
		pass


	else:
		try:
			result = Result.objects.get(exam_slug=exam_slug, student__pk=student_id)

			exam = Exam.objects.get(exam_slug=result.exam_slug)

			context = {"result": result, "exam": exam}
			return render(request, "main/student_result.html", context)


		except:
			return HttpResponse("No Result for this Exam, contact your institution!")







def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("main:login"))




#try:
#	pass
#except Exception as e:
#	raise
#else:
#	pass
#finally:
#	pass