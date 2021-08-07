import conference
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .models import Conference

# Create your views here.

def index(request):
    context = {
        'name':'Rafi',
        'university': 'American International University Bangladesh',
        'age' : 26,
        'city': 'Dhaka',
        'country': 'Bangladesh',
        'passion':'Data Science',
    }
    return render(request, 'index.html', context)

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

        latest_conferences = Conference.objects.order_by('-first_day')[:50]
        context = {'conference': conference, 'latest_conferences': latest_conferences}

    return render(request, 'conference/conference_list.html', context)

def conferenceDetails(request, id):
    conference = get_object_or_404(Conference, id=id)
    context = {'conference': conference}

    return render(request, 'conference/conference_details.html', context)
