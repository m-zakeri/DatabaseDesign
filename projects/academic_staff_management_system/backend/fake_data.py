from googletrans import Translator
from faker import Faker
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from api import models
import random
import io
import datetime
import requests


translator = Translator()
fake = Faker()
persian_fake = Faker(["fa_IR"])
Faker.seed(2)

MAJORS = [
    "Business Administration",
    "Management",
    "Marketing",
    "Finance",
    "Accounting",
    "International Business",
    "Entrepreneurship",
    "Mechanical Engineering",
    "Civil Engineering",
    "Electrical Engineering",
    "Computer Engineering",
    "Chemical Engineering",
    "Aerospace Engineering",
    "Biomedical Engineering",
    "Computer Science",
    "Information Technology",
    "Software Engineering",
    "Data Science",
    "Cybersecurity",
    "Computer Information Systems",
    "Nursing",
    "Medicine",
    "Pharmacy",
    "Public Health",
    "Health Administration",
    "Physical Therapy",
    "Medical Laboratory Science",
    "Biology",
    "Chemistry",
    "Physics",
    "Environmental Science",
    "Geology",
    "Astronomy",
    "Mathematics",
    "Psychology",
    "Sociology",
    "Anthropology",
    "Political Science",
    "Economics",
    "International Relations",
    "Social Work",
    "English",
    "History",
    "Philosophy",
    "Literature",
    "Linguistics",
    "Religious Studies",
    "Art History",
    "Elementary Education",
    "Secondary Education",
    "Special Education",
    "Early Childhood Education",
    "Educational Leadership",
    "Counseling",
    "Journalism",
    "Public Relations",
    "Media Studies",
    "Advertising",
    "Communication Sciences",
    "Studio Art",
    "Graphic Design",
    "Performing Arts (Theatre, Dance, Music)",
    "Film Studies",
    "Photography",
    "Agricultural Business",
    "Environmental Science",
    "Forestry",
    "Animal Science",
    "Horticulture",
    "Information Systems",
    "Mechanical Technology",
    "Electrical Technology",
    "Construction Management",
    "Industrial Design",
    "Public Administration",
    "Policy Studies",
    "Urban Planning",
    "Social Policy",
    "Nonprofit Management",
    "Criminal Justice",
    "Criminology",
    "Legal Studies",
    "Pre-law",
    "Mathematics",
    "Statistics",
    "Actuarial Science",
    "Applied Mathematic",
]
DEGREES = [
    "Associate's Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "Doctoral Degree (Doctorate or PhD)",
    "Professional Degrees",
    "Certificate Programs",
    "Diplomas",
    "Honorary Degrees",
    "Postgraduate Diplomas and Certificates",
    "Undergraduate Certificates",
]
UNIVERSITIES = [
    "University of Tehran ",
    "Sharif University of Technology ",
    "Iran University of Science and Technology ",
    "Amirkabir University of Technology ",
    "Isfahan University of Technology ",
    "Shiraz University ",
    "Tarbiat Modares University ",
    "University of Isfahan ",
    "Iran University of Medical Sciences ",
    "K. N. Toosi University of Technology ",
    "Massachusetts Institute of Technology ",
    "Stanford University:",
    "Harvard University:",
    "California Institute of Technology ",
    "University of Oxford:",
    "University of Cambridge:",
    "ETH Zurich - Swiss Federal Institute of Technology:",
    "University of Chicago:",
    "Imperial College London:",
    "University College London ",
    "Princeton University:",
    "University of California, Berkeley:",
    "Yale University:",
    "Columbia University:",
    "University of California, Los Angeles ",
]
PHONE_TYPES = ["Mobile", "Work", "Home"]
GENDERS = ["M", "F"]
NATIONALITIES = ["Iran", "Japanese", "Iraq", "Chinese"]


def gen_address_object(n):
        for _ in range(n - len(models.Address.objects.all())):
                address = models.Address(
                state=fake.city(),
                city=fake.city(),
                street=fake.street_name(),
                street_number=fake.building_number(),
                building_name=fake.building_number(),
                district=fake.random_int(min=1, max=10),
                floor=fake.random_int(min=1, max=10),
                unit_number=fake.random_int(min=1, max=5),
                plate_number=fake.zipcode(),
                postal_code=fake.zipcode(),
                coordinate=f"{fake.latitude()}:{fake.longitude()}",
                )
                address.save()

