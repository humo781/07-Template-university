from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=255)

    def __str__(self):
        return self.faculty_name

class Department(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    amount_of_students = models.IntegerField()

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    kafedra = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
