import os


class Base(object):
    PHOTOS_ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    IMAGES_PATH = ["static/images", BASE_DIR + "/media"]

    os.chdir(BASE_DIR)

    THREADS_PER_PAGE = 2

    # Enable protection agains *Cross-site Request Forgery (CSRF)*
    WTF_CSRF_ENABLED = True

    # Secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET_KEY', 'fs4q6f4qs6d4fSDfsdfG6')

    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 's6f4sd6f46GFF4d64sd64D')

    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_TIME_LIMIT = None


class ProductionConfig(Base):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://username:password@host/db_name')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}

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


class DevelopmentConfig(Base):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:@localhost/frecog')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_CONNECT_OPTIONS = {}

    # Mail Config
    MAIL_SERVER = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
    MAIL_PORT = os.environ.get('SMTP_PORT', 587)
    #MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', True)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
    MAIL_USERNAME = "username@gmail.com"
    MAIL_PASSWORD = "password"
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', "username@gmail.com")


class StagingConfig(Base):
    TESTING = True
