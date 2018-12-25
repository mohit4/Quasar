from django.urls import path

from .views import HomePageView, QuestionDetailsView

app_name = 'ques_app'

urlpatterns = [
    # Home Page
    path('home/', HomePageView.as_view(), name='home'),

    # Single Question Details
    path('question/<int:pk>', QuestionDetailsView.as_view(), name='ques_details'),
]