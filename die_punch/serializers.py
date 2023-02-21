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



class BlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blank
        fields = '__all__'

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = '__all__'

class BodyTipMachiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyTipMachining
        fields = '__all__'

class HeadMachiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadMachining
        fields = '__all__'

class KeywayTaperFinishSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeywayTaperFinish
        fields = '__all__'

class HTSerializer(serializers.ModelSerializer):
    class Meta:
        model = HT
        fields = '__all__'

class GrindingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grinding
        fields = '__all__'

class HardChromeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HardChrome
        fields = '__all__'

class QualityCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityCheck
        fields = '__all__'

class PackingDispachSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingDispach
        fields = '__all__'

class DispachModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DispachMode
        fields = '__all__'







