from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic
from company.models import Company
from .models import Interview
from .forms import InterviewRegisterForm, InterviewUpdateForm

User = get_user_model()

class InterviewTop(generic.TemplateView):
    template_name = 'interview/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # company_id
        pk = self.kwargs['pk']
        context['company'] = Company.objects.get(id=pk)
        context['interviewes'] = Interview.objects.filter(company_id=pk).values
        return context


class InterviewRegister(generic.View):
    form_class = InterviewRegisterForm
    template_name = 'interview/interview_register.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        company = Company.objects.get(id=pk)
        form = self.form_class
        return render(request, self.template_name, {'form': form, 'company': company})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            pk = self.kwargs['pk']
            company = Company.objects.get(id=pk)
            selection_phase = form.cleaned_data['selection_phase']
            selection_date = form.cleaned_data['selection_date']
            question = form.cleaned_data['question']
            reflection = form.cleaned_data['reflection']
            other = form.cleaned_data['other']
            Interview.objects.create(
                company_id=company,
                selection_phase=selection_phase,
                selection_date=selection_date,
                question=question,
                reflection=reflection,
                other=other,
            )
            return render(request, 'interview/interview_register_complete.html', {'company_id': company.id})
        return render(request, self.template_name, {'form': form})


class InterviewRegisterComplete(generic.TemplateView):
    template_name = 'interview/interview_register_complete.html'
#
#
# class InterviewUpdate(generic.TemplateView):
#     form_class = InterviewUpdateForm
#     template_name = 'interview/interview_update.html'
#
#     def get(self, request, *args, **kwargs):
#         pk = self.kwargs['pk']
#         interview = Interview.objects.get(id=pk)
#         form = self.form_class(instance=interview)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             interview_name = form.cleaned_data['interview_name']
#             pk = self.kwargs['pk']
#             interview = Interview.objects.get(id=pk)
#             interview.company_name = company_name
#             interview.save()
#             return redirect('interview:update_complete')
#         return render(request, self.template_name, {'form': form})
#
#
# class InterviewUpdateComplete(generic.TemplateView):
#     template_name = 'interview/interview_update_complete.html'
#
#
# class InterviewDelete(generic.TemplateView):
#     template_name = 'interview/interview_delete_complete.html'
#
#     def get(self, request, *args, **kwargs):
#         pk = self.kwargs['pk']
#         Interview.objects.get(id=pk).delete()
#         return render(request, self.template_name)