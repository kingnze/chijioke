from django import forms
from .models import africanewsComment
from django.contrib.auth.decorators import login_required



class africanewsForm(forms.ModelForm):
    class Meta:
        model = africanewsComment
        fields = '__all__'
        exclude = ['africanewsusercomment','post']


