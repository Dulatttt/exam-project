from django.db import models
from django.utils import timezone

# Create your models here.

class NominationForm(models.Model):
	name_one = models.CharField(max_length=100)
	phone_one = models.CharField(max_length=100)
	qualification_one = models.TextField()
	residental_state_one = models.CharField(max_length=100)

	name_two = models.CharField(max_length=100)
	phone_two = models.CharField(max_length=100)
	qualification_two = models.TextField()
	residental_state_two = models.CharField(max_length=100)

	name_three = models.CharField(max_length=100)
	phone_three = models.CharField(max_length=100)
	qualification_three = models.TextField()
	residental_state_three = models.CharField(max_length=100)

	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.pub_date)