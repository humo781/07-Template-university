from django.contrib import admin
from .models import Faculty, Group, Student, Subject, Chair, Teacher

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_name', 'number_of_departments', 'dean')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'amount_of_students', 'telegram_group')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'group')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'kafedra', 'recommended_literature')

@admin.register(Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = ('chair_name', 'head_of_chair', 'faculty')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio')
