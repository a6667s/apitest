from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from company import views

urlpatterns = [
    path('job/', views.Jobview.as_view()),
    path('job/<int:pk>/', views.JobDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)