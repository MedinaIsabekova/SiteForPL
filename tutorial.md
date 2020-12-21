## Tutorial for Site in Django
First, we import **django** library in laptop console and pycharm console

```
$ pip install django
```

Then, We create the project inside the pytharm terminal

```
$ django-admin startproject Sitebybye
```

Then, we can see the new Directory "Sitebybye"
Inside this Directory, we can see new file "manage.py"
This is our main file in our project

Also, manage.py is our local server

Was created new Directory the same as previus one
Let’s look at what startproject created:

```
Sitebybye/
    manage.py
    Sitebybye/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

These files are:

The outer Sitebybye/ root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
The inner Sitebybye/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. Sitebybye.urls).
Sitebybye/__init__.py: An empty file that tells Python that this directory should be considered a Python package.
Sitebybye/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
Sitebybye/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
Sitebybye/asgi.py: An entry-point for ASGI-compatible web servers to serve your project.
Sitebybye/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project.

Let’s verify your Django project works. Change into the outer mysite directory, if you haven’t already, and run the following commands:

```
$ python manage.py runserver
```
You’ll see the following output on the command line:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 21, 2020 - 16:29:21
Django version 3.1.4, using settings 'honey.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Now that your environment – a “project” – is set up, you’re set to start doing work.

Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

```
$ python manage.py startapp honey
```

That’ll create a directory honey, which is laid out like this:

```
honey/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

To create a URLconf in the polls directory, create a file called urls.py. Your app directory should now look like:

```
honey/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    urls.py
    views.py
```
In the honey/urls.py file include the following code:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

Also we created the Directory "main" in honey directory.

The next step is to point the root URLconf at the honey.urls module. In Sitebybye/urls.py, add an import for django.urls.include and insert an include() in the urlpatterns list, so you have:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

The include() function allows referencing other URLconfs. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.


Now, open up Sitebybye/settings.py. It’s a normal Python module with module-level variables representing Django settings.

By default, the configuration uses SQLite. If you’re new to databases, or you’re just interested in trying Django, this is the easiest choice. SQLite is included in Python, so you won’t need to install anything else to support your database. When starting your first real project, however, you may want to use a more scalable database like PostgreSQL, to avoid database-switching headaches down the road.

While you’re editing Sitebybye/settings.py, set TIME_ZONE to your time zone.

Also, note the INSTALLED_APPS setting at the top of the file. That holds the names of all Django applications that are activated in this Django instance. Apps can be used in multiple projects, and you can package and distribute them for use by others in their projects.

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

```
django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.
```
These applications are included by default as a convenience for the common case.

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:

```
$ python manage.py migrate
```

The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app (we’ll cover those later). You’ll see a message for each migration it applies. If you’re interested, run the command-line client for your database and type \dt (PostgreSQL), SHOW TABLES; (MariaDB, MySQL), .schema (SQLite), or SELECT TABLE_NAME FROM USER_TABLES; (Oracle) to display the tables Django created.


In our honey app, we’ll create two models: Task and Meta.
These concepts are represented by Python classes. Edit the honey/models.py file so it looks like this:

```
from django.db import models


class Task(models.Model):
    title = models.CharField('Name', max_length=60)
    task = models.TextField('Describtion')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Task'
    verbose_name_plural = 'Task'

```

Here, each model is represented by a class that subclasses django.db.models.Model. Each model has a number of class variables, each of which represents a database field in the model.

Each field is represented by an instance of a Field class – e.g., CharField for character fields and DateTimeField for datetimes. This tells Django what type of data each field holds.

The name of each Field instance (e.g. question_text or pub_date) is the field’s name, in machine-friendly format. You’ll use this value in your Python code, and your database will use it as the column name.

You can use an optional first positional argument to a Field to designate a human-readable name. That’s used in a couple of introspective parts of Django, and it doubles as documentation. If this field isn’t provided, Django will use the machine-readable name. In this example, we’ve only defined a human-readable name for Question.pub_date. For all other fields in this model, the field’s machine-readable name will suffice as its human-readable name.

