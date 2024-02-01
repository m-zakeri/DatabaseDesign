from django import forms
from apps.account.models import User
from . import models


class FirstStageAdmissionForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth', 'caption']
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'phone_number': forms.TextInput(),
            'date_of_birth': forms.DateInput(format='%d/%m/%Y'),
            'caption': forms.Textarea()
        }


class SecondStageAdmissionForm(forms.ModelForm):
    user = forms.IntegerField(required=False)

    class Meta:
        model = models.Teacher
        exclude = ['score']
        widgets = {
            'description': forms.Textarea(),
            'gender': forms.RadioSelect(),
            'teaching_experience': forms.TextInput(),
        }


class FourthStageAdmissionForm(forms.ModelForm):
    teacher = forms.IntegerField(required=False)

    class Meta:
        model = models.Work
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'work_phone': forms.TextInput(),
            'employment_file': forms.FileInput()
        }


class FifthStageAdmissionForm(forms.ModelForm):
    teacher = forms.IntegerField(required=False)

    class Meta:
        model = models.Skill
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(),
            'description': forms.Textarea(),
            'certificate_photo': forms.FileInput(),
            'learning_percentage': forms.TextInput()
        }


class SixthStageAdmissionForm(forms.ModelForm):
    teacher = forms.IntegerField(required=False)

    class Meta:
        model = models.LevelEducation
        fields = '__all__'
        widgets = {
            'name_university': forms.TextInput(),
            'date_of_graduation': forms.DateInput(format='%d/%m/%Y'),
            'graduation': forms.Select(),
            'Academic_discipline': forms.TextInput(),
            'graduation_image': forms.FileInput()

        }
