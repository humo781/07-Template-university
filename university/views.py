from django.shortcuts import render, redirect, get_object_or_404
from .forms import FacultyForm, GroupForm, DepartmentForm, TeacherForm, StudentForm, SubjectForm
from .models import Faculty, Group, Department, Teacher, Student, Subject

# faculty viewlari
def faculty_create(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'faculty/faculty_create.html', {'form': form})

def faculty_list(request):
    faculties = Faculty.objects.all()
    return render(request, 'faculty/faculty_list.html', {'faculties': faculties})

def faculty_update(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.name = request.POST['name']
        faculty.save()
        return redirect('faculty_list')

    return render(request, 'faculty/faculty_update.html', {'faculty': faculty})

def faculty_delete(request, pk):
    faculty = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        faculty.delete()
        return redirect('faculty_list')
    return render(request, 'faculty/faculty_confirm_delete.html', {'faculty': faculty})

# group viewlari

def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group/group_create.html', {'form': form})


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group/group_list.html', {'groups': groups})

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.name = request.POST['name']
        group.save()
        return redirect('group_list')
    return render(request, 'group/group_update.html', {'group': group})

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'group/group_confirm_delete.html', {'group': group})

# department viewlari

def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department/department_list')
    else:
        form = GroupForm()
    return render(request, 'department/department_create.html', {'form': form})


def department_list(request):
    departments = Department.objects.all()
    return render(request, 'department/department_list.html', {'departments': departments})

def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.name = request.POST['name']
        department.save()
        return redirect('department/department_list')
    return render(request, 'department/department_update.html', {'department': department})

def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department/department_list')
    return render(request, 'department/department_confirm_delete.html', {'department': department})

# teacher viewlari
def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher/teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher/teacher_create.html', {'form': form})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher/teacher_list.html', {'teachers': teachers})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.first_name = request.POST['name']
        teacher.save()
        return redirect('teacher/teacher_list')
    return render(request, 'teacher/teacher_update.html', {'teacher': teacher})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher/teacher_list')
    return render(request, 'teacher/teacher_confirm_delete.html', {'teacher': teacher})

# student viewlari
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_create.html', {'form': form})


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.first_name = request.POST['name']
        student.save()
        return redirect('student_list')
    return render(request, 'student/student_update.html', {'student': student})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'student': student})

# subject viewlari
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject/subject_list')
    else:
        form = SubjectForm()
    return render(request, 'subject/subject_create.html', {'form': form})


def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject/subject_list.html', {'subjects': subjects})

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.name = request.POST['name']
        subject.save()
        return redirect('subject/subject_list')
    return render(request, 'subject/subject_update.html', {'subject': subject})

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject/subject_list')
    return render(request, 'subject/subject_confirm_delete.html', {'subject': subject})
