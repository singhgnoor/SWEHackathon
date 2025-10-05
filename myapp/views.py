from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # This view will find and render the 'hello.html' template.
    return render(request, 'home.html')


def notice(request):
    return render(request, 'notice.html')


def timetable(request):
    return render(request, 'timetable.html')


def events(request):
    return render(request, 'events.html')


def resources(request):
    return render(request, 'resources.html')


def career(request):
    return render(request, 'career.html')


def achive(request):
    return render(request, 'achive.html')