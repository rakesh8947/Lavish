from django.db import models
from datetime import datetime

class Office(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    pub_date= models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Scontact(models.Model):
	Name = models.CharField(max_length=20)
	Lname = models.CharField(max_length=20)
	Contact = models.CharField(max_length=20)
	Email = models.EmailField(max_length=20)
	Message = models.TextField(max_length=100)

	def __str__(self):
		return self.Name



# Create your models here.
