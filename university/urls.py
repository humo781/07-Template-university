from django.urls import path
from .views import faculty_view, group_view, kafedra_view, student_view, subject_view, teacher_view

urlpatterns = [
    path('faculty/', faculty_view),
    path('group/', group_view),
    path('kafedra/', kafedra_view),
    path('student/', student_view),
    path('subject/', subject_view),
    path('teacher/', teacher_view),
]
