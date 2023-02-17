from rest_framework import serializers
from .models import *


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'

class MocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moc
        fields = '__all__'

class ToolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToolType
        fields = '__all__'

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = '__all__'

class TabletSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabletSize
        fields = '__all__'

class U1Serializer(serializers.ModelSerializer):
    class Meta:
        model = U1
        fields = '__all__'

class U2Serializer(serializers.ModelSerializer):
    class Meta:
        model = U2
        fields = '__all__'

class L1Serializer(serializers.ModelSerializer):
    class Meta:
        model = L1
        fields = '__all__'

class L2Serializer(serializers.ModelSerializer):
    class Meta:
        model = L2
        fields = '__all__'

class DSerializer(serializers.ModelSerializer):
    class Meta:
        model = D
        fields = '__all__'

class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = '__all__'

class PlatingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatingType
        fields = '__all__'

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'

class PunchBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = PunchBlank
        fields = '__all__'

class DieBlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = DieBlank
        fields = '__all__'







