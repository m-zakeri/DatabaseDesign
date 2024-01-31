from django.db import models

# Create your models here.

import datetime
from django.db import models

class Person(models.Model):
    gender_types = (("Male", "Male"), ("Female", "Female")) #
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100) #
    address = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True) #
    national_code = models.CharField(max_length=10, unique=True) #


    def age_calculator(self):
        current_time = datetime.datetime.now().year
        birth_year = self.date_of_birth.year
        return current_time - birth_year

    def __str__(self):
        return self.first_name + " " + self.last_name



class Email(models.Model):
    email_types = (('Personal', 'Personal'), ('Work', 'Work'), ('University', 'University')) #
    Email_ID = models.AutoField(primary_key=True)
    Person_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Email_Address = models.EmailField(max_length=100)
    Email_Type = models.CharField(max_length=100, choices=email_types, default='Personal')

    def __str__(self):
        return self.Email_Address

    def get_email_type(self):
        return self.email_type

class Phone(models.Model):
    Phone_ID = models.AutoField(primary_key=True)
    Person_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Phone_Number = models.CharField(max_length=11)

    def __str__(self):
        return self.Phone_Number

class Student(models.Model):
    Student_ID = models.AutoField(primary_key=True)
    Person_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Educational_Degree = models.CharField(max_length=100) #
    University = models.CharField(max_length=100) #
    GPA = models.FloatField() #
    Field = models.CharField(max_length=100)

    def __str__(self):
        return self.Student_Number

class Subscription_plan(models.Model):
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Start_Date = models.DateField()
    Subscription_Duration = models.DuritionField()
    Price = models.IntegerField()

    @property
    def end_date(self):
        return self.Start_Date + self.Subscription_Duration

    def __str__(self):
        return self.Plan_Name

class Course(models.Model):
    Course_ID = models.AutoField(primary_key=True)
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Platform = models.CharField(max_length=100)
    Subject = models.CharField(max_length=100)
    Session_Number = models.IntegerField()
    Estimated_Time = models.DurationField()
    Description = models.CharField(max_length=500) #
    Price = models.IntegerField() #

    def __str__(self):
        return self.Name

class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.Model(max_length=500)
    Work_Time = models.DurationField()

    def __str__(self):
        return self.Name

class Room(models.Model):
    Room_ID = models.AutoField(primary_key=True)
    Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)


    def __str__(self):
        return self.Name