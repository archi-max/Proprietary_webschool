from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Class, Event
from .forms import ClassCreateForm, EventCreateForm
from django.contrib.auth import get_user_model
from datetime import datetime
from django.db.models import Q

User = get_user_model()

# Create your views here
def get_classes(user):
    if user.user_type == User.TEACHER:  # Show Classes For the Day
        q = Class.objects.filter(event__created_by=user)
    else:
        q = Class.objects.filter(groups__in=user.groups.all())
    return q

class EventCreateView(FormView):
    model = Event
    form_class = EventCreateForm
    template_name = 'backend/form_page.html'
    success_url = '/formsuccess/'

    def form_valid(self, form):
        event = form.save(commit=False)
        event.created_by = self.request.user
        event.save()
        for grp in form.cleaned_data['groups']:
            event.groups.add(grp)

        event.save()
        return super().form_valid(form)

class EventListView(ListView):
    model = Event
    template_name = 'classes/list.html'
    context_object_name = 'events'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_form'] = EventCreateForm()
        return context

    def get_queryset(self):
        return Event.objects.filter(Q(groups__in=self.request.user.groups.all()) |
                                    Q(created_by=self.request.user)).distinct()


class ClassJoinView(DetailView):
    model = Class
    template_name = 'classes/object_view.html'

    def dispatch(self, request, *args, **kwargs):
        cls = self.get_object()
        if not(any([cls.is_today, cls.starts_at <= datetime.now().time()])):
            return self.render_to_response({'error': 'Class is not available'})
        return super().dispatch(request, *args, **kwargs)