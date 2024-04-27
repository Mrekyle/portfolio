from django.shortcuts import render

# Create your views here.

def index(request):
    """
        Index page
    """

    template = 'index.html'

    context = {

    }

    return render(request, template, context)