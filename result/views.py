from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from nomination_form.models import NominationForm
from result.models import  Result
from exam.models import Exam
from student.models import Student

def AddResultView(request):
	if request.method == "POST":
		pass
		
	else:
		context = {}
		return render(request, 'result/add_result.html', context)
		


def AllResultView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass


		else:
			exams = Exam.objects.all()
			exam_type_list = set()

			for item in exams:
				exam_type_list.add(item.exam_slug)


			#
			grouped_results = []
			for item in exam_type_list:
				results = Result.objects.filter(exam_slug=item)
				if results:
					grouped_results.append(results)
								

			#return HttpResponse(str(grouped_results))
			context = {"results": grouped_results}
			return render(request, 'result/all_result.html', context)


			
	else:
		return HttpResponse("Не авторизованы!, Свяжитесь с номером 87074440969")		



def ResultDetailView(request, result_id, student_id):
	if request.user.is_superuser == True:
		if request.method == "POST":
			student = Student.objects.get(id=student_id)
			result = Result.objects.get(id=result_id)

			total_nomination_score = request.POST.get("total_nomination_score")
			given_nomination_score = request.POST.get("given_nomination_score")

			result.score += int(given_nomination_score)
			result.total += int(total_nomination_score)

			result.percentage = (result.score/result.total)*100
			
			result.save()


			return HttpResponseRedirect(reverse("result:all_result"))

			
		else:
			result = Result.objects.get(id=result_id)
			response_nf = NominationForm.objects.get(id=result.response_nomination_form_id)

			context = {"result": result, "response_nf":response_nf}
			return render(request, 'result/result_detail.html', context)
		
	else:
		return HttpResponse("Не авторизованы!, Свяжитесь с номером 87074440969")		



def EditResultView(request, result_id, student_id):
	student = Student.objects.get(id=student_id)
	result = Result.objects.get(id=result_id)
	if request.method == "POST":
		score = request.POST.get("score")
		total = request.POST.get("total")

		result.score = int(score)
		result.total = int(total)
		result.percentage = (int(score)/int(total))*100
			
		result.save()


		return HttpResponseRedirect(reverse("result:all_result"))


		
	else:
		result = Result.objects.get(id=result_id)
		context = {"result": result}
		return render(request, 'result/edit_result.html', context)
