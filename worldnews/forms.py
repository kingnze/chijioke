from django import forms
from .models import worldnewsComment


class worldnewsForm(forms.ModelForm):
    class Meta:
        model = worldnewsComment
        fields = '__all__'
        exclude = ['worldnewsusercomment','post']


