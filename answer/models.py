from django.db import models
from django.utils import timezone

# Create your models here.

class Answer(models.Model):
	title = models.CharField(max_length=50)
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)