from django import forms
from .models import Faculty, Group, Teacher, Department, Subject, Student

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['faculty_name']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'amount_of_students']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'bio']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'faculty']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'kafedra']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name']
