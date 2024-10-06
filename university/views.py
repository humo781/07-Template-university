from django.shortcuts import render
from .models import Faculty, Group, Student, Subject, Teacher, Chair


def faculty_view(request):
    faculties = Faculty.objects.all()
    ctx = {'faculties': faculties}
    return render(request, 'faculties.html', ctx)

def group_view(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups.html', ctx)

def kafedra_view(request):
    chairs = Chair.objects.all()
    ctx = {'chairs': chairs}
    return render(request, 'kafedras.html', ctx)

def student_view(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students.html', ctx)

def subject_view(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects.html', ctx)

def teacher_view(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers.html', ctx)
