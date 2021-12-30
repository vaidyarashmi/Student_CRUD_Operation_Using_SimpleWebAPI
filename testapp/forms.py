from django import forms
from django.core.exceptions import ValidationError
from django.forms import fields
from testapp.models import Student
class StudentForm(forms.ModelForm):
    def clean_marks(self):
        input_marks=self.cleaned_data['marks']
        if input_marks > 100 :
            raise ValidationError('The maximum marks should be 100')
        return input_marks
    class Meta:
        model=Student
        fields='__all__'