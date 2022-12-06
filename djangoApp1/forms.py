from django import forms

class userNForm(forms.Form):
    name=forms.CharField(label='Name',max_length=300,required=0)