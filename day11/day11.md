# 🚀 Day 11 – Entering the Django World

## 🎯 Goal

Today I started learning Django after building APIs with Node.js and Express.

Instead of immediately rebuilding my ARCHERS website, I focused on understanding how Django is structured and how requests move through a Django application.

---

# 🧠 Why Django?

Until now I learned:

```text
Frontend
   ↓
fetch()
   ↓
Express API
   ↓
JSON
```

Now I want to learn Python Full Stack Development.

Django provides:

- Backend Framework
- URL Routing
- Template Engine
- ORM (Database Layer)
- Authentication System
- Admin Dashboard

all in one framework.

---

# 🏗 Creating a Django Project

Installed Django:

```bash
pip install django
```

Created a project:

```bash
django-admin startproject core .
```

---

# Understanding the Command

```bash
django-admin startproject core .
```

### django-admin

Django's command line tool.

### startproject

Creates a new Django project.

### core

Project name.

### .

Create the project in the current directory.

---

# Project Structure

```text
archers-django/
│
├── manage.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
```

---

# Understanding Key Files

## manage.py

Command center of Django.

Used for:

```bash
python manage.py runserver
python manage.py startapp
python manage.py migrate
```

---

## settings.py

Control panel of the project.

Contains:

- Installed Apps
- Database Configuration
- Time Zone
- Language
- Static Files

---

## urls.py

Routing system.

Example:

```python
path("", home)
```

Maps URLs to functions.

Equivalent to:

```javascript
app.get("/")
```

in Express.

---

## views.py

Contains application logic.

Example:

```python
def home(request):
    return HttpResponse("Hello")
```

Handles requests and returns responses.

---

# Creating My First App

Created:

```bash
python manage.py startapp main
```

Generated:

```text
main/
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── views.py
└── migrations/
```

---

# Registering the App

Added:

```python
'main'
```

inside:

```python
INSTALLED_APPS
```

in settings.py.

---

# My First View

Created:

```python
from django.http import HttpResponse

def home(request):
    return HttpResponse(
        "Hello Irfan, Django is working!"
    )
```

---

# Understanding request

One of the most important concepts learned today:

```python
def home(request):
```

The request object contains information coming from the browser.

Examples:

```python
request.method
request.path
request.headers
```

Simple definition:

```text
request
=
Data coming into the server
```

---

# Understanding HttpResponse

```python
return HttpResponse("Hello")
```

Sends data back to the browser.

Simple definition:

```text
HttpResponse
=
Data going out of the server
```

---

# First URL Route

In urls.py:

```python
from main.views import home

urlpatterns = [
    path("", home),
]
```

Meaning:

```text
/
↓
home()
↓
Response
```

---

# Django Request Flow

Today I learned how Django processes requests.

```text
Browser
   ↓
urls.py
   ↓
views.py
   ↓
HttpResponse
   ↓
Browser
```

---

# Comparing Express and Django

## Express

```javascript
app.get("/", (req,res)=>{
    res.send("Hello")
})
```

## Django

```python
def home(request):
    return HttpResponse("Hello")
```

Different syntax.

Same idea.

---

# Templates

Learned why templates are important.

Instead of:

```python
return HttpResponse("Hello")
```

Django can render HTML files:

```python
return render(
    request,
    "index.html"
)
```

This is how real websites are built.

---

# Mental Model

Today I learned that Django is not magic.

The flow is:

```text
URL
 ↓
View
 ↓
Response
```

and later:

```text
URL
 ↓
View
 ↓
Template
 ↓
Browser
```

---

# Biggest Lesson

I used to focus on learning syntax.

Today I focused on understanding architecture.

Whether it's Express or Django, the core idea remains:

```text
Request
 ↓
Logic
 ↓
Response
```

Frameworks change.

Concepts stay the same.

---

# Next Goal

- Render HTML Templates
- Move ARCHERS into Django
- Learn Django Template Engine
- Pass Python Data into HTML
- Learn Django Models

Day 11 ✅
