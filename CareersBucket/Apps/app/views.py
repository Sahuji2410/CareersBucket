# views.py
from rest_framework import generics
from Apps.apps_models.models import JobType, JobDescription
from .serializers import JobTypeSerializer, JobDescriptionSerializer

class JobTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobType.objects.all()
    print(queryset)
    serializer_class = JobTypeSerializer

class JobTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

class JobDescriptionListCreateAPIView(generics.ListCreateAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer

class JobDescriptionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
