from .models import Review
from django import forms
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',) #