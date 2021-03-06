import conference
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *
from .decorators import *

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

#login
@unauthenticated_user
def LoginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}, you are at index page!')
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'login/login.html', context)

#logout
def LogoutView(request):
    logout(request)
    return redirect('index')


#Register
@unauthenticated_user
def UserRegistration(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user}, your account has been created!')
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/user_registration.html', context)

#profile
def ProfileView(request):
    if request.user.is_authenticated:
        user = request.user
        group = request.user.groups.all()[0]
        context = {'user':user, 'group':group}
        return render(request, 'profile/profile.html', context)
    return render(request, 'profile/profile.html')


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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','host'])
def createConference(request):
    form = ConferenceForm()
    context = {'form': form}
    return render(request, 'conference/create_conference.html', context)

#optimize this view function
@login_required(login_url='login')
def conferenceList(request):
    form = ConferenceForm()
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_conferences')
    
    # abstracts = AbstractPaper.objects.all()
    # abstract_count = abstracts.count()

    latest_conferences = Conference.objects.order_by('-first_day')[:25]
    context = {'conference': conference, 'latest_conferences': latest_conferences}

    return render(request, 'conference/conference_list.html', context)

def conferenceDetails(request, id):
    conference = get_object_or_404(Conference, id=id)
    context = {'conference': conference}

    return render(request, 'conference/conference_details.html', context)

def viewConferences(request):
    latest_conferences = Conference.objects.order_by('-first_day')[:25]

    # abstracts = Conference.AbstractPaper.objects.all()
    # abstract_count = abstracts.count()
    
    context = {'latest_conferences': latest_conferences}
    return render(request, 'conference/view_conference_list.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','author'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','host','reviewer'])
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


