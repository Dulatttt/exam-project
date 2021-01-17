from django.db import models

from student.models import Student
from question.models import Question
from answer.models import  Answer
from theory.models import Theory
from nomination_form.models import NominationForm
from result.models import Result

from django.utils import timezone

# Create your models here.

class Exam(models.Model):
	title = models.CharField(max_length=500)
	exam_slug = models.CharField(max_length=500, default="no slug")
	exam_type = models.CharField(max_length=500)
	batch = models.CharField(max_length=500)

	duration = models.CharField(max_length=500)
	
	students = models.ManyToManyField(Student, through="ExamStudentConnector")
	questions = models.ManyToManyField(Question, through="ExamQuestionConnector")
	answers = models.ManyToManyField(Answer, through="ExamAnswerConnector")

	theorys = models.ManyToManyField(Theory, through="ExamTheoryConnector")

	nomination_forms = models.ManyToManyField(NominationForm, through="ExamNominationFormConnector")

	total_score = models.IntegerField(default=0)

	results = models.ManyToManyField(Result, through="ExamResultConnector")

	status = models.BooleanField(default=False)
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)




  
class ExamStudentConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


  
class ExamQuestionConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ExamAnswerConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ExamTheoryConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	theory = models.ForeignKey(Theory, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ExamNominationFormConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	nomination_form = models.ForeignKey(NominationForm, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)


class ExamResultConnector(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	result = models.ForeignKey(Result, on_delete=models.CASCADE)
	pub_date = models.DateTimeField(default=timezone.now)
