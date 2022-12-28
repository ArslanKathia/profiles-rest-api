from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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