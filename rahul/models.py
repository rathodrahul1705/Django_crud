from django.db import models

# Create your models here.

class Create(models.Model):
	first_name = models.CharField(max_length = 200)
	last_name = models.CharField(max_length = 200)
	company = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	website = models.CharField(max_length = 200)
