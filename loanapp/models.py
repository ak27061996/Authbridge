
from django.db import models


class LoanApplication(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(default='', max_length=50)
	dob = models.DateTimeField(null=True)
	phone = models.CharField(default='', max_length=50)
	email = models.CharField(default='', max_length=50)
	amount = models.IntegerField(default=0)
	status = models.BooleanField(default=False) 
