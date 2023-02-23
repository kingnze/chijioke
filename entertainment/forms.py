from django import forms
from .models import entertainmentComment


class entertainmentForm(forms.ModelForm):
    class Meta:
        model = entertainmentComment
        fields = '__all__'
        exclude = ['entertainmentusercomment','post']


