from django.db import models

from student.models import Student

from django.utils import timezone

# Create your models here.

class Result(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)

	exam_id = models.CharField(max_length=100, default="none")
	exam_title = models.CharField(max_length=100, default="none")
	exam_type = models.CharField(max_length=100, default="none")
	exam_slug = models.CharField(max_length=100, default="none")

	answers = models.CharField(max_length=100, default="none")
	response_nomination_form_id = models.CharField(max_length=100, default="none")
	response_theory = models.TextField(default="none")

	score = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
	percentage = models.IntegerField(default=0)

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.student.name)