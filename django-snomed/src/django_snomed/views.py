from django.shortcuts import render
from rest_framework import viewsets, generics
from django_snomed.serializers import DescriptionSerializer
from django_snomed.models import DescriptionF
class DescriptionViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = DescriptionSerializer
    
    def get_queryset(self):
        term  = self.kwargs['term']
        return DescriptionF.objects.filter(term__icontains=term, languagecode = 'es')
    
