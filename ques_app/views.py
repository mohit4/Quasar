from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from .models import Question, Answer

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'ques_app/home.html'
    
    def get_context_data(self, **kwargs):
        '''
        Overiding the context date sent to template
        '''
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.all()
        return context

class QuestionDetailsView(DetailView):
    template_name = 'ques_app/ques_details.html'
    model = Question