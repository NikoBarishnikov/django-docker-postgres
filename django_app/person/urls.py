from django.urls import path
from .views import PersonListCreateAPIView, PersonRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("persons/", PersonListCreateAPIView.as_view(), name="person-list-create"),
    path("persons/<int:pk>/", PersonRetrieveUpdateDestroyAPIView.as_view(), name="person-detail"),
]





