# serializers.py
from rest_framework import serializers
from Apps.apps_models.models import JobType, JobDescription , jobAnnouncments

class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = '__all__'

class jobAnnouncmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobAnnouncments
        fields = '__all__'