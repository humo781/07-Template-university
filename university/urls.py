from django.urls import path
from . import views

urlpatterns = [
    # fakultet manzillari
    path('faculties/', views.faculty_list, name='faculty_list'),
    path('faculties/create/', views.faculty_create, name='faculty_create'),
    path('faculties/<int:pk>/edit/', views.faculty_update, name='faculty_update'),
    path('faculties/<int:pk>/delete/', views.faculty_delete, name='faculty_delete'),

    # group manzillari
    path('groups/', views.group_list, name='group_list'),
    path('group/create/', views.group_create, name='group_create'),
    path('groups/<int:pk>/edit/', views.group_update, name='group_update'),
    path('groups/<int:pk>/delete/', views.group_delete, name='group_delete'),

    # department manzillari
    path('departments/', views.department_list, name='department_list'),
    path('department/create/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),

    # teacher manzillari
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/create/', views.teacher_create, name='teacher_create'),
    path('teachers/<int:pk>/edit/', views.teacher_update, name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.teacher_delete, name='teacher_delete'),

    # student manzillari
    path('students/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),

    # subject manzillari
    path('subjects/', views.subject_list, name='subject_list'),
    path('subject/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/edit/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_update, name='subject_update'),
]
