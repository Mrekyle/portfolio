from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from django.core.mail import send_mail

# Create your views here.

def index(request):
    """
        Index page
    """

    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        subject_line = f"New contact request from {name}"
        send_copy = request.POST.get('send_copy')

        contact_email = f"""
                New contact request from : {name}. 

                ====================================
                Subject : {subject}.

                {message}.

                ====================================

                You can contact them at: {email}
            """

        if send_copy == 'on':
            send_mail(
                subject=subject_line,
                message=contact_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )
            messages.success(request, f"Thank you {name}. Your email was sent successfully.")
            return redirect('index')
        else:
            send_mail(
                subject=subject_line,
                message=contact_email,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[email]
            )
            messages.success(request, f"Thank you {name}. Your email was sent successfully.")
            return redirect('index')


    template = 'index.html'

    context = {

    }

    return render(request, template, context)