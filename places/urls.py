from django.urls import path

from places.views import CityViewSet, CountryViewSet, HotelViewSet, PlaceCategoryViewSet, PlaceViewSet


urlpatterns = [
    path('places-categories/', PlaceCategoryViewSet.as_view(), name='place-category-list'),
    path('countries/', CountryViewSet.as_view(), name='country-list'),
    path('cities/', CityViewSet.as_view(), name='city-list'),
    path('places/', PlaceViewSet.as_view(), name='place-list'),
    path('hotels/', HotelViewSet.as_view(), name='hotel-list'),
]