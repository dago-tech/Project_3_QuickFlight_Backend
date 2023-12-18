# Proyecto Backend de la app QuickFlight

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" alt="Python" width="130" height="60"/> <img src="https://www.thetestspecimen.com/img/django-initial/django-rest-logo-960w.jpg" alt="django rest framework" width="130" height="60"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain-wordmark.svg" alt="postgresql" width="65" height="65"/>

---

Esta API REST busca servir la información para la aplicación QuickFlight la cual va a permitir crear vuelos de avión así como la solicitud de reservas de vuelos basados en datos como el origen, destino, fechas de partida y llegada, y por último la generación de estadísticas.

Esta API usa una base de datos PostgreSQL alojada en un servidor en la nube del sitio web https://render.com/.

Se utilizan peticiones HTTP y las respuestas son recibidas en formato JSON.

- Se desplegó API en un servidor del sitio web Heroku obteniendo la siguiente  dirección donde se puede navegar a través de sus endpoints:

https://quickflight-ffbdc0233c84.herokuapp.com/api/flights


---

### Documentacion de API:
- Modo dev: http://localhost:8000/docs/
- Modo producción: https://quickflight-ffbdc0233c84.herokuapp.com/docs/

![Alt text](<docs/img/API Documentation.jpg>)

- Ejemplo de endpoint para solicitar el listado de vuelos creados: https://quickflight-ffbdc0233c84.herokuapp.com/api/flights/

- Visualización de solicitud brindada por la librería de Django Rest Framework:

![Alt text](<docs/img/API DRF.jpg>)

---

### Versiones usadas en desarrollo

- Sistema operativo local: Windows 10
- Entorno de desarrollo: Visual Studio Code
- Versión de Python: 3.11.1
- Versión base de datos PostgreSQL: 14
- Version Docker: 4.26.1

---


### Guía de descarga a local

- Se debe tener instalado Python y Git

1. Abre la terminal o línea de comandos en el computador donde deseas descargar el proyecto.

2. Navega al directorio donde deseas almacenar el repositorio.

3. Ejecuta el siguiente comando de Git para clonar el repositorio a la carpeta actual, esto copiará todas las ramas:
```sh
git clone https://github.com/dago-tech/Project_3_QuickFlight_Backend.git
```

4. Muévete a la rama main:
```sh
git checkout main
```
5. Crea y activa un entorno virtual en la carpeta del proyecto:

```sh
py -m venv venv
```
En powershell
```sh
venv\Scripts\activate
```
En bash
```sh
source venv/Scripts/activate
```

6. Instala todas las dependencias:
```sh
pip install -r requirements.txt
```

7. Como la base de datos corre en la nube ya se le ha realizado migraciones previamente y estos comandos no son necesarios, pero si creas la base de datos en local se deben ajustar los parametros de la base de datos en el archivo settings.py y ejecutar:

```sh
py manage.py makemigrations
py manage.py migrate
```

8. Correr el servidor de desarrollo:
```sh
py manage.py runserver
```

9. Ya se pueden hacer solicitudes HTTP a este servidor, por ejemplo, usando:
```sh
Metodo: GET
http://localhost:8000/api/flights/
```

---

### Docker

De esta aplicación también se puede generar un contenedor utilizando el archivo dockerfile incluido en la raiz del proyecto usando los siguientes comandos:

- Arrancamos Docker desktop

- Nos ubicamos en la raíz del proyecto donde se encuentra el dockerfile y construimos la imagen del contenedor con el nombre que desee:

```sh
docker build -t nombre_de_la_imagen .
```
- Corremos el contenedor y exponemos el puerto 8000 del host y del contenedor, lo creamos con el nombre que le quedamos dar:
```sh
docker run -p 8000:8000 --name nombre_del_contenedor nombre_de_la_imagen
```
- Ahora, con el contenedor corriendo, podemos generar peticiones HTTP por medio del navegador y el localhost:8000

![Alt text](docs/img/Docker1.jpg)