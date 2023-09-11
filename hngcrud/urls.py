from django.urls import path, include
from rest_framework.schemas import get_schema_view
from .views import PersonList, PersonDetail
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('api/', PersonList.as_view(), name='api'),
    path('api/<int:pk>/', PersonDetail.as_view(), name='api'),
    path('api/docs/', include_docs_urls(title='PersonAPI')),
    path('api/schema', get_schema_view(title='PersonAPI',
         description='API for the person database', version='1.0.0'), name='openapi-schema'),

]