def gen_education_object(n):
    
    num_addresses = models.Address.objects.count()    
    
    for _ in range(n - len(models.Education.objects.all())):
        
        random_address_id = fake.random_int(min=1, max=num_addresses)
        
        start_date_start = datetime.date(2010, 1, 1)
        start_date_end = datetime.date(2015, 12, 31)
        
        graduation_date_start = datetime.date(2016, 1, 1)
        graduation_date_end = datetime.date(2020, 12, 31)
        
        
        education = models.Education(
            start_date=fake.date_between(start_date=start_date_start, end_date=start_date_end),
            graduation_date=fake.date_between(start_date=graduation_date_start, end_date=graduation_date_end),
            major=random.choice(MAJORS),
            degree=random.choice(DEGREES),
            gpa=random.randrange(0, 10000) / 100,
            institution_name=random.choice(UNIVERSITIES),
            institution_address=models.Address.objects.all()[random_address_id-1],
        )
        education.save()


def gen_phone_number(n):
    for _ in range(n - len(models.PhoneNumber.objects.all())):
        phone_number = models.PhoneNumber(
            phone_number=fake.phone_number(), phone_type=random.choice(PHONE_TYPES)
        )
        phone_number.save()


def gen_user(n):
    for i in range(n - User.objects.count()):
        try:
            print(f"We construct user {i}")
            persian_first_name = persian_fake.first_name()
            persian_last_name = persian_fake.last_name()
            user = User(
                username=fake.user_name(),
                first_name=translator.translate(persian_first_name).text,
                last_name=translator.translate(persian_last_name).text,
                email=fake.email(),
                password=fake.pystr(),
            )
            user.set_password(user.password)
            user.save()

            image_response = requests.get("https://thispersondoesnotexist.com/")
            image = image_response.content
            image_content = ContentFile(image)
            uploaded_file = SimpleUploadedFile(fake.file_name(extension="jpg"), image_content.read())
            
            
            random_address_id = models.Address.objects.count()
            random_address = models.Address.objects.all()[random_address_id-1]
            
            start_date = datetime.date(1970, 1, 1)
            end_date = datetime.date(2000, 12, 31)
            
            person = models.Person(
                user=user,
                persian_first_name=persian_first_name,
                persian_last_name=persian_last_name,
                gender=random.choice(GENDERS),
                date_of_birth=fake.date_between(start_date=start_date, end_date=end_date),
                nationality=random.choice(NATIONALITIES),
                national_code=fake.passport_number(),
                picture=uploaded_file,
                home_address=random_address,
            )
            person.save()
            
            for j in range(random.randrange(1, 5)):
                random_phone_number_id = fake.random_int(min=1, max=models.PhoneNumber.objects.count())
                random_phone_number = models.PhoneNumber.objects.all()[random_phone_number_id-1]
                person.phone_numbers.add(random_phone_number)
            
            for j in range(random.randrange(1, 5)):
                random_education_id = fake.random_int(min=1, max=models.Education.objects.count())
                random_education = models.Education.objects.all()[random_education_id-1]
                person.educations.add(random_education)
        except:
            pass


def gen_building_object(n):
    
    num_address = models.Address.objects.count()
    
    for _ in range(n - models.Building.objects.count()):
        try:
        
            random_address_id = fake.random_int(min=1, max=num_address)
            selected_address = models.Address.objects.all()[random_address_id-1]
            
            start_date = datetime.date(2010, 1, 1)
            end_date = datetime.date(2014, 12, 31)
            
            building = models.Building(
                name=fake.company(),
                creation_date=fake.date_between(start_date=start_date, end_date=end_date),
                floors=random.randint(1, 20),
                capacity=random.randint(50, 1000), 
                rooms=random.randint(1, 200), 
                address=selected_address,
            )
            building.save()
        except:
            pass

        
def gen_faculty_object(n):

    num_buildings = models.Building.objects.count()
    
    for _ in range(n - models.Faculty.objects.count()):
        try:
        
            random_building_id = fake.random_int(min=1, max=num_buildings)
            selected_building = models.Building.objects.all()[random_building_id-1]
            
            start_date = datetime.date(2015, 1, 1)
            end_date = datetime.date(2016, 12, 31)
            
            faculty = models.Faculty(
                name=fake.company(),
                creation_date=fake.date_between(start_date=start_date, end_date=end_date),
                building=selected_building,
            )
            faculty.save()
        except:
            pass
        
def gen_department_object(n):
    
    num_faculties = models.Faculty.objects.count()
    
    for _ in range(n - models.Department.objects.count()):
        try:
        
            random_faculty_id = fake.random_int(min=1, max=num_faculties)
            selected_faculty = models.Faculty.objects.all()[random_faculty_id-1]
            
            start_date = datetime.date(2017, 1, 1)
            end_date = datetime.date(2018, 12, 31)
            
            department = models.Department(
                name=fake.word(),
                budget=random.randint(10000, 1000000), 
                creation_date=fake.date_between(start_date=start_date, end_date=end_date),
                faculty=selected_faculty,
            )
            department.save()
        except:
            pass


