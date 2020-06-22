
from django_snomed.models import DescriptionF
from rest_framework import serializers
class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptionF
        fields = ['term',]

