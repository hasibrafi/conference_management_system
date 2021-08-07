from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_conference', views.createConference, name='create_conference'),
    path('conference_list', views.conferenceList, name='conference_list'),
    path('conference_details/<str:id>', views.conferenceDetails, name='conference_details'),
]