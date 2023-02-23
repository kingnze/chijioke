from django import forms
from .models import Contact,Comment,TrendingComment,CrimeCommemt,EnvironmentComment,HealthComment,BusinessComment ,TechComment,Commet,PoliticsComment

class TrendingForm(forms.ModelForm):
    class Meta:
        model = TrendingComment
        fields = '__all__'
        exclude = ['Trendingusercomment','post']

class CrimeForm(forms.ModelForm):
    class Meta:
        model = CrimeCommemt
        fields = '__all__'
        exclude = ['Crimeusercomment','post']

class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = EnvironmentComment
        fields = '__all__'
        exclude = ['Environmentusercomment','post']

class HealthForm(forms.ModelForm):
    class Meta:
        model = HealthComment
        fields = '__all__'
        exclude = ['Healthusercomment','post']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = BusinessComment
        fields = '__all__'
        exclude = ['Businessusercomment','post']

class PoliticsForm(forms.ModelForm):
    class Meta:
        model = PoliticsComment
        fields = '__all__'
        exclude = ['Politicsusercomment','post']

class TechForm(forms.ModelForm):
    class Meta:
        model = TechComment
        fields = '__all__'
        exclude = ['Techusercomment','post']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'fullname':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'message':forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['usercomment','post']

class CommetForm(forms.ModelForm):
    class Meta:
        model = Commet
        fields = '__all__'
        exclude = ['usercomment','post']


