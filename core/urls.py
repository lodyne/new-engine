from django.urls import path
from . import views
from .views import (
    ChartData,
    HomeView,
    # API_Objects,
    # API_Objects_details,
    # ChartData
)

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('',HomeView.as_view(), name = "dashboard" ),
    # path('basic/',API_Objects.as_view(), name='basic'),
    # path('basic/<int:pk>/',API_Objects_details.as_view(), name='basic-details'),
    # path('chart/', views.get_data, name='chart'),
    path('api/data/chart', ChartData.as_view(), name='api-data'), 
    path('chart/api/data/chart', ChartData.as_view(), name='api-data') 
    
]

urlpatterns = format_suffix_patterns(urlpatterns)