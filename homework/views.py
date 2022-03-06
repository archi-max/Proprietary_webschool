from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, FormView, DeleteView
from .models import Work, Submission
from .forms import SubmissionForm, WorkForm
# Create your views here.
from django import template
register = template.Library()

def get_submission_file(work, user):
    submission = Submission.objects.filter(work_id=work.id, student_id=user.id)
    if submission:
        return submission[0].file
    else:
        return None


@register.filter
def submission_file(work, user):
    return get_submission_file(work, user)

class SubmissionFormView(FormView):
    model = Submission
    form_class = SubmissionForm
    fields = ['file']
    template_name = 'backend/form_error.html'
    success_url = '/formsuccess/'

    def form_valid(self, form):
        # submission = form.save(commit=False)
        # submission.student, submission.work = /self.request.user, Work.objects.get(id=self.kwargs["pk"])
        # submission.save()
        sub, _ = Submission.objects.get_or_create(student_id=self.request.user.id, work_id=self.kwargs["pk"])
        sub.file = form.cleaned_data['file']
        sub.save()
        return super().form_valid(form)


class WorkFormView(FormView):
    model = Work
    form_class = WorkForm
    template_name = 'backend/form_page.html'
    success_url = '/formsuccess/'

    def form_valid(self, form):
        work = form.save(commit=False)
        work.created_by = self.request.user
        work.save()
        for grp in form.cleaned_data['groups']:
            work.groups.add(grp)
        work.save()
        return super().form_valid(form)

class WorkListView(ListView):
    model = Work
    template_name = 'homework/documents.html'
    success_url = '/homework/'
    context_object_name = 'homeworks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dat = []
        for hw in context['homeworks']:
            sf = get_submission_file(hw, self.request.user)
            dat.append((sf, hw))
        print(dat)
        context['homeworks'] = dat
        context['create_form'] = WorkForm()
        return context

    def get_queryset(self):
        if self.request.user.user_type == self.request.user.TEACHER:
            return Work.objects.filter(created_by=self.request.user.id).order_by('-updated_at')
        else:
            return Work.objects.filter(groups__in=self.request.user.groups.all()).order_by('-updated_at').distinct()

class SubmissionListView(ListView):
    model = Submission
    template_name = 'homework/submissions.html'
    context_object_name = 'submissions'
    def get_queryset(self):
        if self.request.user.user_type == self.request.user.TEACHER:
            return Submission.objects.filter(work=self.kwargs['pk']).order_by('-updated_at')


class WorkDeleteView(DeleteView):
    model = Work
    template_name = 'homework/documents.html'
    success_url = '/homework/'

