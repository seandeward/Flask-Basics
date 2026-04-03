# How to Set Up Basic User Authentication in a Flask App

User authentication is important for protecting sensitive information and resources from unauthorized access.

It helps ensure that only authorized users can access and make changes to data, and helps prevent unauthorized users from gaining access to sensitive information.

There are different methods for implementing user authentication, including password-based authentication, token-based authentication, and so on.

We'll learn how to set up basic user authentication (in this case, password-based authentication) in this Flask application.

## Prerequisites

### Virtual Environment

Since we'll need a few external libraries for this project, it's best practice to create virtual environment to install them into.

Code: `py -m venv env` and then `env/scripts/activate`.

### Libraries

- **Flask**
  - A **simple microframework** that helps build scalable and secure web apps.
- **Flask-Login**
  - **Provides user session management** for Flask.
  - Handles logging in, logging out, and remembering user sessions over extended periods of time.
- **Flask-Bcrypt**
  - A Flask extension providing **bcrypt** hashing utilities for the app. *(bcrypt itself is a hashing algorithm that tends to be a significant hurdle for hackers. Keep in mind of course that users still require strong passwords!)*
- **Flask-WTF**
  - Simple integration of Flask and WTForms to create forms in Flask.
- **Flask-Migrate**
  - **Handles SQLAlchemy database migrations** for Flask apps using **Alembic**.
  - Database operations are available through the Flask cmd-line interface.
  - Beginner's Guide to SQLAlchemy and Alembic: https://medium.com/@evembijo/beginners-guide-to-alembic-and-sqlalchemy-in-python-manage-your-database-like-a-pro-9395b5b5080d
- **Flask-SQLAlchemy**
  - Adds support for SQLAlchemy to the app,
- **Flask-Testing**
  - Provides unit testing utilities for Flask.
- **Python Decouple**
  - Helps you use environment variables in your project.
    - *Environment variables are key-balue pairs stored outside of your Python code in the OS environment. They are supposed to be more secure than leaving your credentials in a `credentials.txt` file next to `mystuff.py`*

**To install all of these libraries, use the following command:**

`pip install Flask Flask-Login Flask-Bcrypt Flask-WTF FLask-Migrate Flask-SQLAlchemy Flask-Testing python-decouple`

## Setting up the Project

