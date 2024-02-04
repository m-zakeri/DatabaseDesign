
# Research Laboratory Managment System(RLMS)

## Overview

This project is a University project aimed at implementing a Research Laboratory Management System (RLMS) database using a Django backend and a user interface powered by the admin-volt library. The RLMS database will be utilized to manage and organize resources for Research purposes.

## Features

- **Admin Panel CRUD Operations:**
  - Superuser or admin can perform CRUD (Create, Read, Update, Delete) operations on the database using the admin panel.

- **User Management:**
  - Admin can create users with different access privileges to control their views and interactions with the database.

- **User Dashboard:**
  - Users can access a personalized dashboard where they can view and manage research projects, including details and team members.

- **Responsive UI:**
  - The user interface is designed to be responsive, ensuring a seamless experience across various devices.

- **Login and Registration:**
  - Full-fledged login and registration panels for secure access to the system.

## Technologies Used

- **Backend Framework:** Django
- **ORM (Object-Relational Mapping):** Django ORM
- **User Interface Library:** admin-volt
- **Database:** Mysql (for development, can be configured for other databases like PostgreSQL in production)


## Database ERD and Schema
You can find ERD of prject in:
- *Backend/Research Laboratory Management ERD.png* 
- *Research Laboratory Management Tables.jpg*

## Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Raeinf/DatabaseDesign/tree/main/projects/RLMS/Backend
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Configure Database Settings:**

   Edit the `RLMS/settings.py` file and update the `DATABASES` settings according to your database configuration.

6. **Apply Database Migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

7. **Create a Superuser Account:**
    ```bash
    python manage.py createsuperuser

8. **Run the Development Server:**
    ```bash
    python manage.py runserver <ip><port>

(For Windows, use py instead of python.)

9. **Enjoy Running the project**


## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](https://opensource.org/licenses/MIT) file for details.

## Project Developers

- [Vahid Esmaeeli](https://github.com/VahidEMA)
- [Raein Farahmandkhah](https://github.com/RaeinF)
- [Ghazal Alirezaei](https://github.com/ghazalAlrz)
