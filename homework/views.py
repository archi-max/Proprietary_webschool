from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
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

class SubmissionCreateView(CreateView):
    model = Submission
    form = SubmissionForm
    fields = ['file']
    template_name = 'homework/form.html'
    success_url = '/homework/'

    def form_valid(self, form):
        submission = form.save(commit=False)
        submission.student, submission.work = self.request.user, Work.objects.get(id=self.kwargs["pk"])
        submission.save()
        return super().form_valid(form)


class WorkCreateView(CreateView):
    model = Work
    form = WorkForm
    fields = ['title', 'description',  'upload_by', 'groups', 'work_type']
    template_name = 'homework/form.html'
    success_url = '/homework/'

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
        # context['submission_form'] = SubmissionForm()
        # context['submission_file'] = lambda x: get_submission_file(x, self.request.user)
        return context

    def get_queryset(self):
        if self.request.user.user_type == self.request.user.TEACHER:
            return Work.objects.filter(created_by=self.request.user.id).order_by('-updated_at')
        else:
            return Work.objects.filter(groups__in=self.request.user.groups.all()).order_by('-updated_at').distinct()

class SubmissionListView(ListView):
    model = Submission
    template_name = 'homework/documents.html'
    success_url = '/homework/'

    def get_queryset(self):
        if self.request.user.user_type == self.request.user.TEACHER:
            return Submission.objects.filter(work=self.kwargs['pk']).order_by('-updated_at')
        # else:
        #     return Submission.objects.filter(student=self.request.user.id)

class WorkUpdateView(UpdateView):
    model = Work
    fields = ['title', 'description',  'upload_by', 'groups', 'work_type']
    template_name = 'homework/create.html'
    success_url = '/homework/'

class SubmissionUpdateView(UpdateView):
    model = Submission
    fields = ['file']
    template_name = 'homework/form.html'
    success_url = '/homework/'


