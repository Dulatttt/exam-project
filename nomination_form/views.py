from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from exam.models import Exam, ExamNominationFormConnector
from nomination_form.models  import NominationForm


def AddNominationFormView(request, exam_id):
	if request.method == "POST":
		exam = Exam.objects.get(id=exam_id)

		name_1 = request.POST.get("name_1")
		phone_1 = request.POST.get("phone_1")
		qualification_1 = request.POST.get("qualification_1")
		residental_state_1 = request.POST.get("residental_state_1")

		name_2 = request.POST.get("name_2")
		phone_2 = request.POST.get("phone_2")
		qualification_2 = request.POST.get("qualification_2")
		residental_state_2 = request.POST.get("residental_state_2")

		name_3 = request.POST.get("name_3")
		phone_3 = request.POST.get("phone_3")
		qualification_3 = request.POST.get("qualification_3")
		residental_state_3 = request.POST.get("residental_state_3")

		nomination_form = NominationForm.objects.create(name_one=name_1, phone_one=phone_1, qualification_one=qualification_1,
			residental_state_one=residental_state_1, name_two=name_2, phone_two=phone_2, qualification_two=qualification_2,
			residental_state_two=residental_state_2, name_three=name_3, phone_three=phone_3, qualification_three=qualification_3,
			residental_state_three=residental_state_3)
		nomination_form.save()

		exam_nomination_form = ExamNominationFormConnector(exam=exam, nomination_form=nomination_form)
		exam_nomination_form.save()

		return HttpResponseRedirect(reverse("theory:add_theory", args=(exam.id,)))
		
	else:
		context = {}
		return render(request, 'nomination_form/add_nomination_form.html', context)
		


def AllNominationFormView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			context = {}
			return render(request, 'nomination_form/all_nomination_form.html', context)
			

			
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		

