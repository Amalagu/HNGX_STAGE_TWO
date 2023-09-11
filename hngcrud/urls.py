from django.urls import path, include
from .views import PersonList, PersonDetail
urlpatterns = [
    path('api/', PersonList.as_view(), name='api'),
    path('api/<int:pk>/', PersonDetail.as_view(), name='api'),
]
