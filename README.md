# MozioProject

The project contains supervisor config file and gunicorn bash which were used to host the application.

### What does the application do?
This application has APIs to create, retrieve, update and delete companies. Each company can create, retrieve, update and delete service areas using geo_json. Application can also search which service_area offers service to a particular geo_json Point provided the latitude and longitude.
To perform update, delete company and operations on service area one would need access token which can only be rendered from successful login.

### Tech

MozioProject uses a number of open source projects to work properly:

* [Python] - Python is an easy to learn, powerful programming language!
* [Django] - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Django Rest Framework] - Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [Shapely] - Manipulation and analysis of geometric objects in the Cartesian plane.
* [Psycopg] - PostgreSQL database adapter for Python
* [Redis] - Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker.

And of course MozioProject itself is open source with a [public repository][dill]
 on GitHub.

### Installation

MozioProject requires Python3.6 or above to run.
```
Clone the repo
$ virtualenv -p python3 venv      # Create virtualenv
$ source venv/bin/activate        # Activate virtualenv
$ pip install -r requirements.txt # Install python modules
Edit database settings in mozio/settings.py
$ python manage.py migrate
```

### Run Server
```
Start Redis
Activate virtualenv
$ python manage.py runserver [IP]:[PORT]
```
### Postman Collection Link

Here is a link to postman collection: [Postman]


[//]: # 
   [dill]: <https://github.com/jinayshah86/mozio>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [Python]: <https://docs.python.org/3/>
   [Django]: <https://www.djangoproject.com/>
   [Django Rest Framework]: <http://www.django-rest-framework.org/>
   [Django Rest Swagger]: <https://django-rest-swagger.readthedocs.io/en/latest/>
   [Psycopg]: <http://initd.org/psycopg/docs/>
   [Redis]: <https://redis.io/>
   [postman]: <https://www.getpostman.com/collections/ebd614c51834ac2a9037>
   [Shapely]: <https://github.com/Toblerity/Shapely>

