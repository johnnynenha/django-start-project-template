# Django start project template

### Start new project

1. Clone template:
```
mkdir <project_name> && cd <project_name>
git clone https://github.com/johnnynenha/django-start-project-template.git . && rm -fr .git
```
2. Install and prepare virtual enviroment:
 ```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Create database
```
python manage.py migrate
```
4. Run DEV server
```
python manage.py runserver
```
