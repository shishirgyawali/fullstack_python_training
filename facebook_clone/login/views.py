from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .utils import send_code_to_user
from .serializers import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here. 
#We are going to create a view to register a new user and 
# secondly we're going to create the model for one time password and 
# we're also going to create utility functions to actually send the 
#generated one time password to user.

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self, request): 
        #post request
        user_data = request.data
        #we get the user data from the frontend and we want to 
        #validate them through serializer and if they are valid wants to save them to our database
        #and send an email to the user a verification code.
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            #this valid method is going to trigger our validate method in the serializer. so we are going to define basic validations
            # once we call this validate here we can raise the exception and set it to true 
            user = serializer.save()
            #if it is valid we want to call this serializer to save the user data to our database and to send an email
            send_code_to_user(user.email)
            print(user)
            #send email function created in utils.py
            #now after setting up this function we have to setup email configuration SMTP, you can use google or any other smtp server that's available to you
            #so to setup our email server we just head over to mailtrap.io and get the SMTP credentials and configure them in our Django settings.py file.
            return Response({
                'data': serializer.data,
                'message': f'Hi {user.first_name} thanks for signing up. A passcode has been sent.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #user object and message by making string and send status code. import status code. 201 for success
        #if by any reason validation fails we want to return another response 400
