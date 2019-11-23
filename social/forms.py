from django import forms
from .models import Entry

class PostForm(forms.ModelForm):
	class Meta:
		model=Entry
		fields=['entry_text']
