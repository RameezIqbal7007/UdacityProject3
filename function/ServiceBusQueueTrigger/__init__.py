import azure.functions
import logging
import sendgrid
import datetime
import psycopg2
import os

app_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = True
    POSTGRES_URL="c.rameezdatabase.postgres.database.azure.com"  #TODO: Update value
    POSTGRES_USER="citus" #TODO: Update value
    POSTGRES_PW="Godfather2403"   #TODO: Update value
    POSTGRES_DB="techconfdb"   #TODO: Update value
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm'
    SERVICE_BUS_CONNECTION_STRING ='Endpoint=sb://rameez.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=DDAdDG7HwJUEL5NRwKg2X2lSKORTDkS7L+ASbKqvbJY=' #TODO: Update value
    SERVICE_BUS_QUEUE_NAME ='notificationqueue'
    ADMIN_EMAIL_ADDRESS = 'rameez.iqbal@lineview.com'
    SENDGRID_API_KEY = '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' #Configuration not required, required SendGrid Account

def main(msg: azure.functions.ServiceBusMessage):
 message = msg.get_body().decode('utf-8')
 logging.info('Python ServiceBus queue trigger processed message: %s', message)
 connection = psycopg2.connect(dbname = Config.POSTGRES_DB, user = Config.POSTGRES_USER, password = Config.POSTGRES_PW, host = Config.POSTGRES_URL)
 cursor = connection.cursor()
 try:
  notification_id = int(message)
  notification_query = "SELECT subject, message FROM notification WHERE id={};".format(notification_id)
  cursor.execute(notification_query
  notification_result = cursor.fetchone()
  subject_field = notification_result[0]
  body_field = notification_result[1]
  attendee_query = "SELECT email, first_name FROM attendee;"
  cursor.execute(attendee_query)
  attendees_result = cursor.fetchall()
  for email_field, first_name_field in attendees_result:
   content_field = "Hello {},\n\n{}".format(first_name_field, body_field)
   mail_object = sendgrid.helpers.mail.Mail(from_email = Config.ADMIN_EMAIL_ADDRESS, to_emails = email_field, subject = subject_field, plain_text_content = content_field)
   try:
    sendgrid_api = sendgrid.SendGridAPIClient(Config.SENDGRID_API_KEY)
    sendgrid_response = sendgrid_api.send(mail_object)
   except Exception as error:
    logging.error(error)
  n_attendees = len(attendees_result)
  status_field = "{} attendees were notified.".format(n_attendees)
  current_time = datetime.datetime.utcnow()
  update_command = "UPDATE notification SET status = '{}', completed_date = '{}' WHERE id = {};".format(status_field, current_time, notification_id)
  cursor.execute(update_command)
  connection.commit()
 except Exception as error:
  logging.error(error)
  connection.rollback()       
 finally:
  cursor.close()
  connection.close()
