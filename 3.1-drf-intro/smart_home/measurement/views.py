# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Sensor
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


# 4. Получить список датчиков. Выдается список с краткой информацией по датчикам: ID, название и описание.
@api_view(['GET'])
def demo(request):
    sensors = Sensor.objects.all()
    ser = SensorSerializer(sensors, many=True)
    return Response(ser.data)


# 3. Создать датчик. Указываются название и описание датчика.

class DemoView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        sensor = request.data.get('sensor')
        serializer = SensorSerializer(data=sensor)
        if serializer.is_valid(raise_exception=True):
            sensor_saved = serializer.save()
            return Response({'status': 'ok'})


# 4. Добавить измерение. Указываются ID датчика и температура.
class MeasurementView(APIView):

    def post(self, request):
        measurement = request.data.get('measurement')
        serializer = MeasurementSerializer(data=measurement)
        if serializer.is_valid(raise_exception=True):
            measurement_saved = serializer.save()
            return Response({'status': 'ok'})


# 2. Изменить датчик. Указываются название и/или описание.
class SensorUpdateView(APIView):

    def put(self, request, pk):
        saved_sensor = get_object_or_404(Sensor.objects.all(), pk=pk)
        data = request.data.get('updation')
        serializer = SensorSerializer(instance=saved_sensor, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved_sensor = serializer.save()
        return Response({
            "success": "Sensor '{}' updated successfully".format(saved_sensor.title)
        })


# 5. Получить информацию по конкретному датчику.
# Выдается полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    # queryset = Sensor.objects.prefetch_related('measurement_id')
    serializer_class = SensorDetailSerializer


