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
    organizacja_paginator = Paginator(organizacja, 5)
    zbiorka_paginator = Paginator(zbiorka, 5)
    
    fun_page_num = request.GET.get('fun_page')
    org_page_num = request.GET.get('org_page')
    zbi_page_num = request.GET.get('zbi_page')
    
    fundacja_page = fundacja_paginator.get_page(fun_page_num)
    organizacja_page = organizacja_paginator.get_page(org_page_num)
    zbiorka_page = zbiorka_paginator.get_page(zbi_page_num)
    
    
    context = { 'count_donation': count_donation,
                'count_institution': count_institution,
                'fundacja': fundacja_page,
                'organizacja': organizacja_page, 
                'zbiorka': zbiorka_page
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
