from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views import generic
from .models import Answer
from .forms import AnswerRegisterForm, AnswerUpdateForm

User = get_user_model()

class AnswerTop(generic.TemplateView):
    template_name = 'answer/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        login_user = self.request.user
        context['answeres'] = Answer.objects.filter(user_id=login_user).values
        return context


class AnswerRegister(generic.View):
    form_class = AnswerRegisterForm
    template_name = 'answer/answer_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            login_user = request.user
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            Answer.objects.create(
                user_id=login_user,
                question=question,
                answer=answer
            )
            return render(request, 'answer/answer_register_complete.html')
        return render(request, self.template_name, {'form': form})


class AnswerRegisterComplete(generic.TemplateView):
    template_name = 'answer/answer_register_complete.html'


class AnswerUpdate(generic.TemplateView):
    form_class = AnswerUpdateForm
    template_name = 'answer/answer_update.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        answer = Answer.objects.get(id=pk)
        form = self.form_class(instance=answer)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            question = form.cleaned_data['question']
            pk = self.kwargs['pk']
            answer_obj = Answer.objects.get(id=pk)
            answer_obj.answer = answer
            answer_obj.question = question
            answer_obj.save()
            return redirect('answer:update_complete')
        return render(request, self.template_name, {'form': form})


class AnswerUpdateComplete(generic.TemplateView):
    template_name = 'answer/answer_update_complete.html'


class AnswerDelete(generic.TemplateView):
    template_name = 'answer/answer_delete_complete.html'

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Answer.objects.get(id=pk).delete()
        return render(request, self.template_name)