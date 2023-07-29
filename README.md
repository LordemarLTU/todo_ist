# Instrukcija

 1. Parsisiųsti projektą iš Github ir atidaryti su Visual Studio Code programa.
 2. Programoje atidaryti terminalą ir sukurti virtual environment, terminale įvykdant komandą "python -m venv virtualEnvironment".
 3. Aktyvuoti sukurtą virtual environment, terminale įvykdant "virtualEnvironment\Scripts\activate" komandą.
 4. Instaliuoti visus reikalingus paketus terminale įvykdant komandą "pip install -r requirements.txt".
 5. Sukurti PostgreSQL duomenų bazę ir nurodyti prisijungimo duomenis core/settings.py faile (NAME, USER, PASSWORD, HOST, PORT laukuose [89-98 eil.])
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
 6. Sukurti duomenų bazėje reikalingas lenteles, termnale įvydant komandą "python manage.py migrate".
 7. Instaliuoti Tailwind CSS terminale įvykdant "python manage.py tailwind install".
 8. Paleisti Tailwind terminale įvykdant komandą "python manage.py tailwind start".
 9. Paleisti projektą naujame terminale įvykdant komandą "python manage.py runserver" arba klaviatūroje paspaudus F5, paleistas projektas matomas naršyklėje "http://127.0.0.1:8000/" nuoroda.

Paleisti testus terminale įvykdant komandą "python manage.py test".
