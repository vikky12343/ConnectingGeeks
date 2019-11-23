from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
import os

# Create your models here.
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):

	entry_title   = models.CharField(max_length=50)
	entry_text    = RichTextUploadingField(blank=	True, null=True)
	entry_date    = models.DateTimeField(auto_now_add=True)
	entry_author  = models.ForeignKey(User, on_delete=models.CASCADE)
	


	class Meta: 
		verbose_name_plural= 'entries'


	def __str__(self):

		return self.entry_title

def get_image_path(instance, filename):
	
  	return os.path.join('photos', str(instance.id), filename)



class Question(models.Model):
	q_text=models.CharField(max_length=50)
	q_auther=models.ForeignKey(User,on_delete=models.CASCADE)
	q_date=models.DateTimeField(auto_now_add=True)
	
