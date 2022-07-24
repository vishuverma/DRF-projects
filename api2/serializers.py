from unicodedata import name
from rest_framework import serializers
from .models import studnt


class studntSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)
    
    
    def create(self, validate_data): 
        return studnt.objects.create(**validate_data)