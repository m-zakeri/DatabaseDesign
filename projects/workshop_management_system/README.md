# Workshop Management System

An educational platform offering a diverse range of online and offline courses for sale, covering various fields of
knowledge.

## Objectives

- Creating a space to sell and introduce training courses by professors and different specialties .

- Improving the level of knowledge and skills of people in many fields and at any level of experience .

- Creating opportunities for direct communication between professors and students .

- Support for offline training courses held in different places .

## Advantages

- Access to a diverse range of educational courses in various fields.
- Expert instructors and experienced guides in the teaching domain.
- Opportunity to participate in offline courses at different city locations.


## Diagram
[Entity-Relationship Diagram](https://drive.google.com/drive/folders/1LMcZY5Zg24eaa8kswAyzNHbj9Bb49H-u?usp=sharing)


## Features

### Course Interactions

#### Likes

- **Like Courses:**
  - Users can like (or favorite) courses to bookmark them or show interest.

#### Comments

- **Comment on Courses:**
  - Users can leave comments on each course to share their thoughts or ask questions.

#### Ratings

- **Rate Courses:**
  - Users can give ratings to courses to provide feedback on their experience.

### Q&A Section

- **Ask Questions:**
  - Users can ask questions related to each course.

- **Answer Questions:**
  - Users can answer questions asked by other users.

### User Engagement

#### User Profiles

- **View Liked Courses:**
  - Users can view a list of courses they have liked.

- **View Comments:**
  - Users can see comments they have made on courses.

- **View Ratings:**
  - Users can see the ratings they have given to courses.
 

## Getting Started

1. **Visit the website:**
    - To explore courses and tutorials, visit [Eduport](https://www.Eduport.com).


2. **Sign Up and Log In:**
    - To access full features, sign up or log in to your user account.


3. **Search and Filter:**
    - Use the site's search and filter features to find courses that match your preferences.


4. **Purchase and Join Courses:**
    - With a single click, easily participate in your preferred courses and benefit from educational resources.

## Authentication

The system supports multiple authentication methods for both login and registration.
The system provides a password reset functionality that requires users to enter their email address to initiate the
process.

### Login

1. **Email and Password:**
    - Users can log in using their email and password.


2. **Username and Password:**
    - Users can log in using their username and password.


3. **Google Sign-In:**
    - Users can log in using their Google accounts.

### Registration

1. **Email Verification:**
    - After registration, a five-digit verification code is sent to the user's email.
    - Users must enter the code to complete the email verification process.


2. **Google Sign-Up:**
    - Users can register by signing up with their Google accounts.
    - Click on the "Sign Up with Google" button and follow the prompts to complete the registration process.

### Password Reset

1. **Forgot Password:**
    - Users who forget their passwords can click on the "Forgot Password" link on the login page.


2. **Enter Email:**
    - Users need to enter their email address associated with their account.


3. **Email Verification:**
    - A link for resetting the password is sent to the user's email.


4. **Reset Password:**
    - Users click on the link and are directed to a page where they can enter a new password.

## Installation and Setup

### 1. Install Python and Virtual Environment

Make sure Python is installed on your system. You can download it from [python.org](https://www.python.org/). After
that, follow these steps:

```bash
# Install virtualenv
pip install virtualenv

# Create a virtual environment
python -m venv venv

# Activate the virtual environment (Windows)
venv\Scripts\activate

# Activate the virtual environment (Unix or MacOS)
source venv/bin/activate 
```

### 2. Clone the Project

```bash
# Clone the project from the repository
git clone https://github.com/rezasharafdini/DatabaseDesign.git
cd DatabaseDesign/project/workshop_management_system
```

### 3. Install Dependencies

```bash
# Install the project dependencies
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
# Apply migrations to set up the database
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Development Server

```bash
# Run the development server
python manage.py runserver
```

