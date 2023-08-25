## Clone the repository
Open your terminal. Navigate to the directory where you want to store your project.
```bash
cd /path/to/the/project/storage/location
```
Clone the Github repository
```bash
git clone https://github.com/LordemarLTU/todo_ist.git
```

## Set up a virtual environment
Navigate to the project directory
```bash
cd /path/to/the/project/location
```
Create and activate a virtual environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS and Linux
python3 -m venv venv
source venv/bin/activate

## Set Up the 
```

## Install dependencies
Install Django and other project dependencies using **`pip`**.
```bash
pip install -r requirements.txt
```

## Set up Tailwind CSS
Install **`django-tailwind`**.
```bash
python manage.py tailwind install
```

## Set up the database
Create a PostgreSQL database and specify the login details in the **`core/settings.py`** file.
```bash
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': '...',
    'USER': '...',
    'PASSWORD': '...',
    'HOST': '...',
    'PORT': '...',
  }
}
```
Apply migrations to create the database schema
```bash
python manage.py makemigrations
python manage.py migrate
```

## Run the development server
Start the **Tailwind CSS** by running the following command in new terminal.
```bash
python manage.py tailwind start
```
Start the **Django** development server.
```bash
python manage.py runserver
```
Access your application in a web browser at **`http://127.0.0.1:8000/`**.

## Run tests
Run the tests by executing the command **`python manage.py test`** in the terminal.
