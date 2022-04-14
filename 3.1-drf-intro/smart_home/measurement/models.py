from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

# датчик
class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование датчика')
    description = models.CharField(max_length=200, verbose_name='Описание датчика')

    def __str__(self):
        return f'{self.name} : {self.description}'


# сенсор
class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement_id')
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sensor_id}, {self.date}, {self.temperature}'
