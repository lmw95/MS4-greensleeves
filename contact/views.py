from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactForm
from .models import Contact


def contact(request):
    """Renders contact form page"""
    return render(request, 'contact/contact.html')