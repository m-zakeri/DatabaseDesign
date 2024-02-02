import random
import io


from googletrans import Translator
import requests
from faker import Faker
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile
from api.models import Address, Education, PhoneNumber, User, Person

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
    for i in range(n - len(Address.objects.all())):
        address = Address(
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
    num_address = len(Address.objects.all())
    for i in range(n - len(Education.objects.all())):
        random_address_id = fake.random_int(min=1, max=num_address)
        selected_address = Address.objects.get(pk=random_address_id)
        education = Education(
            start_date=fake.date(),
            graduation_date=fake.date(),
            major=random.choice(MAJORS),
            degree=random.choice(DEGREES),
            gpa=random.randrange(0, 10000) / 100,
            institution_name=random.choice(UNIVERSITIES),
            institution_address=selected_address,
        )
        education.save()


def gen_phone_number(n):
    for i in range(n - len(PhoneNumber.objects.all())):
        phone_number = PhoneNumber(
            phone_number=fake.phone_number(), phone_type=random.choice(PHONE_TYPE)
        )
        phone_number.save()


def gen_user(n):
    for i in range(n - len(User.objects.all())):
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
        person = Person(
            user=user,
            persian_first_name=persian_first_name,
            persian_last_name=persian_last_name,
            gender=random.choice(GENDERS),
            date_of_birth=fake.date(),
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


WANTED_ADDRESS = 1000
WANTED_EDUCATION = 2000
WANTED_PHONE_TYPE = 3000
WANTED_USER = 300

gen_address_object(WANTED_ADDRESS)
gen_education_object(WANTED_EDUCATION)
gen_phone_number(WANTED_PHONE_TYPE)
gen_user(WANTED_USER)