from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Address(models.Model):
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"
        
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField(null=True, blank=True)
    building_name = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255)
    floor = models.IntegerField(null=True, blank=True)
    unit_number = models.IntegerField(null=True, blank=True)
    plate_number = models.CharField(max_length=10)
    postal_code = models.CharField(max_length=20, unique=True)
    coordinate = models.CharField(max_length=255, blank=True, null=True)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.state} state, {self.city} city, {self.street} street, {self.district} district"

    def clean(self):

        if self.street_number and not self.street_number > 0:
            raise ValidationError("Street number must be greater than zero.")

        if self.floor and not self.floor > 0:
            raise ValidationError("Floor must be greater than zero.")

        if self.unit_number and not self.unit_number > 0:
            raise ValidationError("Unit Number must be greater than zero.")


class Education(models.Model):
    start_date = models.DateField()
    graduation_date = models.DateField()
    major = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    institution_name = models.CharField(max_length=255)
    institution_address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.institution_name}"
    
    def clean(self):
        # Date Constraints
        if self.start_date >= self.graduation_date:
            raise ValidationError("Start date cannot be same or after graduation date.")

        if self.start_date > timezone.now().date():
            raise ValidationError("Start date cannot be in future.")

        if self.graduation_date > timezone.now().date():
            raise ValidationError("Graduation date cannot be in the future.")
        
        # GPA Constraints
        if not (0 <= self.gpa <= 20):
            raise ValidationError("GPA should be between 0.00 and 20.00.")
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class PhoneNumber(models.Model):

    class Meta:
            verbose_name = "Phone Number"
            verbose_name_plural = "Phone Numbers"
        
    PHONE_TYPES = (("Mobile", "Mobile"), ("Work", "Work"), ("Home", "Home"))
    phone_number = models.CharField(max_length=20)
    phone_type = models.CharField(max_length=6, choices=PHONE_TYPES, default="Mobile")
    
    def __str__(self):
        return f"{self.phone_type}: {self.phone_number}"
    
    def clean(self):
        if not self.phone_number.isdigit():
            raise ValidationError("Phone number must be number")


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    GENDER_TYPES = (("M", "Male"), ("F", "Female"))
    persian_first_name = models.CharField(max_length=255)
    persian_last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_TYPES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    national_code = models.CharField(max_length=20, unique=True)
    picture = models.ImageField(upload_to="images/", blank=True)
    home_address = models.ForeignKey(
        Address, on_delete=models.SET_NULL, null=True
    )
    educations = models.ManyToManyField(Education)
    phone_numbers = models.ManyToManyField(PhoneNumber)

    def get_age(self):
        """
        Calculate and return user age.
        """
        current_year = timezone.now().year
        birth_year = self.date_of_birth.year
        return current_year - birth_year

    def get_persian_first_name(self):
        """
        Return the persian_first_name.
        """
        return self.persian_first_name

    def get_persian_last_name(self):
        """
        Return the persian_last_name.
        """
        return self.persian_last_name

    def get_persian_full_name(self):
        """
        Return the persian_first_name and persian_last_name.
        """
        return f"{self.persian_first_name} {self.persian_last_name}"

    def get_full_name(self):
        """
        Return the first_name and last_name from user
        """
        if self.user.first_name and self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}".title()
    
    def clean(self):
        if not self.national_code.isdigit():
            raise ValidationError('National code must contain only digits.')
        
        if self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be in the future.")

    def __str__(self):
        if self.get_full_name():
            return  self.get_full_name()
        else:
            return self.get_persian_full_name()


