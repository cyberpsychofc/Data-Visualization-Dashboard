from rest_framework import serializers
from .models import Report
from collections import OrderedDict

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
    # to remove the empty entries in the data
    def to_representation(self, instance):
        result = super().to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] != ""])