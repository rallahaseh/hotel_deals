# Expedia Coding Exercise
- Create a very simple site that consumes offer svc API as a server-side call and displays deals in an appealing manner.
- [About.md](https://github.com/rallahaseh/hotel_deals/blob/master/ABOUT.md)
- **[Website](https://hotels-deals-demo.herokuapp.com/)**

#### Language
<img src="https://raw.githubusercontent.com/github/explore/6c6508f34230f0ac0d49e847a326429eefbfc030/topics/python/python.png" width="200" height="200" />

#### Framework
<img src="https://raw.githubusercontent.com/github/explore/6c6508f34230f0ac0d49e847a326429eefbfc030/topics/django/django.png" width="200" height="200" />

## Files
```
.
+-- Procfile
+-- Pipfile
+-- requirements.txt
+-- runtime.txt
+-- manage.py
+-- hotel_deals
|   +-- settings.py
|   +-- urls.py
|   +-- wsgi.py
|   +-- __init__.py
+-- main
|	+-- static
|	|	+-- css	
|	|	|	+-- style.css
|	+-- templates
|	|	+-- hotel_deals	
|	|	|	+-- index.html
|   +-- apps.py
|   +-- form.py
|   +-- models.py
|   +-- services.py
|   +-- urls.py
|   +-- views.py
+-- db.sqlite3

```

## Setup Local Sandbox

Requirements:
- [HomeBrew](https://brew.sh/)
- [Pip & Python 3.6](https://docs.brew.sh/Homebrew-and-Python)
- [Django 2.0.5](https://www.djangoproject.com/download/)
- [VirtualEnv](https://virtualenv.pypa.io/en/stable/)
- [Django Requests](http://docs.python-requests.org/en/master/user/install/)

After you install the required list.
1.  We will be using a new directory `hotels` from your home directory.
> $ mkdir hotels  
	$ cd hotel
2. Create a virtualenv called `myvenv`.
>$ python -m venv myvenv
3. Move the project to your main web root directory.
for example:
 > $ pwd  
	/WWW/django_projects/hotel_deals
4. Run the server
>python manage.py runserver
