from django.shortcuts import render
from django.views.generic import TemplateView
from charity.models import Donation, Institution
from django.core.paginator import Paginator
# Create your views here.

class LandingPageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['count_donation'] = Donation.count_bags()
        context['count_institution'] = Institution.objects.count()
        
        context['fundacja'] = Institution.objects.filter(type="fundacja")
        context['organizacja'] = Institution.objects.filter(type="organizacja")
        context['zbiorka'] = Institution.objects.filter(type="zbiorka")

        return context

class AddDonationView(TemplateView):
    template_name = 'addDonation.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class RegisterView(TemplateView):
    template_name = 'register.html'

class FormView(TemplateView):
    template_name = 'form.html'
