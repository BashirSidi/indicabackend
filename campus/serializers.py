from rest_framework import serializers
from .models import Detail, Measure, KPI, Control


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['id', 'description', 'created_at', 'updated_at']


class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'name', 'value', 'created_at', 'updated_at']


class KPISerializer(serializers.ModelSerializer):
    class Meta:
        model = KPI
        fields = ['id', 'name', 'value', 'created_at', 'updated_at']


class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ['id', 'name', 'status', 'created_at', 'updated_at']
