from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=500)
	reg_no = models.CharField(max_length=500)
	batch = models.CharField(max_length=500)

	image = models.FileField(upload_to='student/images/', blank=True)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.name)