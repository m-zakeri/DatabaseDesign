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
        return self.first_namename + " " + self.last_name



class Email(models.Model):
    email_types = (('Personal', 'Personal'), ('Work', 'Work'), ('University', 'University')) #
    email_if = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=100)
    email_type = models.CharField(max_length=100, choices=email_types, default='Personal')

    def __str__(self):
        return self.email_address

class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    person_id  = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.phone_number

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    educational_degree = models.CharField(max_length=100) #
    university = models.CharField(max_length=100) #
    gpa = models.FloatField() #
    field = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id

class Subscription_plan(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField()
    subscription_duration = models.DuritionField()
    price = models.IntegerField()

    @property
    def end_date(self):
        return self.start_date + self.subscription_duration


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    session_number = models.IntegerField()
    estimated_time = models.DurationField()
    description = models.CharField(max_length=500) #
    price = models.IntegerField() #

    def __str__(self):
        return self.name

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.Model(max_length=500)
    work_time = models.DurationField()

    def __str__(self):
        return self.name

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name