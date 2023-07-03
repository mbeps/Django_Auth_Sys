This is a simple backend system built with Django that allows users to sign up and log in using a REST API.

# **Requirements**
These are the requirements needed to run the project:
- Python 3.10+
- Poetry

# **Features**

- **Sign Up:** New users can create an account.
- **Log In:** Existing users can log in to their account.

# **Stack**

This project uses the following technologies:

- [Python](https://www.python.org/): Python is a powerful, easy-to-learn, and widely-used programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.
- [Django](https://www.djangoproject.com/): Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development.
- [Django REST Framework](https://www.django-rest-framework.org/): Django REST Framework is a powerful and flexible toolkit for building Web APIs. It's a flexible, full-featured, and modular toolkit for building APIs.

# **Installation Instructions**

To run the project locally, you need to follow the below instructions:

## 1. **Clone the Project**
```sh
git clone https://github.com/mbeps/Django_Auth_Sys.git
```


## 2. **Install Dependencies**

Install dependencies using [Poetry](https://python-poetry.org/), a Python dependency management tool. If you don't have Poetry, you can install it following the [official guide](https://python-poetry.org/docs/#installation).


```bash
poetry install
```

## 3. **Run Migrations**

Once all dependencies are installed, you can run the migrations:

```bash
poetry run ./manage.py migrate
```

## 4. **Run Project** 
After running migrations, start the development server:

```bash
poetry run ./manage.py runserver
```

The server should start at http://127.0.0.1:8000.

You can now use the API endpoints to sign up and log in.
