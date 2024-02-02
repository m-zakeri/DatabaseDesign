# Academic staff management system

A back-end for managing academic staff in a university


## Diagram, Schemas and Models

### Diagram
[Digram in GoogleDrive](https://drive.google.com/file/d/1d3I85F1LHfmMR3n_x4SvY4TFgrGqdP1a/view?usp=sharing)

---

### Schemas
[Schema in GoogleDrive](https://drive.google.com/file/d/17Pfe_ew1TB88XZvp-da9OGawEj3wYojU/view?usp=drive_link)

---
### Models
#### Address
Represents an address entity.

Attributes:
- state (CharField): The state of the address.
- city (CharField): The city of the address.
- street (CharField): The street of the address.
- street_number (IntegerField, optional): The street number of the address.
- building_name (CharField, optional): The name of the building at the address.
- district (CharField): The district of the address.
- floor (IntegerField, optional): The floor number of the address.
- unit_number (IntegerField, optional): The unit number of the address.
- plate_number (CharField): The plate number of the address.
- postal_code (CharField): The postal code of the address.
- coordinate (CharField, optional): The coordinate of the address.
- note (TextField, optional): Additional notes related to the address.

#### Education
Represents an educational history entity.

Attributes:
- start_date (DateField): The start date of the education.
- graduation_date (DateField): The graduation date of the education.
- major (CharField): The major of the education.
- degree (CharField): The degree obtained.
- gpa (DecimalField): The GPA (Grade Point Average) achieved.
- institution_name (CharField): The name of the educational institution.
- institution_address (ForeignKey to Address): The address of the educational institution.

#### PhoneNumber
Represents a phone number entity.

Attributes:
- phone_number (CharField): The phone number.
- phone_type (CharField): The type of the phone number. Choices: "Mobile", "Work", "Home" (default:"Mobile").

#### Person
Represents a person entity.

Attributes:
- user (OneToOneField to User): The related user instance.
- persian_first_name (CharField): The Persian first name of the person.
- persian_last_name (CharField): The Persian last name of the person.
- gender (CharField): The gender of the person. Choices: "M" (Male), "F" (Female).
- date_of_birth (DateField): The date of birth of the person.
- nationality (CharField): The nationality of the person.
- national_code (CharField): The national code of the person.
- picture (ImageField, optional): The picture of the person.
- home_address (ForeignKey to Address, optional): The home address of the person.
- educations (ManyToManyField to Education): The educations associated with the person.
- phone_numbers (ManyToManyField to PhoneNumber): The phone numbers associated with the person.

Methods:
- get_age(): Method to calculate and return the age of the person.
- get_persian_first_name(): Method to return the Persian first name of the person.
- get_persian_last_name(): Method to return the Persian last name of the person.
- get_persian_full_name(): Method to return the full Persian name of the person.

#### Building
Represents a building entity.

Attributes:
- name (CharField): The name of the building.
- creation_date (DateField): The creation date of the building.
- floors (IntegerField): The number of floors in the building.
- capacity (IntegerField): The capacity of the building.
- rooms (IntegerField): The number of rooms in the building.
- address (ForeignKey to Address): The address of the building.

#### Faculty
Represents a faculty entity.

Attributes:
- name (CharField): The name of the faculty.
- creation_date (DateField): The creation date of the faculty.
- building (ForeignKey to Building): The building associated with the faculty.

#### Department
Represents a department entity.

Attributes:
- name (CharField): The name of the department.
- budget (IntegerField): The budget of the department.
- creation_date (DateField): The creation date of the department.
- faculty (ForeignKey to Faculty): The faculty associated with the department.

#### Office
Represents an office entity.

Attributes:
- phone_number (ForeignKey to PhoneNumber): The phone number associated with the office.
- department (ForeignKey to Department): The department associated with the office (optional).

#### Employee
Represents an employee entity.

Attributes:
- person (OneToOneField to Person): The related person instance.
- salary (IntegerField): The salary of the employee.
- hire_date (DateField): The date of hiring of the employee.
- office_hours (CharField): The office hours of the employee.
- status (CharField): The status of the employee.
- office (ManyToManyField to Office): The offices associated with the employee.
- is_committee (BooleanField): Indicates if the employee is part of a committee.

#### Field
Represents a field entity.

Attributes:
- name (CharField): The name of the field.
- department (ForeignKey to Department): The department associated with the field.
- head (OneToOneField to Professor): The head professor of the field (optional).

#### Professor
Represents a professor entity.

Attributes:
- employee (OneToOneField to Employee): The related employee instance.
- rank (CharField): The rank of the professor.
- field (ForeignKey to Field): The field associated with the professor.
- is_in_committee (BooleanField): Indicates if the professor is in a committee.

#### Researcher
Represents a researcher entity.

Attributes:
- employee (OneToOneField to Employee): The related employee instance.
- field (ForeignKey to Field): The field associated with the researcher.

#### Research
Represents a research entity.

Attributes:
- title (CharField): The title of the research.
- start_date (DateField): The start date of the research.
- end_date (DateField, optional): The end date of the research.
- search_area (TextField): The search area of the research.
- funding_source (TextField): The funding source of the research.
- budget (IntegerField): The budget allocated for the research.
- description (TextField): The description of the research.
- publication (TextField, optional): The publication related to the research.
- keywords (TextField): The keywords related to the research.
- status (CharField): The status of the research. Choices: "ToDo", "InProgress", "Done" (default: "ToDo").
- website (TextField, optional): The website related to the research.
- related_research (TextField, optional): Related research information.

#### ResearchMember
Represents a member associated with a research.

Attributes:
- professor (ForeignKey to Professor, optional): The professor associated with the research (optional).
- researcher (ForeignKey to Researcher, optional): The researcher associated with the research (optional).
- research (ForeignKey to Research): The research associated with the member.
- role (CharField): The role of the member.

#### Schedule
Represents a schedule entity.

Attributes:
- day (CharField): The day of the schedule. Choices: "Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri".
- start_time (TimeField): The start time of the schedule.
- end_time (TimeField): The end time of the schedule.

#### Laboratory
Represents a laboratory entity.

Attributes:
- name (CharField): The name of the laboratory.
- equipments (TextField): The equipments available in the laboratory.
- capacity (IntegerField): The capacity of the laboratory.
- budget (IntegerField): The budget allocated for the laboratory.
- managers (ManyToManyField to Employee): The managers associated with the laboratory.
- schedules (ManyToManyField to Schedule): The schedules associated with the laboratory.

#### Library
Represents a library entity.

Attributes:
- name (CharField): The name of the library.
- capacity (IntegerField): The capacity of the library.
- books (IntegerField): The number of books in the library.
- managers (ManyToManyField to Employee): The managers associated with the library.
- schedules (ManyToManyField to Schedule): The schedules associated with the library.

#### For more information check ```/admin/docs/models/```

## Features
1. An API over all entities for CRUD
2. Add authentication for create, update and delete accesses

## Create development environment
First install docker. Then run `docker compose up` command to start development server. There are ports you can test the website:
- http://localhost:8000 is for backend and api
- http://localhost:3000 is for frontend
- http://localhost:8080 is main website over nginx webserver

## Deployment


## Front End Design
[Figma Design Link](https://www.figma.com/file/mSOeJXGZW9ZBRveeLNKIM1/Search-Page?type=design&node-id=0%3A1&mode=design&t=s3j0DHQkXXjsSY4n-1)

