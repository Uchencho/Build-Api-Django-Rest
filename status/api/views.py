from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication
from .serializers import StatusSerializer
from status.models import Status

class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

#Explaining Mixins
# CreateModelMixin ---> POST method
# UpdateModelMixin ---> PUT method
# DestroyModelMixin ---> DELETE method

class StatusAPIView(mixins.CreateModelMixin ,generics.ListAPIView): #Create and List
    #This will enable a list view
    #permission_classes          = [permissions.IsAuthenticated]
    #authentication_classes      = [SessionAuthentication]
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

    #Inheriting from mixin class, this will enable a create function
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        #This is used to override an nbuilt function which enables user which is a required field be read only
        serializer.save(user=self.request.user)

    #This enables search --> seraching for testing  http://127.0.0.1:8000/api/status/?q=Testing
    def get_queryset(self):
        qs = Status.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

'''
#Because of the Create model mixin above, this has been rendered useless
class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()
'''

class StatusDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    #permission_classes          = [permissions.IsAuthenticated]
    #authentication_classes      = [SessionAuthentication]
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

'''
#Because of the Update and Destroy mixins above, these have been rendered useless
class StatusUpdateAPIView(generics.UpdateAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

class StatusDeleteAPIView(generics.DestroyAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

'''