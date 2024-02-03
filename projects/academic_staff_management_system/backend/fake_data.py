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
    for i in range(n - len(models.Address.objects.all())):
        try:
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
        except:
            pass


def gen_education_object(n):
    
    num_address = len(models.Address.objects.all())
    
    for _ in range(n - len(models.Education.objects.all())):
        
        random_address_id = fake.random_int(min=1, max=num_address)
        selected_address = models.Address.objects.get(pk=random_address_id)
        
        start_date_start = datetime.date(2010, 1, 1)
        start_date_end = datetime.date(2015, 12, 31)
        
        graduation_date_start = datetime.date(2016, 1, 1)
        graduation_date_end = datetime.date(2020, 12, 31)
        
        
        education = models.Education(
            start_date=fake.date_between(start_date=start_date_start, end_date=start_date_end),
            graduation_date=fake.date_between(start_date=graduation_date_start, end_date=graduation_date_end),
            major=random.choice(MAJORS),
            degree=random.choice(DEGREES),
            gpa=random.randrange(0, 2000) / 100,
            institution_name=random.choice(UNIVERSITIES),
            institution_address=selected_address,
        )
        education.save()


def gen_phone_number(n):
    for _ in range(n - len(models.PhoneNumber.objects.all())):
        phone_number = models.PhoneNumber(
            phone_number=fake.phone_number(), phone_type=random.choice(PHONE_TYPES)
        )
        phone_number.save()


