# Used internally by Django, can be anything of your choice
SECRET_KEY = 'abc'
# API hostname, e.g. https://api.openbankproject.com
API_HOST = 'http://127.0.0.1:8080'
#API_HOST = 'https://openlab.openbankproject.com'

#API_HOST = 'https://apisandbox.openbankproject.com'
API_VERSION = '3.1.0'

#REDIRECT_URL = 'https://openlab.openbankproject.com'
# Consumer key + secret to authenticate the _app_ against the API
# When the app is created on the API, the redirect URL should point to this
# host + /obp, e.g. `http://127.0.0.1:9090`

#OAUTH_CONSUMER_KEY = 'wjpryoltrom3faqfok4ozyxrqxqxjsvrqlgypzmj'
#OAUTH_CONSUMER_SECRET = 'ew2d0yiew2juilvpjfpcufmxozk0icbhnozzk54m'

REDIRECT_URL = 'http://127.0.0.1:9090'
OAUTH_CONSUMER_KEY = 'ttxkdryyzr5n5ibgnt3a5velzxw2bpdcopm4qu1u'
OAUTH_CONSUMER_SECRET = 'rtvsmyan1gduxbj3ytvbvwbafim1pwylnfpny5sy'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'api-tester',
        'USER': 'postgres',
        'PASSWORD': '0218',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


ADMIN_USERNAME = "pflee"
ADMIN_PASSWORD = "Pflee@0218"
FILE_ROOT = "./output_path/"
OUTPUT_PATH = './output_path/'

INPUT_PATH = "./input_file/"
DATASET_PATH = "{}dataset.xlsx".format(INPUT_PATH)
OPTIONS_PATH = "{}options.xlsx".format(INPUT_PATH)

MONTHS = 36
BANK_NUMBER=3
BRANCH_NUMBER=4
ATM_NUMBER=6
PRODUCT_NUMBER=10
COUNTRY='Hong Kong'

VERIFY = True if API_HOST.startswith("https") else False