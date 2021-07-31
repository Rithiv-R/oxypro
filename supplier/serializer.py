from rest_framework import  serializers
from . models import  oxygensuppliers

class oxysupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=oxygensuppliers
        fields='__all__'