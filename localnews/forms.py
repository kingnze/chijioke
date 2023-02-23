from django import forms
from .models import localnewsComment


class localnewsForm(forms.ModelForm):
    class Meta:
        model = localnewsComment
        fields = '__all__'
        exclude = ['localnewsusercomment','post']


