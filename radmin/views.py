from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def IndexView(request):
	if request.user.is_superuser == True:
		if request.method == "POST":
			pass
			
		else:
			context = {}
			return render(request, "radmin/index.html", context)
			
	else:
		return HttpResponse("Not Authorised!, Please contact NigTech(www.NigTech.net)")		

