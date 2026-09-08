from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']

#compare the password, the two passwords that user provide because that is only validation that we do you account at the model level
    def validate(self, attrs):
        password = attrs.get('password', '')
        password2 = attrs.get('password2', '')
        if password != password2:
            raise serializers.ValidationError("Passwords do not match")
        #attrs.pop('password2', None)
        return attrs
        #return super().validate(attrs)
#after validation we create the user object so at this point where you have this you can say

    def create(self, validated_data):
        #user=User.objects.create_user(**validated_data)
        #user equals to our user model we need to import that
        #from objects.create_user. so in this case normally you can put spread the dictionary object because
        #that attribute is coming as a dictionary object but we can't do it like this [user=User.objects.create_user(**validated_data)] because the user is not 
        #just sending the exact and data that is being inserted into a database they also sending extra password 
        #which is the password two so the password two is not actually going to be inserted into our database it's just for 
        #validation of the actual password we do as follows:
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            password=validated_data.get('password')
        )

        #once we pass this we have the user object created so what we need to do is we just need to return the user
        #that was created so we return the user
        return user

#no we need to setup the email verification so we are going to create the utility function that will help us 
#send this email to the user. so in our login app we will create a utility function utils.py for sending email verification.

      #  def create(self, validated_data):
      #      return super().create(validated_data)

