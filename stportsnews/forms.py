from django import forms
from .models import stportnewsComment


class stportnewsForm(forms.ModelForm):
    class Meta:
        model = stportnewsComment
        fields = '__all__'
        exclude = ['stportnewsusercomment','post']


