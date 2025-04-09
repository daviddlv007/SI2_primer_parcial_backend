Datos utiles del proyecto:

1. Arbol de archivos:

django_proyect/
│
├── manage.py
├── django_proyect/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── django_app_1/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── apps.py
│   ├── admin.py
│   ├── tests.py
│   ├── urls.py
│   ├── serializers.py
│   └── migrations/
│
├── requirements.txt
├── .gitignore
└── manage.py

2. .gitignore:

# Ignorar entorno virtual
venv/

# Ignorar base de datos SQLite
db.sqlite3

# Ignorar archivos de compilación de Python
*.pyc
__pycache__/

# Ignorar archivos de configuración del editor (si usas VSCode)
.vscode/

# Ignorar logs
*.log


3. requirements.txt:

asgiref==3.8.1
attrs==25.3.0
Django==5.2
django-cors-headers==4.7.0
djangorestframework==3.16.0
djangorestframework_simplejwt==5.5.0
drf-spectacular==0.28.0
inflection==0.5.1
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
PyJWT==2.9.0
PyYAML==6.0.2
referencing==0.36.2
rpds-py==0.24.0
sqlparse==0.5.3
tzdata==2025.2
uritemplate==4.1.1
