from django.urls import path, include
from django.conf.urls import url
from .views import (
    StatusAPIView, 
    #StatusCreateAPIView,
    StatusDetailAPIView,
    #StatusUpdateAPIView,
    #StatusDeleteAPIView,
    )

urlpatterns = [
    path('', StatusAPIView.as_view()),
    #path('create/', StatusCreateAPIView.as_view()),
    url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]

# /api/status/ --> List
# /api/status/create --> Create
# /api/status/12/ --> Detail
# /api/status/12/update/ --> Update
# /api/status/12/delete/ --> Delete