from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from exam.models import Exam, ExamTheoryConnector
from theory.models  import Theory


def AddTheoryView(request, exam_id):
	if request.user.is_superuser == True:
		if request.method == "POST":
			exam = Exam.objects.get(id=exam_id)

			title_1 = request.POST.get("title_1")
			if title_1 != "":
				theory1 = Theory.objects.create(title=title_1)
				theory1.save()
				exam_theory = ExamTheoryConnector(exam=exam, theory=theory1)
				exam_theory.save()


			title_2 = request.POST.get("title_2")
			if title_2 != "":
				theory2 = Theory.objects.create(title=title_2)
				theory2.save()
				exam_theory = ExamTheoryConnector(exam=exam, theory=theory2)
				exam_theory.save()


			title_3 = request.POST.get("title_3")
			if title_3 != "":
				theory3 = Theory.objects.create(title=title_3)
				theory3.save()
				exam_theory = ExamTheoryConnector(exam=exam, theory=theory3)
				exam_theory.save()

			return HttpResponseRedirect(reverse("exam:all_exam"))
			
		else:
			context = {}
			return render(request, 'theory/add_theory.html', context)
		
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		


def AllTheoryView(request):
	if request.user.is_superuser == True:
	
		if request.method == "POST":
			pass
			
		else:
			context = {}
			return render(request, 'theory/all_theory.html', context)
		
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		
