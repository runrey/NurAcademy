from django import forms
from .models import Course, Module


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
    # id = forms.CharField(label='id',widget=forms.HiddenInput, empty_value='667')
    # Title = forms.CharField(label= 'Course title', max_length=100, required=True)
    # Description = forms.CharField(label='Description' ,widget=forms.Textarea)
    # Status = forms.ChoiceField(label='Status', choices=[('IA', 'inactive')])


class ModulesForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['Module_title', 'Content']
        # fields = '__all__'

