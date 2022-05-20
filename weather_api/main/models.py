from django.db import models


class City(models.Model):

    city_name = models.CharField(
        max_length=255,
    )

    country_abbreviation = models.CharField(
        max_length=2,
    )

    longitude = models.FloatField()

    latitude = models.FloatField()


class Temperature(models.Model):

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )

    temperature = models.FloatField()

    minimum_temperature = models.FloatField()

    maximum_temperature = models.FloatField()

    pressure = models.FloatField()

    humidity = models.FloatField()

    wind_speed = models.FloatField()

    time = models.DateTimeField(
        auto_now_add=True,
    )
