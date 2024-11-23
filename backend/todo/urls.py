from django.urls import path
from .views import TodoViewSet


urlpatterns = [
    path('todo/', TodoViewSet.as_view({'get': 'list'}))
]