from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """Renders contact form page"""
    contact_request = None
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_request = contact_form.save(commit=False)
            if request.user.is_authenticated:
                contact_request.user = request.user
            contact_request.save()
            user_email = contact_request.email_address
            subject = render_to_string(
                'contact/confirmation_emails/contact_confirmation_subject.txt',
                {'contact_request': contact_request})
            body = render_to_string(
                'contact/confirmation_emails/contact_confirmation_body.txt',
                {'contact_request': contact_request, 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
                fail_silently=False
            )
            messages.success(request, 'Your query was submitted successfully.')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'Your query could not be sent! Please try again.')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
