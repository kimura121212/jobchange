from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
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


class CompanyUpdate(generic.TemplateView):
    form_class = CompanyUpdateForm
    template_name = 'company/company_update.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        company = Company.objects.get(id=pk)
        form = self.form_class(instance=company)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            pk = self.kwargs['pk']
            company = Company.objects.get(id=pk)
            company.company_name = company_name
            company.save()
            return redirect('company:update_complete')
        return render(request, self.template_name, {'form': form})


class CompanyUpdateComplete(generic.TemplateView):
    template_name = 'company/company_update_complete.html'


class CompanyDelete(generic.TemplateView):
    template_name = 'company/company_delete_complete.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Company.objects.get(id=pk).delete()
        return render(request, self.template_name)
