# Django settings for joejasinski project.
import os
import sys
import dj_database_url
gettext = lambda s: s


def env(key, default=None):
    """Retrieves env vars and makes Python boolean replacements"""
    val = os.getenv(key, default)

    if val == 'True':
        val = True
    elif val == 'False':
        val = False
    return val


def env_list(key, default=""):
    val = os.getenv(key, default)
    return val.split(",")


PROJECT_DIR = env(
    "DJANGO_PROJECT_DIR",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

SITE_DIR = env(
    "SITE_DIR",
    os.path.abspath(os.path.join(PROJECT_DIR, '..', '..', '..')))


sys.path.insert(0, os.path.join(PROJECT_DIR, 'apps', ))

DEBUG = env("DJANGO_DEBUG", False)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS


# FORMAT:    postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {'default': dj_database_url.parse(env("DJANGO_DATABASE_URL", "postgres://user:pass@localhost:/database"))}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", '*')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en-us', 'English'),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = env(
    "DJANGO_MEDIA_ROOT",
    os.path.abspath(os.path.join(SITE_DIR, 'htdocs', 'media')))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = env(
    "DJANGO_STATIC_ROOT",
    os.path.abspath(os.path.join(SITE_DIR, 'htdocs', 'static')))

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static'),
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", '1s(wsqn%(gvu92f%%l2(vwaiewz_6xnx&9v15z^40-jq3&0%)0')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'htmlmin.middleware.MarkRequestMiddleware',
)

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/x-sass', 'sass {infile} {outfile}'),
    ('text/x-scss', 'sass --scss {infile} {outfile}'),
)

ROOT_URLCONF = 'dddemo.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'dddemo.wsgi.application'


HTML_MINIFY = True
EXCLUDE_FROM_MINIFYING = ('^files/', '^admin/', '^media/')

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',

    'django_extensions',
    'compressor',

)

CONTACT_EMAIL = "joe.jasinski@gmail.com"


MIGRATION_MODULES = {
}

THUMBNAIL_HIGH_RESOLUTION = True
