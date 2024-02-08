# Human Resource Management System
This is a django application for managing human resources

# Run
## Venv And Dependencies
Create a virtual env, then install dependencies with pip.

### Linux
```bash
python -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows
```powershell
python.exe -m virtualenv .venv
.\\venv\bin\activate
pip install -r requirements.txt
```

## Migration
```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Admin
```bash
python manage.py createsuperuser
Run The Test Server
python manage.py runserver
```

you can optionally specify a IP and port

# Defined URLS
Only admins have access to these urls
## admin
- `admin/`
Django's admin menu
## users
- `users/`
- `user/detail/<username>`
## personels
- `personels/`
- `personels/detail/<username>`
- `personels/vacation_requests/`
- `personels/payroll/`
- `personels/performance_review/`
## course
- `course/`
- `course/personel`
## department
- `department/`
- `department/buildings/`
- `department/director/<directory>/`
## resume
- `resume/`
- `resume/detail/<username>/`
## meeting
- `meeting/`
## interview
- `interview/`
- `interview/list/`
- `interview/stablisher/<username>/`
# ERD

# Normalization
Every table besides `buildings_has_departmend`, `personels_has_meetings` and `courses_has_personels` has an integer id as their primarly key and they don't have any other condidate keys. for those other three table mentioned they are all either created by only keys or there is the score value with has only functional dependancy `course_id personel_id -> score` and is only dependent to it's primarly key.

With arguments mentioned above we only need to prove this schema is in 3rd Normal Form.

There is no functional dependencies between non-prime atributes, so schema is in 3rd Normal Form and thus is in BCNF.