class Building(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    floors = models.IntegerField()
    capacity = models.IntegerField()
    rooms = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.title()
    
    def clean(self):

        if self.creation_date > timezone.now().date():
            raise ValidationError("Creation date cannot be in the future.")
        
        if not (self.floors > 0):
            raise ValidationError("Floors must be greater than zero.")
        
        if not (self.capacity > 0):
            raise ValidationError("Capacity must be greater than zero.")

        if not (self.rooms > 0):
            raise ValidationError("Rooms must be greater than zero.")
    

class Faculty(models.Model):
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        
    name = models.CharField(max_length=255)
    creation_date = models.DateField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.title()
    
    def clean(self):

        if self.creation_date > timezone.now().date():
            raise ValidationError("Creation date cannot be in the future.")
    

class Department(models.Model):
    name = models.CharField(max_length=255)
    budget = models.IntegerField()
    creation_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name.title()
              
    def clean(self):

        if self.name.lower() == self.faculty.name.lower():
            raise ValidationError("Faculty and department name cannot be the same.")
        
        if not self.budget > 0:
            raise ValidationError("Budget must be greater than zero.")
        
        if self.creation_date > timezone.now().date():
            raise ValidationError("Creation date cannot be in the future.")
        
        if self.creation_date < self.faculty.creation_date:
            raise ValidationError("Department creation date cannot be earlier than faculty creation date.")
        


class Office(models.Model):
    
    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"
        
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"office: {self.phone_number.phone_number}"
    
    def clean(self):

        if self.phone_number.phone_type != 'Work':
            raise ValidationError("The phone number type associated with the office must be 'Work'.")
    

class Employee(models.Model):
    
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        

    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    salary = models.IntegerField()
    hire_date = models.DateField()
    office_hours = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    office = models.ManyToManyField(Office)
    
    def __str__(self):
        return f"Employee: {self.person.get_full_name()}"
    
    def clean(self):
        if not self.salary > 0:
            raise ValidationError("The salary must be greater than zero.")
        
        if self.hire_date > timezone.now().date():
            raise ValidationError("Hire date cannot be in the future.")
        
        if self.hire_date < self.person.user.date_joined.date():
            raise ValidationError("Hire date cannot be earlier than user registration date.")


class Field(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="fields"
    )
    head = models.OneToOneField(
        "Professor", on_delete=models.SET_NULL, null=True, blank=True, related_name="head_of_field"
    )
    
    def __str__(self):
        return self.name.title()
    

class Professor(models.Model):
    
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professors"

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    RANK_CHOICES = [
        ("Instructor", "Instructor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Associative Professor", "Associative Professor"),
        ("Full Professor", "Full Professor"),
    ]
    rank = models.CharField(max_length=255, choices=RANK_CHOICES)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    is_in_committee = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Professor: {self.employee.person.get_full_name()} rank: {self.rank}  field:{self.field}"
    

class Researcher(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Professor: {self.employee.person.get_full_name()} field:{self.field}"


class Research(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    search_area = models.TextField()
    funding_source = models.TextField()
    budget = models.IntegerField()
    description = models.TextField()
    publication = models.TextField()
    keywords = models.TextField()
    STATUS_CHOICE = [("ToDo", "ToDo"), ("InProgress", "InProgress"), ("Done", "Done")]
    status = models.CharField(choices=STATUS_CHOICE, max_length=10, default="ToDo")
    website = models.TextField(blank=True, null=True)
    related_research = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title.title()
    
    def clean(self):
        if self.end_date and self.start_date >= self.end_date:
            raise ValidationError("End date cannot be earlier than start date.")
        
        if not self.budget > 0:
            raise ValidationError("Buget must be greater than zero.")


class ResearchMember(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True, blank=True)
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE, null=True, blank=True)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    role = models.CharField(max_length=255)
    
    def __str__(self):
        if self.professor:
            return f"ResearchMember: {self.professor} - Role: {self.role}"
        elif self.researcher:
            return f"ResearchMember: {self.researcher} - Role: {self.role}"
    
    def clean(self):
        if self.professor is None and self.researcher is None:
            raise ValidationError("A research member must be either a professor or a researcher.")


class Schedule(models.Model):
    DAY_CHOICES = [
        ("Sat", "Saturday"),
        ("Sun", "Sunday"),
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
    ]
    day = models.CharField(choices=DAY_CHOICES, max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()


class Laboratory(models.Model):
    
    class Meta:
        verbose_name = "Laboratory"
        verbose_name_plural = "Laboratories"
        
    name = models.CharField(max_length=255)
    equipments = models.TextField()
    capacity = models.IntegerField()
    budget = models.IntegerField()
    managers = models.ManyToManyField(Employee)
    schedules = models.ManyToManyField(Schedule)
    
    def __str__(self):
        return self.name.title()

    def clean(self):
        days_of_schedules = [schedule.day for schedule in self.schedules]
        if len(set(days_of_schedules)) != len(days_of_schedules):
            raise ValidationError("Days of laboratory's schedules should be unique")
        
        
class Library(models.Model):
    
    class Meta:
        verbose_name = "Library"
        verbose_name_plural = "Libraries"
        
    name = models.CharField(max_length=255)
    capacity = models.IntegerField()
    books = models.IntegerField()
    managers = models.ManyToManyField(Employee)
    schedules = models.ManyToManyField(Schedule)
    
    def __str__(self):
        return self.name.title()

    def clean(self):
        days_of_schedules = [schedule.day for schedule in self.schedules]
        if len(set(days_of_schedules)) != len(days_of_schedules):
            raise ValidationError("Days of library's schedules should be unique")
