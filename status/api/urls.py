from django.urls import path, include
from django.conf.urls import url
from .views import StatusAPIView, StatusCreateAPIView

urlpatterns = [
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    #url(r'^(?P<id>.*)/$', StatusDetailAPIView.as_view()),
    #url(r'^(?P<id>.*)/update/$', StatusUpdateAPIView.as_view()),
    #url(r'^(?P<id>.*)/delete/$', StatusDeleteAPIView.as_view()),
]

# /api/status/ --> List
# /api/status/create --> Create
# /api/status/12/ --> Detail
# /api/status/12/update/ --> Update
# /api/status/12/delete/ --> Delete