from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.signing import BadSignature, SignatureExpired, loads, dumps
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.views import generic
from .models import Company
from .forms import CompanyRegisterForm, CompanyUpdateForm

User = get_user_model()

class CompanyTop(generic.TemplateView):
    template_name = 'company/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        context['companies'] = Company.objects.filter(user_id=login_user).values
        return context

class CompanyRegister(generic.View):
    form_class = CompanyRegisterForm
    template_name = 'company/company_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            login_user = request.user
            Company.objects.create(company_name=company_name, user_id=login_user)
            return redirect('company:register_complete')
        return render(request, self.template_name, {'form': form})

class CompanyRegisterComplete(generic.TemplateView):
    template_name = 'company/company_register_complete.html'