def gen_user(n):
    for _ in range(n - len(User.objects.all())):
        print(f"We construct user {i}")
        persian_first_name = persian_fake.first_name()
        persian_last_name = persian_fake.last_name()
        user = User(
            username=fake.pystr(),
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
        
        
        random_address_id = random.randrange(len(Address.objects.all()))
        random_address = Address.objects.get(pk=random_address_id)
        
        start_date = datetime.date(1970, 1, 1)
        end_date = datetime.date(2000, 12, 31)
        
        person = Person(
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
        
        for j in range(random.randrange(5)):
            random_phone_number_id = random.randrange(1, len(PhoneNumber.objects.all()))
            random_phone_number = PhoneNumber.objects.get(pk=random_phone_number_id)
            person.phone_numbers.add(random_phone_number)
        
        for j in range(random.randrange(5)):
            random_education_id = random.randrange(1, len(Education.objects.all()))
            random_education = Education.objects.get(pk=random_education_id)
            person.educations.add(random_education)


def gen_building_object(n):
    num_address = len(models.Address.objects.all())
    
    for _ in range(n - len(models.Building.objects.all())):
        
        random_address_id = fake.random_int(min=1, max=num_address)
        selected_address = models.Address.objects.get(pk=random_address_id)
        
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

        
def gen_faculty_object(n):
    
    num_buildings = len(models.Building.objects.all())
    
    for _ in range(n - len(models.Faculty.objects.all())):
        
        random_building_id = fake.random_int(min=1, max=num_buildings)
        selected_building = models.Building.objects.get(pk=random_building_id)
        
        start_date = datetime.date(2015, 1, 1)
        end_date = datetime.date(2016, 12, 31)
        
        faculty = models.Faculty(
            name=fake.name(),
            creation_date=fake.date_between(start_date=start_date, end_date=end_date),
            building=selected_building,
        )
        faculty.save()
        
        
def gen_department_object(n):
    
    num_faculties = len(models.Faculty.objects.all())
    
    for _ in range(n - len(models.Department.objects.all())):
        
        random_faculty_id = fake.random_int(min=1, max=num_faculties)
        selected_faculty = models.Faculty.objects.get(pk=random_faculty_id)
        
        start_date = datetime.date(2017, 1, 1)
        end_date = datetime.date(2018, 12, 31)
        
        department = models.Department(
            name=fake.word(),
            budget=random.randint(10000, 1000000), 
            creation_date=fake.date_between(start_date=start_date, end_date=end_date),
            faculty=selected_faculty,
        )
        department.save()


def gen_office_object(n):
    
    num_phone_numbers = len(models.PhoneNumber.objects.filter(phone_type="Work"))
    num_departments = len(models.Department.objects.all())
    
    for _ in range(n - len(models.Office.objects.all())):
        
        random_phone_number_id = fake.random_int(min=1, max=num_phone_numbers)
        selected_phone_number = models.PhoneNumber.objects.get(pk=random_phone_number_id)
        
        random_department_id = fake.random_int(min=1, max=num_departments)
        selected_department = models.Department.objects.get(pk=random_department_id)
        
        office = models.Office(
            phone_number=selected_phone_number,
            department=selected_department
        )
        office.save()


def gen_field_object(n):
    
    num_departments = len(Department.objects.all())
    
    for _ in range(n - len(Field.objects.all())):
        
        random_department_id = fake.random_int(min=1, max=num_departments)
        selected_department = models.Department.objects.get(pk=random_department_id)
        
        
        field = Field(
            name=fake.word(),
            department=selected_department,
        )
        field.save()


def gen_employee_object(n):
    
    num_persons = len(models.Person.objects.all())
    num_offices = len(models.Office.objects.all())
    
    for _ in range(n - len(models.Employee.objects.all())):
        
        random_person_id = fake.random_int(min=1, max=num_persons)
        selected_person = models.Person.objects.get(pk=random_person_id)
        
        random_office_id = fake.random_int(min=1, max=num_offices)
        selected_office = models.Office.objects.get(pk=random_office_id)
        
        office_hours = f"{fake.time()}-{fake.time()}"
        
        
        employee = models.Employee(
            person=selected_person,
            salary=random.randint(10000, 1000000),
            hire_date=selected_person.user.date_joined.date(),
            office_hours=office_hours,
            status=random.choice(['Full-time', 'Part-time']),
            office=selected_office,
            is_committee=random.choice([True, False]) 
        )
        
        employee.save()
        

def gen_professor_object(n):
    
    num_employees = len(models.Employee.objects.all())
    num_fields = len(models.Field.objects.all())
    
    for _ in range(n - len(Professor.objects.all())):
        
        random_employee_id = fake.random_int(min=1, max=num_employees)
        selected_employee = models.Employee.objects.get(pk=random_employee_id)
        
        random_field_id = fake.random_int(min=1, max=num_fields)
        selected_field = models.Field.objects.get(pk=random_field_id)
        
        professor = Professor(
            employee=selected_employee,
            rank=random.choice(["Instructor", "Assistant Professor", "Associative Professor", "Full Professor"]),
            field=selected_field,
            is_in_committee=fake.boolean(chance_of_getting_true=50)
        ) 
        professor.save()


def gen_researcher_object(n):
    
    num_employees = len(models.Employee.objects.all())
    num_fields = len(models.Field.objects.all())
    
    for _ in range(n - len(models.Researcher.objects.all())):
        
        random_employee_id = fake.random_int(min=1, max=num_employees)
        selected_employee = models.Employee.objects.get(pk=random_employee_id)
        
        random_field_id = fake.random_int(min=1, max=num_fields)
        selected_field = models.Field.objects.get(pk=random_field_id)
        
        researcher = Researcher(
            employee=selected_employee,
            field=selected_field,
        )
        
        researcher.save()


def gen_research_object(n):
    
    for _ in range(n - len(Research.objects.all())):
        
        start_date_start = datetime.date(2010, 1, 1)
        start_date_end = datetime.date(2015, 12, 31)
        
        end_date_start = datetime.date(2016, 1, 1)
        end_date_end = datetime.date(2020, 12, 31)
        
        research = Research(
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
    
    num_professors = len(models.Professor.objects.all())
    num_researches = len(models.Research.objects.all())
    
    for _ in range(n - len(models.ResearchMember.objects.all())):
        
        random_professor_id = fake.random_int(min=1, max=num_employees)
        selected_professor = models.ResearchMember.objects.get(pk=random_professor_id)
        
        random_research_id = fake.random_int(min=1, max=num_employees)
        selected_research = models.Research.objects.get(pk=random_research_id)
        
        research_member = models.ResearchMember(
            professor=selected_professor,
            research=selected_research,
            role=fake.word()
        )
        research_member.save()  


def gen_researcher_research_member_object(n):
    
    num_researchers = len(models.Researcher.objects.all())
    num_researches = len(models.Research.objects.all())
    
    for _ in range(n - len(ResearchMember.objects.all())):
        
        random_researcher_id = fake.random_int(min=1, max=num_employees)
        selected_researcher = models.Researcher.objects.get(pk=random_professor_id)
        
        random_research_id = fake.random_int(min=1, max=num_employees)
        selected_research = models.Research.objects.get(pk=random_research_id)
        
        research_member = models.ResearchMember(
            researcher=selected_researcher,
            research=selected_research,
            role=fake.word()
        )
        research_member.save()  


def gen_schedule_object(n):
    
    for i in range(n - len(models.Schedule.objects.all())):
        
        random_time1 = fake.time()
        randon_time2 = fake.time()
        
        schedule = models.Schedule(
            day=random.choice(["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]),
            start_time=min(random_time1, randon_time2),
            end_time=max(random_time1, randon_time2),
        )
        schedule.save()


def gen_laboratory_object(n):
    
    num_employees = len(models.Employee.objects.all())
    num_schedules = len(models.Schedule.objects.all())
    
    for _ in range(n - len(models.Laboratory.objects.all())):
        random_employee_id = fake.random_int(min=1, max=num_employees)
        selected_employee = models.Employee.objects.get(pk=random_employee_id)
        
        
        radnom_schedule_id = fake.random_int(min=1, max=num_schedules)
        selected_schedule = models.Schedule.objects.get(pk=radnom_schedule_id)
        
                
        laboratory = Laboratory(
            name=fake.company(),
            equipments=fake.text(),
            capacity=random.randint(10, 1000),  
            budget=random.randint(1000, 100000),
            managers=selected_employee,
            schedules=selected_schedule
        )
        
        laboratory.save()


def gen_library_object(n):
    num_employees = len(models.Employee.objects.all())
    num_schedules = len(models.Schedule.objects.all())
    
    for _ in range(n - len(models.Library.objects.all())):
        random_employee_id = fake.random_int(min=1, max=num_employees)
        selected_employee = models.Employee.objects.get(pk=random_employee_id)
        
        radnom_schedule_id = fake.random_int(min=1, max=num_schedules)
        selected_schedule = models.Schedule.objects.get(pk=radnom_schedule_id)
        
        library = models.Library(
            name=fake.company(),
            capacity=random.randint(10, 100),
            books=random.randint(1000, 10000),
            managers=selected_employee,
            schedules=selected_schedule
        )
        library.save()
        
        
                              
WANTED_ADDRESS = 1000
WANTED_EDUCATION = 2000
WANTED_PHONE_TYPE = 3000
WANTED_USER = 300
WANTED_BUILDING = 100
WANTED_FACULTY = 25
WANTED_DEPARTMENT = 100
WANTED_OFFICE = 500
WANTED_FIELD = 400
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
gen_building_object(1)
gen_education_object(WANTED_EDUCATION)
gen_phone_number(WANTED_PHONE_TYPE)
gen_user(WANTED_USER)
gen_building_object(WANTED_BUILDING)
gen_faculty_object(WANTED_FACULTY)
gen_department_object(WANTED_DEPARTMENT)
gen_office_object(WANTED_OFFICE)
gen_field_object(WANTED_FIELD)
gen_employee_object(WANTED_EMPLOYEE)
gen_professor_object(WANTED_PROFESSOR)
gen_researcher_object(WANTED_RESEARCHER)
gen_research_object(WANTED_RESEARCH)
gen_professor_research_member_object(WANTED_PROFESSOR_RESEARCH_MEMBER)
gen_researcher_research_member_object(WANTED_RESEARCHER_RESEARCH_MEMBER)
gen_laboratory_object(WANTED_LABORATORY)
gen_library_object(WANTED_LIBRATY)


