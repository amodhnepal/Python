import smtplib
import datetime as dt
import random

MY_EMAIL = "amodhnepal3@gmail.com"
MY_PASSWORD = "12345abc()"


now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    with open("quotes.txt") as file:
        quote = file.readlines()
        Quote = random.choice(quote)
    print(Quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject:Monday Motivation\n\n{quote}")