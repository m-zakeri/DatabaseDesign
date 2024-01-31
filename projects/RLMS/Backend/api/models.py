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

class Storage(models.Model):
    storage_id = models.AutoField(primary_key=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.Name

class Product_Info(models.Model):
    product_id = models.AutoField(primary_key=True)
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500) #
    quantity = models.IntegerField()
    creation_Date = models.DateField() #
    expiration_Date = models.DateField() #

    def __str__(self):
        return self.Name



class Supervisor(models.Model):
    Rank = (("Instructor", "Instructor"), ("Assistant", "Assistant"), ("Associate Professor", "Associate Professor"),
            ("Professor", "Professor"), ("Full Professor", "Full Professor")) #
    Supervisor_ID = models.AutoField(primary_key=True)
    Person_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Rank = models.CharField(max_length=100, choices=Rank, default='Instructor')
    Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Field = models.CharField(max_length=100)
    Salary = models.IntegerField()

"""    def __str__(self):
        return self.Supervisor_Name"""

class Degree(models.Model):
    supervisor_ID = models.ForeignKey(Supervisor, on_delete=models.CASCADE, primary_key=True)
    educational_Degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100) #
    started_Date = models.DateField()

    def __str__(self):
        return self.name

class Company(models.Model):
    company_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Contact_Ways(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField(max_length=100)


class Research(models.Model):
    status = (("Pending", "Pending"), ("Ongoing", "Ongoing"), ("Terminated", "Terminated")) #
    research_ID = models.AutoField(primary_key=True)
    student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    #storage_ID = models.ForeignKey(Storage, on_delete=models.CASCADE) #
    company_ID = models.ForeignKey(Company, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    budget = models.IntegerField()
    purpose = models.CharField(max_length=500)
    start_Date = models.DateField()
    end_Date = models.DateField(blank= True)

    def __str__(self):
        return self.name