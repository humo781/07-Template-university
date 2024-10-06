from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    number_of_departments = models.IntegerField()
    dean = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.faculty_name

class Chair(models.Model):  # chair = kafedra
    chair_name = models.CharField(max_length=255)
    head_of_chair = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.chair_name

class Group(models.Model):
    group_name = models.CharField(max_length=255)
    amount_of_students = models.IntegerField()
    telegram_group = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Chair, on_delete=models.CASCADE)
    recommended_literature = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject_name
