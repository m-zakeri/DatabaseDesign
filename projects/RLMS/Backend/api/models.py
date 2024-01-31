import datetime
from django.db import models

class Person(models.Model):
    Gender_Types = (("Male", "Male"), ("Female", "Female")) #
    ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Father_Name = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100) #
    Address = models.CharField(max_length=500)
    Date_of_Birth = models.DateField()
    Picture = models.ImageField(upload_to='images/', null=True, blank=True) #
    National_Code = models.CharField(max_length=10, unique=True) #



    def age_calculator(self):
        current_time = datetime.datetime.now().year
        birth_year = self.Date_of_Birth.year
        return current_time - birth_year

    def __str__(self):
        return self.name + " " + self.family



class Email(models.Model):
    Email_Types = (('Personal', 'Personal'), ('Work', 'Work'), ('University', 'University')) #
    Email_ID = models.AutoField(primary_key=True)
    Person_ID = models.ForeignKey(Person, on_delete=models.CASCADE)
    Email_Address = models.EmailField(max_length=100)
    Email_Type = models.CharField(max_length=100, choices=Email_Types, default='Personal')

    def __str__(self):
        return self.Email_Address

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

class Storage(models.Model):
    Storage_ID = models.AutoField(primary_key=True)
    Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)


    def __str__(self):
        return self.Name

class Product_Info(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Storage_ID = models.ForeignKey(Storage, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=500) #
    Quantity = models.IntegerField()
    Creation_Date = models.DateField() #
    Expiration_Date = models.DateField() #

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
    Supervisor_ID = models.ForeignKey(Supervisor, on_delete=models.CASCADE, primary_key=True)
    Educational_Degree = models.CharField(max_length=100)
    University = models.CharField(max_length=100) #
    Started_Date = models.DateField()

    def __str__(self):
        return self.Name

class Company(models.Model):
    Company_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=500)

    def __str__(self):
        return self.Name

class Contact_Ways(models.Model):
    Company_ID = models.ForeignKey(Company, on_delete=models.CASCADE, primary_key=True)
    Phone_Number = models.CharField(max_length=11)
    Email_Address = models.EmailField(max_length=100)


class Research(models.Model):
    Status = (("Pending", "Pending"), ("Ongoing", "Ongoing"), ("Terminated", "Terminated")) #
    Research_ID = models.AutoField(primary_key=True)
    Student_ID = models.ForeignKey(Student, on_delete=models.CASCADE)
    Department_ID = models.ForeignKey(Department, on_delete=models.CASCADE)
    #Storage_ID = models.ForeignKey(Storage, on_delete=models.CASCADE) #
    Company_ID = models.ForeignKey(Company, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=100)
    Status = models.CharField(max_length=100)
    Budget = models.IntegerField()
    Purpose = models.CharField(max_length=500)
    Start_Date = models.DateField()
    End_Date = models.DateField(blank= True)

    def __str__(self):
        return self.Name