Some Field classes have required arguments. CharField, for example, requires that you give it a max_length. That’s used not only in the database schema, but in validation, as we’ll soon see.

A Field can also have various optional arguments; in this case, we’ve set the default value of votes to 0.

Finally, note a relationship is defined, using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.


ACTIVARING MODELS

That small bit of model code gives Django a lot of information. With it, Django is able to:

Create a database schema (CREATE TABLE statements) for this app.
Create a Python database-access API for accessing Question and Choice objects.
But first we need to tell our project that the honey/main app is installed.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

```

Now Django knows to include the honey/main app. Let’s run another command:

```
$ python manage.py makemigrations
```

You should see something similar to the following:

Migrations for 'main':

```
  main/migrations/0001_initial.py
    - Create model Task
```
By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.

Migrations are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file main/migrations/0001_initial.py. Don’t worry, you’re not expected to read them every time Django makes one, but they’re designed to be human-editable in case you want to manually tweak how Django changes things.

Now, run migrate again to create those model tables in your database:

```
$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Rendering model states... DONE
  Applying polls.0001_initial... OK
  
```

The migrate command takes all the migrations that haven’t been applied (Django tracks which ones are applied using a special table in your database called django_migrations) and runs them against your database - essentially, synchronizing the changes you made to your models with the schema in the database.

Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

- Change your models (in models.py).
- Run python manage.py makemigrations to create migrations for those changes
- Run python manage.py migrate to apply those changes to the database.
The reason that there are separate commands to make and apply migrations is because you’ll commit migrations to your version control system and ship them with your app; they not only make your development easier, they’re also usable by other developers and in production.


Wait a minute. <Task: Task object (1)> isn’t a helpful representation of this object. Let’s fix that by editing the Task model and adding a __str__() method to both Task and Meta:

from django.db import models

  
```
class Task(models.Model):
    title = models.CharField('Name', max_length=60)
    task = models.TextField('Describtion')

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Task'
    verbose_name_plural = 'Task'
  
```

It’s important to add __str__() methods to your models, not only for your own convenience when dealing with the interactive prompt, but also because objects’ representations are used throughout Django’s automatically-generated admin.

CREATING AN ADMIN USER

First we’ll need to create a user who can login to the admin site. Run the following command:

```
$ python manage.py createsuperuser
```

Enter your desired username and press enter.

```
Username: admin
```
You will then be prompted for your desired email address:

```
Email address: admin@example.com
```

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
Superuser created successfully.
```

The Django admin site is activated by default. Let’s start the development server and explore it.

If the server is not running start it like so:

```
$ python manage.py runserver
```

Now, open a Web browser and go to “/admin/” on your local domain – e.g., http://127.0.0.1:8000/admin/. You should see the admin’s login screen:

![alt text](admin01.png)

Now, try logging in with the superuser account you created in the previous step. You should see the Django admin index page:

![alt text](admin02.png)

You should see a few types of editable content: groups and users. They are provided by django.contrib.auth, the authentication framework shipped by Django.


Make the poll app modifiable in the admin

But where’s our poll app? It’s not displayed on the admin index page.

Only one more thing to do: we need to tell the admin that Task objects have an admin interface. To do this, open the main/admin.py file, and edit it to look like this:

```
from django.contrib import admin
from .models import Task


admin.site.register(Task)
```

Writing more views

Now let’s add a few more views to main/views.py. These views are slightly different, because they take an argument:

```
from django.shortcuts import render
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'main/index.html')


def about(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/about.html', {'title': 'About our plans after Finals', 'tasks': tasks})


def kpop(request):
    return render(request, 'main/kpop.html')


def anime(request):
    return render(request, 'main/anime.html')


def create(request):
    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html')

def aiu(request):
    return render(request, 'main/aiu.html')

```

Wire these new views into the main.urls module by adding the following path() calls:

```
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('kpop', views.kpop),
    path('anime', views.anime),
    path('create', views.create, name='create'),
    path('aiu', views.aiu, name='aiu'),
]
```

