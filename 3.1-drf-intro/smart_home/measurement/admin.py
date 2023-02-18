from django.contrib import admin

from .models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement
    extra = 1


class SensorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    inlines = [MeasurementInline]


class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'date')


admin.site.register(Sensor, SensorAdmin)
admin.site.register(Measurement, MeasurementAdmin)
