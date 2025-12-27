from django.views.generic import TemplateView
from charity.models import Donation, Institution
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.

def landing_page(request):

    count_donation = Donation.count_bags()
    count_institution = Institution.objects.count()
    
    fundacja = Institution.objects.filter(type="fundacja")
    organizacja = Institution.objects.filter(type="organizacja")
    zbiorka = Institution.objects.filter(type="zbiorka")
    
    fundacja_paginator = Paginator(fundacja, 5)
    
    
    context = { 'count_donation': count_donation,
                'count_institution': count_institution,
                'fundacja': fundacja,
                'organizacja': organizacja, 
                'zbiorka': zbiorka
               }
    
    return render(request, 'base.html', context)


class AddDonationView(TemplateView):
    template_name = 'addDonation.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class FormView(TemplateView):
    template_name = 'form.html'
