from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserCreateViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'users', UserCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
