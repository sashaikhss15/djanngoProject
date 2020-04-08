from django.db import models
from django.contrib.auth.models import User	#django built-in user

# Create your models here.
class Board(models.Model):
	name = models.CharField(max_length=30,unique=True)
	description = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Topic(models.Model):
	subject = models.CharField(max_length=255)
	last_updated = models.DateTimeField(auto_now_add=True)
	board = models.ForeignKey(Board,on_delete=models.SET_NULL,null=True,related_name="topics")
	starter = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="topics")

class Post(models.Model):
	message = models.TextField(max_length=4000)
	topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True,related_name='posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="posts")#related is optional,but it shows reverse relationship
	updated_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="+")# here  + will not create reverse relationship
