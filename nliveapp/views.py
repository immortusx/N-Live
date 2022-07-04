from urllib import response
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['newsdata'] = inshorts_data
    return render(request, 'index.html', records)

def sports(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def entertainment(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=entertainment"
    response = requests.get(url=url)
    inshrots_data = response.json()
    records['entertainmentdata'] = inshrots_data
    return render(request, 'entertainment.html', records)

def business(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['businessdata'] = inshorts_data
    return render(request, 'business.html', records)

def technology(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=technology"
    response = requests.get(url=url)
    inshort_data = response.json()
    records['technologydata'] = inshort_data
    return render(request, 'technology.html', records)

def startup(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=startup"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['startupdata'] = inshorts_data
    return render(request, 'startup.html', records)

def politics(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['politicsdata'] = inshorts_data
    return render(request, 'politics.html', records)

def education(request):
    records = {}
    url = "https://inshortsapi.vercel.app/news?category=education"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['educationdata'] = inshorts_data
    return render(request, 'education.html', records)

def national(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=national"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['nationaldata'] = inshorts_data
    return render(request, 'national.html', records)

def miscellaneous(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=miscellaneous"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['miscellaneousdata'] = inshorts_data
    return render(request, 'miscellaneous.html', records)

def world(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=world"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['worlddata'] = inshorts_data
    return render(request, 'world.html', records)

def hatke(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=hatke"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['hatkedata'] = inshorts_data
    return render(request, 'hatke.html', records)

def about(request):
    return render(request, 'about.html')


