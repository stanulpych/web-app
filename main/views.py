from django.views.generic import TemplateView, CreateView, ListView
from . import models


class HomePageView(TemplateView):
    template_name = 'home.html'


class RoadmapPageView(TemplateView):
    template_name = 'roadmap.html'


class FeedbackPageView(CreateView):
    model = models.Feedback
    template_name = 'feedback.html'
    fields = ['name', 'message']
    success_url = '/'


class FeedbackListView(ListView):
    model = models.Feedback
    template_name = 'feedback_list.html'
    context_object_name = 'feedback_list'