def gen_office_object(n):
    
    num_phone_numbers = models.PhoneNumber.objects.filter(phone_type="Work").count()
    num_departments = models.Department.objects.count()
        
    for _ in range(n - len(models.Office.objects.all())):
        
        random_phone_number_id = fake.random_int(min=1, max=num_phone_numbers)
        selected_phone_number = models.PhoneNumber.objects.filter(phone_type="Work")[random_phone_number_id-1]
        
        random_department_id = fake.random_int(min=1, max=num_departments)
        selected_department = models.Department.objects.all()[random_department_id-1]
        
        office = models.Office(
            phone_number=selected_phone_number,
            department=selected_department
        )
        office.save()


def gen_field_object(n):
    
    num_departments = models.Department.objects.count()
    
    for _ in range(n - models.Field.objects.count()):
        
        random_department_id = fake.random_int(min=1, max=num_departments)
        selected_department = models.Department.objects.all()[random_department_id-1]
        
        
        field = models.Field(
            name=fake.word(),
            department=selected_department,
        )
        field.save()


def gen_employee_object():
    
    num_persons = models.Person.objects.count()
    num_offices = models.Office.objects.count()
    
    for selected_person in models.Person.objects.all():
        
        random_office_id = fake.random_int(min=1, max=num_offices)
        selected_office = models.Office.objects.all()[random_office_id-1]
        
        office_hours = f"{fake.time()}-{fake.time()}"
        
        
        employee = models.Employee(
        person=selected_person,
        salary=random.randint(10000, 1000000),
        hire_date=selected_person.user.date_joined.date(),
        office_hours=office_hours,
        status=random.choice(['Full-time', 'Part-time']),
        is_committee=random.choice([True, False]) 
        )
        employee.save()
        employee.office.add(selected_office)
        

def gen_professor_object(n):
    
    num_fields = models.Field.objects.count()
    
    for selected_employee in models.Employee.objects.all()[:n]:
        try:                    
            random_field_id = fake.random_int(min=1, max=num_fields)
            selected_field = models.Field.objects.all()[random_field_id-1]
            
            professor = models.Professor(
                employee=selected_employee,
                rank=random.choice(["Instructor", "Assistant Professor", "Associative Professor", "Full Professor"]),
                field=selected_field,
                is_in_committee=fake.boolean(chance_of_getting_true=50)
            ) 
            professor.save()
        except:
            pass


def gen_researcher_object(n):
    
    num_professors = models.Professor.objects.count()
    num_fields = models.Field.objects.count()
    
    for selected_employee in models.Employee.objects.all()[num_professors+1: num_professors+n+1]:
        try:        
            random_field_id = fake.random_int(min=1, max=num_fields)
            selected_field = models.Field.objects.all()[random_field_id-1]
            
            researcher = models.Researcher(
                employee=selected_employee,
                field=selected_field,
            )
            
            researcher.save()
        except:
            pass


def gen_research_object(n):
    
    for _ in range(n - models.Research.objects.count()):
        
        start_date_start = datetime.date(2010, 1, 1)
        start_date_end = datetime.date(2015, 12, 31)
        
        end_date_start = datetime.date(2016, 1, 1)
        end_date_end = datetime.date(2020, 12, 31)
        
        research = models.Research(
            title=fake.sentence(),
            start_date=fake.date_between(start_date=start_date_start, end_date=start_date_end),
            end_date=fake.date_between(start_date=end_date_start, end_date=end_date_end),
            search_area=fake.paragraph(),
            funding_source=fake.paragraph(),
            budget=random.randint(1000, 100000),
            description=fake.paragraph(),
            publication=fake.paragraph(),
            keywords=fake.words(),
            status=random.choice(["ToDo", "InProgress", "Done"]),
        )
        
        research.save()


def gen_professor_research_member_object(n):
    
    num_professors = models.Professor.objects.count()
    num_researches = models.Research.objects.count()
    
    
    for _ in range(n - models.ResearchMember.objects.filter(professor__isnull=False).count()):
        
        random_professor_id = fake.random_int(min=1, max=num_professors)
        selected_professor = models.Professor.objects.all()[random_professor_id-1]
        
        random_research_id = fake.random_int(min=1, max=num_researches)
        selected_research = models.Research.objects.all()[random_research_id-1]
        
        research_member = models.ResearchMember(
            professor=selected_professor,
            research=selected_research,
            role=fake.word()
        )
        research_member.save()  


