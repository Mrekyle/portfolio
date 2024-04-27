from django.shortcuts import render

def handler404(request, exception):
    """
        Error 404 handling
    """

    template = 'errors/404.html'

    context = {

    }

    return render(request, template, context)