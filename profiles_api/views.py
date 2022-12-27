from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test Api View"""

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