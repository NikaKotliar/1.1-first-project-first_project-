from rest_framework import serializers

# TODO: опишите необходимые сериализаторы
from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Sensor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'date']

    def create(self, validated_data):
        return Measurement.objects.create(**validated_data)


class SensorDetailSerializer(serializers.ModelSerializer):
    measurement_id = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement_id']
