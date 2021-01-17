from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
	title = models.TextField()
	answer_a = models.CharField(max_length=500, default="None")
	answer_b = models.CharField(max_length=500, default="None")
	answer_c = models.CharField(max_length=500, default="None")
	answer_d = models.CharField(max_length=500, default="None")
	real_answer = models.CharField(max_length=500, default="None")
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)