from django.urls import path
from trips.views import UserTripViewSet


urlpatterns = [
    path('', UserTripViewSet.as_view(), name='user-trip-list'),
]