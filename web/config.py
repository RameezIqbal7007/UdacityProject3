import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_URL="c.rameezdatabase.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="citus" #TODO: Update value
    POSTGRES_PW="Godfather2403"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'MNr5lvjkhjdNAYLATYd4ap6PQUmDtvx'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://rameezservicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=YgyaGUBRFimVMOa/UvcbSmzcAzfauqjqWA7ytHSHays=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS = 'rameez.iqbal@lineview.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
