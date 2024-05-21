from django.urls import path
from Apps.app.views import *

urlpatterns = [
    path('job-types/', JobTypeListCreateAPIView.as_view(), name='jobtype-list-create'),
    path('job-types/<int:pk>/', JobTypeRetrieveUpdateDestroyAPIView.as_view(), name='jobtype-detail'),
    path('job-descriptions/', JobDescriptionListCreateAPIView.as_view(), name='jobdescription-list-create'),
    path('job-descriptions/<int:pk>/', JobDescriptionRetrieveUpdateDestroyAPIView.as_view(), name='jobdescription-detail'),
]