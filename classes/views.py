from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Class, Event
from .forms import ClassCreateForm
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# Create your views here
def get_classes(user):
    if user.user_type == User.TEACHER:  # Show Classes For the Day
        q = Class.objects.filter(event__created_by=user)
    else:
        q = Class.objects.filter(groups__in=user.groups.all())
    return q

class ClassCreateView(FormView):
    model = Class
    template_name = 'classes/form.html'
    form_class = ClassCreateForm
    success_url = '/classes/'

    def form_valid(self, form):
        cls = form.save(commit=False)
        cls.created_by = self.request.user
        cls.save()
        return super().form_valid(form)


class ClassUpdateView(UpdateView):
    model = Class
    template_name = 'classes/form.html'
    fields = ['subject','starts_at','days','groups']
    success_url = '/classes/'


class ClassListView(ListView):
    model = Event
    template_name = 'classes/list.html'
    context_object_name = 'events'

    def get_queryset(self):
        return Event.objects.filter(groups__in=self.request.user.groups.all()).distinct()


class DayClassListView(ListView):
    model = Class
    template_name = 'classes/list.html'


    def get_queryset(self):
        q = get_classes(self.request.user).distinct()
        q = [obj for obj in q if obj.is_on_day(self.kwargs['day'])]
        return q

class ClassJoinView(DetailView):
    model = Class
    template_name = 'classes/object_view.html'

    def dispatch(self, request, *args, **kwargs):
        cls = self.get_object()
        if not(any([cls.is_today, cls.starts_at <= datetime.now().time()])):
            return self.render_to_response({'error': 'Class is not available'})
        return super().dispatch(request, *args, **kwargs)