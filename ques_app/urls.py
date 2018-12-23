from django.urls import path

from .views import HomePageView

app_name = 'ques_app'

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
]