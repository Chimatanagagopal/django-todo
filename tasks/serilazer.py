from rest_framework import serializers
from .models import studentData

class studentSerilazation(serializers.ModelSerializer):
    class Meta:
        model=studentData
        fields='__all__'