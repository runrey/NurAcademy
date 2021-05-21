from django import forms
from .models import Course, Module
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['id', 'Title', 'Description']

    Status = forms.ChoiceField(label='Status', choices=[('IA', 'inactive')])



class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['Module_title', 'Content']
        exclude = []
        # fields = '__all__'

