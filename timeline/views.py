from django_filters import rest_framework as filters
from rest_framework import mixins, permissions, viewsets
from rest_framework.permissions import AllowAny

from .filters import TimelineFilter
from .models import Timeline
from .permissions import IsAdminOrIsOwner
from .serializers import TimelineSerializer


class TimelineCreateViewset(mixins.CreateModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    filterset_fields = '__all__'
    filterset_class = TimelineFilter
    filter_backends = (filters.DjangoFilterBackend,)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TimelineViewset(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    permission_classes = (IsAdminOrIsOwner & permissions.IsAuthenticated,)
