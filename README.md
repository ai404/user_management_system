# User Management System
A ready to use template with python and Flask to build your own web application.
## Getting Started

We have already implemented the following functions to help you get started to what matters the most in your own application:
* Login system
* Registration system with activation email
* Password reset/change
* User profile with picture import form

### Prerequisites

First, you will need to install
```
python 2.7
```

python 3 is not tested but you can get it to work with small changes if required.


next, install all the packages mentioned in requirements.txt file
```
pip install  -r requirements.txt
```
For the following you can either change the default value or define Environment Variables.

Now, we will have to configure our Mailing Service

- for Production, we will be using MailGun:

open config.py and locate the following Class
```python
class ProductionConfig(Base):
    # ...
    
    # Mail Config
    MAIL_SERVER = os.environ.get('MAILGUN_SMTP_SERVER', 'smtp.mailgun.org')
    MAIL_PORT = os.environ.get('MAILGUN_SMTP_PORT', 587)
    MAILGUN_KEY = os.environ.get('MAILGUN_KEY', "key-xxxxxxxxxxxxxxxxxxxxxxxxxx")
    MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN', "appaxxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org")
    MAIL_USERNAME = os.environ.get('MAILGUN_SMTP_LOGIN', "postmaster@appaxxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org")
    MAIL_PASSWORD = os.environ.get('MAILGUN_SMTP_PASSWORD', "xxxxxxxxxxxxxxxxxxxxxxxxxx")

    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', "no-reply@my-domain.com")
    #MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', True)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
```

- for Development, we will be using Gmail or any other smtp server:
```python
class DevelopmentConfig(Base):
    # ...
    
    # Mail Config
    MAIL_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('SMTP_PORT', 587)
    #MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', True)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
    MAIL_USERNAME = "username@gmail.com"
    MAIL_PASSWORD = "password"
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', "username@gmail.com")
```

Next, we will configure our database:

open config.py and locate the following line in both Dev and Production Configurations:
```python
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://username:password@host/database_name')
```

here I'm using mysql you can use any other engine by reading this documentation:
```
http://docs.sqlalchemy.org/en/latest/core/engines.html
```

finally, we are ready to run our App
### Running the app

```
manage.py runserver -h 0.0.0.0 -p 8080
```
Enjoy !