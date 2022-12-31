from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer 

    def get(self,request,format=None):
        """Return List of API View Features"""
        an_apiview = [
            'Use Http request method as function (get,post,put,patch,delete)',
            'Is similar to django default View',
            'Give you most control over the application logic',
            'Is mapped manually to URLs'
        ]
        return Response({
            'message': 'hello world',
            'an_apiview': an_apiview
        })

    def post(self,request):
        """create hello message with my name""" 
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status =status.HTTP_400_BAD_REQUEST
                )
    
    def put(self,request,pk=None):
        """Handling updating the object"""
        return Response({
            'message':'Method Put!'
        })
    
    def patch(self,request,pk=None):
        """Handling Partial Updating the objects"""
        return Response({
            'message':'Method Patch!'
        })
    
    def delete(self,request,pk=None):
        """Handling the deletion of the Objects"""
        return Response({
            'message': 'Method Delete!'
        })

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a hello message"""

        a_viewset = [
            'User actions (list,create,retireve,delete,update partial update',
            'Automaicall maps to URLs using',
            'Provide more functionality with less code',
        ]
        return Response({
            'message':'Hello World!',
            'a_viewset': a_viewset
        })
    
    def create(self,request):
        """Handling for creating an object"""
        serializers =  self.serializer_class(data=request.data)

        if serializers.is_valid():
            name =  serializers.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                'message':message
            })
        else:
            return Response(
                serializers.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

    def retrieve(self,request,pk=None):
        """Handling retireve the objects  by Id"""
        return Response({
            'http_method':'GET'
        })
    
    def update(self,request,pk=None):
        """Handling the update the  object"""
        return Response({
            'http_method':'Put'
        })

    def partial_update(self,request,pk=None):
        """Handling the updating patch """
        return Response({
            'http_method':'patch'
        })

    def destroy(self,request,pk=None):
        """Handling the removing objects"""
        return Response({
            'http_method':'delete'
        })


class UserProfileViewset(viewsets.ModelViewSet):
    "handling creating annd updating profiles"
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)


class UserLoginApiView(ObtainAuthToken):
    """Handling creating user authennication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """handing creating and updating profile feed item"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.UserProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated,)

    def perform_create(self, serializer):
        """set the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

