from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	tags = models.CharField(max_length=30, blank=True)
	author = models.ForeignKey(User)
	post_date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title