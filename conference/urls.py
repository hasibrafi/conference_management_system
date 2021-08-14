from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_conference', views.createConference, name='create_conference'),
    path('conference_list', views.conferenceList, name='conference_list'),
    path('conference_details/<str:id>', views.conferenceDetails, name='conference_details'),

    path('view_conferences', views.viewConferences, name='view_conferences'),
    path('upload_abstract/<str:id>', views.uploadAbstract, name='upload_abstract'),

    path('abstract_list/<str:id>', views.abstractList, name='abstract_list'),   

] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)