def gen_researcher_research_member_object(n):
    
    num_researchers = models.Researcher.objects.count()
    num_researches = models.Research.objects.count()
    
    for _ in range(n - models.ResearchMember.objects.filter(researcher__isnull=False).count()):
        
        random_researcher_id = fake.random_int(min=1, max=num_researchers)
        selected_researcher = models.Researcher.objects.all()[random_researcher_id-1]
        
        random_research_id = fake.random_int(min=1, max=num_researchers)
        selected_research = models.Research.objects.all()[random_researcher_id-1]
        
        research_member = models.ResearchMember(
            researcher=selected_researcher,
            research=selected_research,
            role=fake.word()
        )
        research_member.save()  


def gen_schedule_object(n):
    
    for i in range(n - models.Schedule.objects.count()):
        
        random_time1 = fake.time()
        randon_time2 = fake.time()
        
        schedule = models.Schedule(
            day=random.choice(["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]),
            start_time=min(random_time1, randon_time2),
            end_time=max(random_time1, randon_time2),
        )
        schedule.save()


def gen_laboratory_object(n):
    
    num_employees = models.Employee.objects.count()
    num_schedules = models.Schedule.objects.count()
    
    for _ in range(n - models.Laboratory.objects.count()):        
                
        laboratory = models.Laboratory(
            name=fake.company(),
            equipments=fake.text(),
            capacity=random.randint(10, 1000),  
            budget=random.randint(1000, 100000),
        )
        
        laboratory.save()
        
        for i in range(random.randrange(1, 5)):
            random_employee_id = fake.random_int(min=1, max=models.Employee.objects.count())
            selected_employee = models.Employee.objects.all()[random_employee_id-1]
            laboratory.managers.add(selected_employee) 
        
        for i in range(random.randrange(1, 5)):
            random_schedule_id = fake.random_int(min=1, max=models.Schedule.objects.count())
            selected_schedule = models.Schedule.objects.all()[random_schedule_id-1]
            laboratory.schedules.add(selected_schedule)        
       

def gen_library_object(n):
    
    num_employees = models.Employee.objects.count()
    num_schedules = models.Schedule.objects.count()
    
    for _ in range(n - models.Library.objects.count()):        
                
        library = models.Library(
            name=fake.company(),
            capacity=random.randint(10, 1000),  
            books=random.randint(1000, 10000),
        )
        
        library.save()
        
        for i in range(random.randrange(1, 5)):
            random_employee_id = fake.random_int(min=1, max=models.Employee.objects.count())
            selected_employee = models.Employee.objects.all()[random_employee_id-1]
            library.managers.add(selected_employee) 
        
        for i in range(random.randrange(1, 5)):
            random_schedule_id = fake.random_int(min=1, max=models.Schedule.objects.count())
            selected_schedule = models.Schedule.objects.all()[random_schedule_id-1]
            library.schedules.add(selected_schedule)        
 
        
                              
WANTED_ADDRESS = 500
WANTED_EDUCATION = 1500
WANTED_PHONE_TYPE = 3000
WANTED_USER = 300
WANTED_BUILDING = 100
WANTED_FACULTY = 25
WANTED_DEPARTMENT = 100
WANTED_OFFICE = 300
WANTED_FIELD = 300
WANTED_EMPLOYEE = WANTED_USER
WANTED_PROFESSOR = 150
WANTED_RESEARCHER = 50
WANTED_RESEARCH = 100
WANTED_PROFESSOR_RESEARCH_MEMBER = 25
WANTED_RESEARCHER_RESEARCH_MEMBER = 25
WANTED_SCHEDULE = 1000
WANTED_LABORATORY = 10
WANTED_LIBRATY =  10

gen_address_object(WANTED_ADDRESS)
gen_education_object(WANTED_EDUCATION)
gen_phone_number(WANTED_PHONE_TYPE)
gen_user(WANTED_USER)
gen_building_object(WANTED_BUILDING)
gen_faculty_object(WANTED_FACULTY)
gen_department_object(WANTED_DEPARTMENT)
gen_office_object(WANTED_OFFICE)
gen_field_object(WANTED_FIELD)
gen_employee_object()
gen_professor_object(WANTED_PROFESSOR)
gen_researcher_object(WANTED_RESEARCHER)
gen_research_object(WANTED_RESEARCH)
gen_professor_research_member_object(WANTED_PROFESSOR_RESEARCH_MEMBER)
gen_researcher_research_member_object(WANTED_RESEARCHER_RESEARCH_MEMBER)
gen_schedule_object(WANTED_SCHEDULE)
gen_laboratory_object(WANTED_LABORATORY)
gen_library_object(WANTED_LIBRATY)


