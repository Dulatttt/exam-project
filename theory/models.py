from django.db import models
from django.utils import timezone

# Create your models here.
class Theory(models.Model):
	title = models.TextField()
	
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		#return self.cart_id
		return str(self.title)