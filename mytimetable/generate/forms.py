from django import forms
from .models import TotalActivities, Subject
from django.forms import ModelForm


class TotalActivitiesForm(ModelForm):
    total = forms.IntegerField()

    class Meta:
        model = TotalActivities
        fields = ['total',]


class SubjectForm(ModelForm):
    name =  forms.CharField(max_length= 30, required=True) 
    hours = forms.IntegerField(required=True)

    class Meta:
        model = Subject
        fields = ['name','hours',]