from django.db import models

class Book(models.Model):
	name=models.CharField(max_length=100, blank=False)
	author=models.CharField(max_length=50, blank=False)
	book_ISBN=models.CharField(max_length=50, blank=False)
	pub_date=models.CharField(max_length=50, blank=False)
	category=models.CharField(max_length=100, blank=False)
	

