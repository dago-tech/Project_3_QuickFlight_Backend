# Turnow Project


API built in Django Rest Framework to cover the backend of this project

1. Create and build the virtual environment in bash console:

```sh
py -m venv venv
source venv/Scripts/activate
```
2. Create requirements.txt
```sh
pip freeze > requirements.txt
```
- Install dependencies:
```sh
pip install -r requirements.txt
```

3. Install Django rest Framework:

```sh
pip install djangorestframework
```
4. Create django project (do not create a new folder):

```sh
django-admin startproject core .
```

5. Create a new app for each database Entity and add it to INSTALLED_APPS in settings.py:
```sh
py manage.py startapp turns
```

6. Try the server:
```sh
py manage.py runserver
```

7. Create a new database in PostgreSQL (PgAdmin), and install the adapter of postgresql for Django:

```sh
pip install psycopg2
```

8. Modify settings.py, update DATABASES:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'TurnowDB',
        'USER': 'postgres',
        'PASSWORD': '', # General postgresql password
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}
```

![Alt text](../img/PostgreSQLServerProps.JPG)

9. Make migrations:

```sh
py manage.py makemigrations
py manage.py migrate
```

10. Create models and serializers in every app.

11. Add the following statement at settings.py:

```sh
AUTH_USER_MODEL = 'users.CustomUser'
```
12. Make migrations, if there is any problem, delete python migrations files and the database.

13. Create a superuser

```sh
py manage.py createsuperuser
```
username: daniel
email: a@a.com
password: abcd9874

username: Cristiano
email: b@b.com
password: qazxsw1234

username: cuadrado
email: b@b.com
password: abcd9874

- Create visualizations for models in panel admin updating admin.py files.

14. Create the views, urls and add 'rest_framework' to INSTALLED_APPS.


## Subiendo a Github

1. Creo nuevo Repo en Github o Gitlab
2. Creo repositorio local en mi carpeta local del proyecto
```sh
git init --initial-branch=main
```
3. Hago mi enlace con el repositorio remoto al que quiero subir el proyecto
```sh
git remote add origin https://github.com/dago-tech/Project_3_QuickFlight_Backend.git
```
4. Agrego todos los archivos del proyecto al area de stage
```sh
git add .
```
5. Hago commit para enviar mis archivos al repositorio local
```sh
git commit -m "Deploy1"
```
6. Hago push para enviar mi repositorio local al repo remoto
```sh
git push -u origin main
```
- Si obtengo la respuesta:
```
Updates were rejected because the remote contains work that you do
not have locally. This is usually caused by another repository pushing
to the same ref. You may want to first integrate the remote changes
(e.g., 'git pull ...') before pushing again.
See the 'Note about fast-forwards' in 'git push --help' for details.
```
- Este error se debe a que lo que está en el repositorio remoto es diferente a lo del local, así que debo integrarlos. Se recomienta hacer un git pull que traiga el repo remoto hacia el local

- Verifico que el repo remoto sea 'origin' y que me muestre su URL, con:

```sh
git remote
git remote -v
```

- (origin es simplemente el nombre predeterminado que recibe el repositorio remoto principal contra el que trabajamos.)

7. Hago git pull intentando traer lo del repo remoto, en este caso hay error porque los commits del repo local son diferentes a los del repo remoto:

```sh
git pull origin main 
(fatal: refusing to merge unrelated histories)
```
8. Agrego una instruccion adicional a git para permitir historias no relacionadas:
```sh
git pull origin main --allow-unrelated-histories
```
9. Finalmente puedo hacer el push con exito:
```sh
git push origin main
```


## API Schema and documentation Generation

Un Schema es metadata que detalla cómo la data está estructurada. Metadata = data about data.

Para generar el Schema de nuestro proyecto, instalamos:

```sh
pip install PyYAML
```

- En nuestro archivo de urls.py general importamos:
```sh
from rest_framework.schemas import get_schema_view
```

- Y agregamos una ruta:

```py
path('schema', get_schema_view(
        title="BlogAPI",
        description="API for the BlogAPI",
        version="1.0.0"
    ), name='openapi-schema'),
```

Ademas, debemos instalar:

```sh
pip install uritemplate
```
- Ahora en la ruta /schema podemos visualizar el schema de nuestro proyecto.

![Alt text](img/Schema1.jpg)


### Doc Generator for Django Rest Framework

- Django Rest Swagger
- Swagger-ui
- drf-yasg
- Redoc

En este caso vamos a generar nuestra documentacion en Swagger-ui, así que importamos lo siguiente en urls.py general:
```py
from rest_framework.documentation import include_docs_urls
```

Agregamos el path:

```py
path('docs/', include_docs_urls(title='BlogAPI')),
```
- Y también debemos instalar coreapi
```sh
pip install coreapi
```
'coreapi' es una herramienta versátil que se utiliza para interactuar con APIs web basadas en documentación interactiva, explorar rutas de API, realizar pruebas de API y generar documentación. En el contexto de Django, coreapi se usa como parte de Django REST framework para mejorar la documentación y la interacción con las APIs web creadas con esta biblioteca.

- En el archivo settings.py agregamos:

```py
REST_FRAMEWORK = { 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema' }
```

- Ahora tenemos con el link /docs la documentacion con la cual podemos interactuar con la API


## CORS

- Instalamos la libreria django-cors-headers, esto permite solicitudes de navegador desde otros origenes.

```sh
pip install django-cors-headers
```

- En el archivo settings.py agregamos corsheaders a las INSTALLED APPS, agregamos el middleware y los origenes colocando la palabra localhost ya que cuando accedemos por el navegador a la app de react, este muestra localhost y no 127.0.0.1: 

```py
"corsheaders.middleware.CorsMiddleware",

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
]
```