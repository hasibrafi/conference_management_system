from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #login
    path('login/', views.LoginView, name='login'),

    #register
    path('user_registration/', views.UserRegistration, name='user_registration'),

    #name_this_section
    path('service/', views.Services, name='service'),
    path('about_us/', views.AboutUs, name='about_us'),
    path('vcs/', views.VCS, name='vcs'),
    


    #conference
    path('conference/', views.ConferenceModule, name='conference'),
    path('create_conference', views.createConference, name='create_conference'),
    path('conference_list', views.conferenceList, name='conference_list'),
    path('conference_details/<str:id>', views.conferenceDetails, name='conference_details'),

    path('view_conferences', views.viewConferences, name='view_conferences'),

    #abstract
    path('upload_abstract/<str:id>', views.uploadAbstract, name='upload_abstract'),

    path('abstract_list/<str:id>', views.abstractList, name='abstract_list'), 
    path('abstract_paper_list/<str:id>', views.abstractpaperList, name='abstract_paper_list'),

    #reviewer
    path('reviewer/', views.ReviewerMain, name='reviewer'),  

    #other_rename_this_section
    path('epic_series/', views.epicSeries, name='epic_series'), 
    path('kalpa_publications/', views.kalpaPublications, name='kalpa_publications'), 
    path('preprints/', views.Preprint, name='preprints'), 
    path('author/', views.Author, name='author'), 
    path('editor/', views.Editor, name='editor'),  


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)