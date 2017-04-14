from django import forms
from .models import *



class addTaskForm(forms.ModelForm):



    taskname                = forms.CharField(label='Task name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    taskDescription         = forms.CharField(label='Task Description', widget=forms.Textarea(attrs={'class':'form-control'}))
    todo_status = (
        ('pending','Pending'),
        ('done','Done')
    )
    taskStatus              = forms.ChoiceField(label='Task Status',widget=forms.Select(attrs={'class':'form-control'}),choices=todo_status)

    class Meta:
        model = todotask
        fields = ['taskname','taskDescription','taskStatus']







class EditTaskForm(forms.ModelForm):

    todo_status = (
        ('pending','Pending'),
        ('done','Done')
    )
    hidestatus = (
        ('1','Show'),
        ('0','Hide'),
    )


    taskname                = forms.CharField(label='Task name', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    taskDescription         = forms.CharField(label='Task Description', widget=forms.Textarea(attrs={'class':'form-control'}))

    taskStatus              = forms.ChoiceField(label='Task Status',widget=forms.Select(attrs={'class':'form-control'}),choices=todo_status)
    hidestatus              =  forms.ChoiceField(label='Show Status',widget=forms.Select(attrs={'class':'form-control'}),choices=hidestatus)

    class Meta:
        model = todotask
        fields = ['taskname','taskDescription','taskStatus','hidestatus']
