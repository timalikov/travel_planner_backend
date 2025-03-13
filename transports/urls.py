from django.urls import path

from transports.views import TransportTypeViewSet


urlpatterns = [
    path('', TransportTypeViewSet.as_view(), name='transport-type-list'),
]