from rest_framework import serializers
from .models import *


class MarketingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketingForm
        fields = '__all__'



class ClientDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientDetails
        fields = '__all__'



