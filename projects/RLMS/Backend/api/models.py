import datetime
from django.db import models


class Person(models.Model):
    gender_types = (("Male", "Male"), ("Female", "Female"))
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    date_of_birth = models.DateField()
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    national_code = models.CharField(max_length=10, unique=True)

    @property
    def age_calculator(self):
        current_time = datetime.datetime.now().year
        birth_year = self.date_of_birth.year
        return current_time - birth_year

    def __str__(self):
        return f"{self.first_name}" + " " + f"{self.last_name}"


class Email(models.Model):
    email_types = (('Personal', 'Personal'), ('Work', 'Work'), ('University', 'University'))
    email_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=100)
    email_type = models.CharField(max_length=100, choices=email_types, default='Personal')

    def __str__(self):
        return self.email_address

    def get_email_type(self):
        return self.email_type


class Phone(models.Model):
    phone_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.phone_number


class Student(models.Model):
    educational_degree_types = (("Associate", "Associate"), ("Bachelor", "Bachelor"), ("Master", "Master"),
                                ("PhD", "PhD"))
    student_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    educational_degree = models.CharField(max_length=100, choices=educational_degree_types)
    university = models.CharField(max_length=100)
    gpa = models.FloatField()
    field = models.CharField(max_length=100)

    def resume(self):
        return (f"The Student with Student ID {self.student_id} \n and has {self.educational_degree} in "
                f"{self.field} from {self.university} with {self.gpa}")


class Subscription_plan(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    start_date = models.DateField()
    subscription_duration = models.DurationField()
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
    session_number = models.IntegerField(null=True)
    estimated_time = models.DurationField(null=True)
    description = models.CharField(max_length=500)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)
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
        return self.name


class Product_Info(models.Model):
    product_id = models.AutoField(primary_key=True)
    storage_id = models.ForeignKey(Storage, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity = models.IntegerField()
    creation_date = models.DateField()
    expiration_date = models.DateField()

    def is_available(self):
        if self.quantity > 0:
            return True
        return False


class Supervisor(models.Model):
    rank = (("Instructor", "Instructor"), ("Assistant", "Assistant"), ("Associate Professor", "Associate Professor"),
            ("Professor", "Professor"), ("Full Professor", "Full Professor"))
    supervisor_id = models.AutoField(primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    #supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE) #Trying to set relation from Supervosir table to Supervisor table
    rank = models.CharField(max_length=100, choices=rank, default='Instructor')
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    field = models.CharField(max_length=100)
    salary = models.IntegerField()


class Degree(models.Model):
    educational_degree_types = (("Associate", "Associate"), ("Bachelor", "Bachelor"), ("Master", "Master"),
                                ("PhD", "PhD"))
    supervisor_id = models.ForeignKey(Supervisor, on_delete=models.CASCADE, primary_key=True)
    educational_degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    started_date = models.DateField()

    def __str__(self):
        return f'Supervisor with ID {self.supervisor_id} Have Degree of {self.educational_degree}'


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Contact_Ways(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=11)
    email_address = models.EmailField(max_length=100)

    def get_company_email(self):
        return self.email_address

    def get_phone(self):
        return self.phone_number


class Research(models.Model):
    statuses = (("Pending", "Pending"), ("Ongoing", "Ongoing"), ("Terminated", "Terminated"), ("Suspand", "Suspand"))
    research_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    supervisor_id = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=statuses, default='Pending')
    budget = models.IntegerField()
    purpose = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def get_status(self):
        return self.status