First, create a directory called templates in your main directory. Django will look for templates in there.

Your project’s TEMPLATES setting describes how Django will load and render templates. The default settings file configures a DjangoTemplates backend whose APP_DIRS option is set to True. By convention DjangoTemplates looks for a “templates” subdirectory in each of the INSTALLED_APPS.

Within the templates directory you have just created, create another directory called polls, and within that create a file called index.html. In other words, your template should be at main/templates/polls/index.html. Because of how the app_directories template loader works as described above, you can refer to this template within Django as main/index.html.

```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Main Page</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
<div class="container">
  <header class="blog-header py-3">
    <div class="row flex-nowrap justify-content-between align-items-center">
      <div class="col-4 pt-1">
        <a class="text-muted" href="/">Hello Everyone. Have a good life!</a>
      </div>
      <div class="col-4 text-center">
      </div>


         <a class="btn btn-sm btn-outline-secondary" href="/aiu">University Page</a>
        <a class="btn btn-sm btn-outline-secondary" href="/about">About</a>

      </div>
    </div>
  </header>



  <div class="jumbotron p-4 p-md-5 text-white rounded bg-dark">
    <div class="col-md-6 px-0">
      <h1 class="display-4 font-italic">Site by Medina and Aida</h1>
      <p class="lead my-3">Dream big. Work hard.</p>
    </div>
  </div>

  <div class="row mb-2">
    <div class="col-md-6">
      <div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-primary">Anime</strong>
          <h3 class="mb-0">What is anime?</h3>
          <div class="mb-1 text-muted">Dec 8</div>
          <p class="card-text mb-auto">Anime is a term for a style of Japanese comic book and video cartoon animation in which the main characters have large doe-like eyes. Many Web sites are devoted to anime. Anime is the prevalent style in Japanese comic books or manga . In Japan, the comic book is a popular form of entertainment for adults as well as for younger audiences. Story lines are often very sophisticated and complex and extend into episodic series.Foils for the main characters, including robots, monsters, or just plain bad people, often lack the doe-eyed quality.</p>
                 <a href="/anime" class="stretched-link">Continue reading</a>
        </div>
        <div class="col-auto d-none d-lg-block">
          <svg class="bd-placeholder-img" width="200" height="250" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
        <div class="col p-4 d-flex flex-column position-static">
          <strong class="d-inline-block mb-2 text-success">K-POP</strong>
          <h3 class="mb-0">What is K-POP?</h3>
          <div class="mb-1 text-muted">Dec 8</div>
          <p class="mb-auto">The term Kpop includes many different musical genres under its umbrella. Along with Korean pop, it can also include rock, hip hop, and electronic music. Kpop is considered a fairly new form of music. The type of K-Pop music that you’re listening to today was formed around the 1990s. The roots for K-Pop began from the 1950s, however, and have since then already been influenced a lot by different types of Western music and pop groups. American pop culture has especially had – and still does have – an effect on K-Pop.</p>
          <a href="/kpop" class="stretched-link">Continue reading</a>
        </div>
        <div class="col-auto d-none d-lg-block">
          <svg class="bd-placeholder-img" width="200" height="250" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>Placeholder</title><rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef" dy=".3em">Thumbnail</text></svg>
        </div>
      </div>
    </div>
  </div>
</div>

    <p>Wish you the best!</p>
</body>
</html>

```

Now let’s update our index view in polls/views.py to use the template:

```
def index(request):
    return render(request, 'main/index.html')
```

A shortcut: render():

```
    return render(request, 'main/index.html')
```

Namespacing URL names

the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

The answer is to add namespaces to your URLconf. In the main/urls.py file, go ahead and add an app_name to set the application namespace:

```
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('kpop', views.kpop),
    path('anime', views.anime),
    path('create', views.create, name='create'),
    path('aiu', views.aiu, name='aiu'),
]
```

And so we add a new html template to each path, and then add render and a module to make it work.

Thank you for watching!
