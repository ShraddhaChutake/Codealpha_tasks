#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Automatic Email Sender 
# Importing Libraries
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

# Email configuration
def send_email():
    sender_email = "sender_email@gmail.com"
    receiver_email = "receiver_email@gmail.com"
    password = "Enter your password"
    subject = "Scheduled Reminder"
    message = "Hello! This is a scheduled reminder from your Python program."

    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Login to your email account with password
        server.login(sender_email, password)
        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
        # Disconnect from the server
        server.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

def schedule_email(send_hour, send_minute):
    while True:
        # Get current time
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        # Check if it's time to send the email
        if current_hour == send_hour and current_minute == send_minute:
            send_email()
            break

# Set the time to send the email (24-hour format)
scheduled_hour = 12
scheduled_minute = 0

# Schedule the email
schedule_email(scheduled_hour, scheduled_minute)

