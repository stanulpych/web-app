from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('roadmap/', views.RoadmapPageView.as_view(), name='roadmap'),
    path('feedback/', views.FeedbackPageView.as_view(), name='feedback'),
    path('feedback/list/', views.FeedbackListView.as_view(), name='feedback_list'),
]
