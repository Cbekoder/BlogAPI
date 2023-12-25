from rest_framework import serializers
from .models import *

class MuallifSerializer(serializers.ModelSerializer):
    class Meta:
        model =Muallif
        fields = '__all__'

class MaqolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maqola
        fields = '__all__'