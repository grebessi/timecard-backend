from rest_framework import serializers
from .models import Timeline


class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = (
            'id',
            'start',
            'stop',
            'start',
            'user',
            'created_at',
        )
        read_only_fields = ['user', 'created_at']
