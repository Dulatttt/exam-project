from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from exam.models import Exam,ExamQuestionConnector
from question.models import Question


# Create your views here.

def AddQuestionAnswerView(request, exam_id):
	if request.user.is_superuser == True:
		if request.method == "POST":

			exam = Exam.objects.get(id=exam_id)


			q1 = request.POST.get("q1")
			if q1 != "":
				q1_a = request.POST.get("q1_a")
				q1_b = request.POST.get("q1_b")
				q1_c = request.POST.get("q1_c")
				q1_d = request.POST.get("q1_d")
				real_answer_1 = request.POST.get("real_answer_1")

				question1 = Question.objects.create(title=q1, answer_a=q1_a, answer_b=q1_b, answer_c=q1_c, answer_d=q1_d, real_answer=real_answer_1)
				question1.save()

				exam_question = ExamQuestionConnector(exam=exam, question=question1)
				exam_question.save()





			q2 = request.POST.get("q2")
			if q2 != "":
				q2_a = request.POST.get("q2_a")
				q2_b = request.POST.get("q2_b")
				q2_c = request.POST.get("q2_c")
				q2_d = request.POST.get("q2_d")
				real_answer_2 = request.POST.get("real_answer_2")

				question2 = Question.objects.create(title=q2, answer_a=q2_a, answer_b=q2_b, answer_c=q2_c, answer_d=q2_d, real_answer=real_answer_2)
				question2.save()

				exam_question = ExamQuestionConnector(exam=exam, question=question2)
				exam_question.save()






			q3 = request.POST.get("q3")
			if q3 != "":
				q3_a = request.POST.get("q3_a")
				q3_b = request.POST.get("q3_b")
				q3_c = request.POST.get("q3_c")
				q3_d = request.POST.get("q3_d")
				real_answer_3 = request.POST.get("real_answer_3")

				question3 = Question.objects.create(title=q3, answer_a=q3_a, answer_b=q3_b, answer_c=q3_c, answer_d=q3_d, real_answer=real_answer_3)
				question3.save()

				exam_question = ExamQuestionConnector(exam=exam, question=question3)
				exam_question.save()





			q4 = request.POST.get("q4")
			if q4 != "":
				q4_a = request.POST.get("q4_a")
				q4_b = request.POST.get("q4_b")
				q4_c = request.POST.get("q4_c")
				q4_d = request.POST.get("q4_d")
				real_answer_4 = request.POST.get("real_answer_4")

				question4 = Question.objects.create(title=q4, answer_a=q4_a, answer_b=q4_b, answer_c=q4_c, answer_d=q4_d, real_answer=real_answer_4)
				question4.save()

				exam_question = ExamQuestionConnector(exam=exam, question=question4)
				exam_question.save()




			q5 = request.POST.get("q5")
			if q5 != "":
				q5_a = request.POST.get("q5_a")
				q5_b = request.POST.get("q5_b")
				q5_c = request.POST.get("q5_c")
				q5_d = request.POST.get("q5_d")
				real_answer_5 = request.POST.get("real_answer_5")

				question5 = Question.objects.create(title=q5, answer_a=q5_a, answer_b=q5_b, answer_c=q5_c, answer_d=q5_d, real_answer=real_answer_5)
				question5.save()

				exam_question = ExamQuestionConnector(exam=exam, question=question5)
				exam_question.save()


			

			



			return HttpResponseRedirect(reverse("theory:add_theory", args=(exam.id,)))
			
		else:
			context = {}
			return render(request, 'question/add_qa.html', context)




	else:
		return HttpResponse("Не авторизованы!, Свяжитесь с номером 87074440969")		

