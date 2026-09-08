#here we create function to actually generate our otp and also the function to send an email
#there are a lot of ways this otp verification can be done. if you want an otp that expires at particular time maybe that short live
#you can use package called pyotp to generate time-based one-time passwords (TOTPs) i.e. function to generate otp that expires at particular set time

#here we want to create simple verification so we are going to create a that just generates a random sequence of number as an otp and
#send it to the user so that users can return that number to us back so that we can actually verify that the user email
#is active 

import random #import random from the Python standard library
from django.core.mail import EmailMessage
from django.conf import settings

from .models import User, OneTimePassword

#this is not the best of doing it use package pyotp to generate time-based one-time passwords (TOTPs) for better security
#we need to create another utility function 


def generateotp():
    otp = "" #set string
    for i in range(6):
        otp += str(random.randint(1, 9))#
    return otp


def send_code_to_user(email):
    #so this is going to take the email of the user
    #now here we construct the email we want to send
    #two things we are going to do: we are going to send code to the user and we're also going to create an otp model
    #just heading to user models i.e models.py and create class OneTimePassword(models.Model): and def __str__(self):

    #1. generate an otp
    otp_code = generateotp()
    print(otp_code)

    #2. send it to the user's email
    subject = "One time passcode for Email Verification"
    user = User.objects.get(email=email)
    current_site = "myAuth.com"
    #we are using this simple current site and domain for the site because the current site or the domain of the site is going to be our frontend domain and we can't use the backend
    #backend api is going to be hidden 
    email_body = (
        f"Hi {user.first_name},\n\n"
        f"Your OTP code for email verification on {current_site} is {otp_code}.\n\n"
        "Thank you!"
    )
    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    send_email = EmailMessage(
        subject=subject,
        body=email_body,
        from_email=from_email,
        to=[email],
    )
    send_email.send(fail_silently=True)

#now import it to the views.py


