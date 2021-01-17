from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from student.models import Student

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


def AddStudentView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			full_name = request.POST.get("full_name")
			reg_no = request.POST.get("reg_no")
			batch = request.POST.get("batch")

			try:
				student = Student.objects.get(reg_no=reg_no)
				if Student.objects.get(reg_no=reg_no):
					return HttpResponse("reg no exist")

			except:
				user = User.objects.create(username=reg_no)
				user.set_password(reg_no)
				user.save()

				user_checker = authenticate(username=reg_no, password=reg_no)

				if user_checker:
					#login(request, user)
					student = Student.objects.create(user=user, name=full_name, reg_no=reg_no, batch=batch)
					student.save()

				try:
					image = request.FILES["image"]
					student.image = image
					student.save()
				except:
					pass

				return HttpResponseRedirect(reverse("student:all_student"))
				

		else:
			context = {}
			return render(request, 'student/add_student.html', context)
	
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)dd")		





def StudentDetailView(request, id):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			student = Student.objects.get(id=id)

			context = {"student": student}
			return render(request, 'student/student_detail.html', context)
		
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		



def AllStudentView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			students = Student.objects.all()
			context = {"students": students}
			return render(request, 'student/all_student.html', context)
		

	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		




def EditStudentView(request, id):
	if request.user.is_superuser == True:
		student = Student.objects.get(id=id)

		if request.method == "POST":
			full_name = request.POST.get("full_name")
			reg_no = request.POST.get("reg_no")
			batch = request.POST.get("batch")

			try:
				if Student.objects.get(reg_no=reg_no):
					new_student = Student.objects.get(reg_no=reg_no)
					if new_student.id == student.id:
						student.name = full_name
						student.reg_no = reg_no
						student.batch = batch

						student.save()


						return HttpResponseRedirect(reverse("student:all_student"))

					else:
						return HttpResponse("reg no exist")

			except:

				student.name = full_name
				student.reg_no = reg_no
				student.batch = batch

				student.save()


				return HttpResponseRedirect(reverse("student:all_student"))

		else:
			context = {"student": student}
			return render(request, 'student/edit_student.html', context)
	
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)dd")		
