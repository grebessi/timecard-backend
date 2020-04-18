from .views import TimelineCreateViewset, TimelineViewset
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'timeline', TimelineCreateViewset)
router.register(r'timeline', TimelineViewset)

urlpatterns = [
    path('', include(router.urls)),
]
