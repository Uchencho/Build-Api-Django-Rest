from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics

from .serializers import StatusSerializer
from status.models import Status

class StatusListSearchAPIView(APIView):
    permission_classes          = []
    authentication_classes      = []

    def get(self, request, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

class StatusAPIView(generics.ListAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

class StatusCreateAPIView(generics.CreateAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

class StatusDetailAPIView(generics.RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = StatusSerializer
    queryset                    = Status.objects.all()

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