from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from .models import Post
from .forms import PostForm


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/announcements.html'
    context_object_name = "announcements"
    def get_queryset(self):
        return Post.objects.filter(groups__in=self.request.user.groups.all()).order_by('-updated_at').distinct()


class PostFormView(FormView):
    template_name = 'posts/post_form.html'
    form_class = PostForm
    success_url = '/posts/'

    def form_valid(self, form):
        post = form.save(user=self.request.user, commit=True)
        for grp in form.cleaned_data['groups']:
            post.groups.add(grp)
        post.save()
        return super().form_valid(form)


class PostsCreatedViews(PostListView):

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user).order_by('-updated_at')


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    success_url = '/posts/'
    # exclude = ['created_by', 'created_at', 'updated_at']
    fields = ['title', 'description', 'file', 'tags', 'groups', 'is_active']
