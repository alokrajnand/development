

from rest_framework import serializers
from .models import jobline


class joblineSerializer(serializers.ModelSerializer):

    class Meta:
        model = jobline
        fields = '__all__'
