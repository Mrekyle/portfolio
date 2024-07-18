from django.shortcuts import render

def handler404(request, exception):
    """
        Error 404 handling
    """

    template = 'errors/404.html'

    context = {

    }

    return render(request, template, context)

def handler500(request):
    """
        Error 500 handling
    """

    template = 'errors/500.html'

    context = {

    }

    return render(request, template, context)