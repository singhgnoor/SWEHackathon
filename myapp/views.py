from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # This view will find and render the 'hello.html' template.
    return render(request, 'home.html')


def notice(request):
    return None