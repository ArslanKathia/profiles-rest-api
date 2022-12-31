from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializer a user for Profile object"""

    class Meta:
        model = models.UserProfile
        fields =('id','name','email','password')
        extra_kwargs = {
            'password':{
                'write_only':True,  
                'style':  {
                    'input_type': 'password'
                }
            }
        }

    def create(self,validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email =  validated_data['email'],
            name = validated_data['name'],
            password= validated_data['password']
        )
        return user

    def update(self,instance,validated_data):
        """Handling updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance,validated_data)

class UserProfileFeedItemSerializer(serializers.ModelSerializer):
    """User profile feeditem of user object"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on',)
        extra_kwargs ={
            'user_profile':{'read_only':True}
        }