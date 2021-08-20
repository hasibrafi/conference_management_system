import conference
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import AbstractPaper, Conference

# Create your views here.

def index(request):
    context = {
        'name': 'Rafi',
    }
    return render(request, 'index.html', context)

#login
def LoginView(request):
    context = {
        'name': 'Rafi',
    }
    return render(request, 'login/login.html', context)

#Register
def UserRegistration(request):
    context = {
        'name': 'Rafi',
    }
    return render(request, 'registration/user_registration.html', context)


def Services(request):
    context = {}
    return render(request, 'services/services.html', context)

def AboutUs(request):
    context = {}
    return render(request, 'about/about_us.html', context)

def VCS(request):
    context = {}
    return render(request, 'vcs/vcs.html', context)

def ConferenceModule(request):
    context = {
        'name': 'Rafi',
    }
    return render(request, 'conference/conference.html', context)



def createConference(request):
    message = 'This is the conference creation page.'
    

    return render(request, 'conference/create_conference.html', context={'message': message})


def conferenceList(request):
    if request.method == 'POST':
        type = request.POST['type']
        title = request.POST['title']
        acronym = request.POST['acronym']
        webpage = request.POST['webpage']
        venue = request.POST['venue']
        city = request.POST['city']
        country = request.POST['country']
        est_submissions = request.POST['noofsubmissions']
        firstday = request.POST['firstday']
        lastday = request.POST['lastday']
        primaryarea = request.POST['primary_area']
        secondaryarea = request.POST['secondary_area']
        areanotes = request.POST['areanotes']
        organizer = request.POST['organizer']
        org_webpage = request.POST['org_webpage']
        phoneno = request.POST['phoneno']
        role = request.POST['role']
        otherinfo = request.POST['otherinfo']

        conference = Conference(type= type, title= title, acronym= acronym, web_page= webpage,
                     venue = venue, city = city, country = country, est_submissions = est_submissions, 
                     first_day = firstday, last_day = lastday, primary_area = primaryarea,
                     secondary_area = secondaryarea, area_notes = areanotes, organizer = organizer,
                     organizer_webpage = org_webpage
                     )

        conference.save()

        latest_conferences = Conference.objects.order_by('-first_day')[:25]
        context = {'conference': conference, 'latest_conferences': latest_conferences}

        return render(request, 'conference/conference_list.html', context)

def conferenceDetails(request, id):
    conference = get_object_or_404(Conference, id=id)
    context = {'conference': conference}

    return render(request, 'conference/conference_details.html', context)

def viewConferences(request):
    latest_conferences = Conference.objects.order_by('-first_day')[:25]
    
    context = {'latest_conferences': latest_conferences}
    return render(request, 'conference/view_conference_list.html', context)

def uploadAbstract(request, id):

    conference = get_object_or_404(Conference, id=id)
    context = {'conference': conference}

    return render(request, 'conference/author_participation.html', context)

def abstractList(request, id):
    conference = get_object_or_404(Conference, id=id)

    if request.method == 'POST':
        name = request.POST['author_name']
        title = request.POST['research_title'] 
        #abstract_file = request.POST['abstract_file']
        uploaded_file = request.FILES['abstract_file']
        print(uploaded_file.name, uploaded_file.size)
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(file_name)
        
        abstract_paper = AbstractPaper(conference=conference, author_name=name, paper_title=title, abstract_file=uploaded_file)
        abstract_paper.save()

        context = {'conference': conference, 'abstract_paper': abstract_paper, 
                   'uploaded_file': uploaded_file, 'file_name': file_name, 'url': url}

    return render(request, 'conference/abstract_list.html', context)


def abstractpaperList(request, id):
    conference = Conference.objects.get(id=id)
    abstractpapers = AbstractPaper.objects.filter(conference__id=id)
    #abstractpapers = conference.abstractpapers_set.all()
    print(abstractpapers)
    context = {'conference': conference, 'abstractpapers': abstractpapers}

    return render(request, 'conference/abstract_paper_list.html', context)

#reviewer
def ReviewerMain(request):
    context = {}
    return render(request, 'reviewer/reviewer.html', context)

def epicSeries(request):
    context = {}
    return render(request, 'epic/epic_series.html', context)

def kalpaPublications(request):
    context = {}
    return render(request, 'kalpa_publications/kalpa_publications.html', context)

def Preprint(request):
    context = {}
    return render(request, 'preprints/preprints.html', context)

def Author(request):
    context = {}
    return render(request, 'author/author.html', context)

def Editor(request):
    context = {}
    return render(request, 'editor/editor.html', context)


