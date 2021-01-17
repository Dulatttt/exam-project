from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from exam.models import Exam

import random
import string



def ray_randomizer(breath=0, length=7):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))

def AddExamView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			title = request.POST.get("title")
			exam_type = request.POST.get("exam_type")
			batch = request.POST.get("batch")
			duration = request.POST.get("duration")

			exam_slug = ray_randomizer(4,10)

			exam = Exam.objects.create(title=title, exam_slug=exam_slug, exam_type=exam_type, batch=batch, duration=duration)
			exam.save()

			return HttpResponseRedirect(reverse("question:add_qa", args=(exam.id,)))
			
		else:
			context = {}
			return render(request, 'exam/add_exam.html', context)
		
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		





def AddNominationFormView(request, exam_id):
	pass


def AddTheoryiew(request, exam_id):
	pass



def ExamDetailView(request, id):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			exam = Exam.objects.get(id=id)

			context = {"exam": exam}
			return render(request, 'exam/exam_detail.html', context)
		

	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		



def EditExamView(request, id):
	if request.user.is_superuser == True:
		exam = Exam.objects.get(id=id)
		if request.method == "POST":
			title = request.POST.get("title")
			exam_type = request.POST.get("exam_type")
			batch = request.POST.get("batch")
			duration = request.POST.get("duration")

			if request.POST.get("status") == "on":
				status = True
			else:
				status = False

			exam.title = title
			exam.exam_type = exam_type
			exam.batch = batch
			exam.duration = duration

			exam.status = status

			exam.save()

			return HttpResponseRedirect(reverse("exam:all_exam"))
			
		else:
			

			context = {"exam": exam}
			return render(request, 'exam/edit_exam.html', context)


	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		




def AllExamView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			exams = Exam.objects.all()
			context = {"exams": exams}
			return render(request, 'exam/all_exam.html', context)
		

	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		

