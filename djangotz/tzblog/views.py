from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import *


class UserCreateView(CreateView):
    model = TzUser
    form_class = TzUserForm
    success_url = '/login'
    template_name = 'register.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'


class PostsListView(ListView):
    model = Post
    template_name = 'main.html'
    login_url = 'login/'
    paginate_by = 5


class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login/'
    form_class = PostCreateForm
    success_url = '/'
    template_name = 'postcreate.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        messages.add_message(self.request, messages.INFO, 'Пост успешно создан')
        obj.save()
        return super().form_valid(form=form)


class MainPostListView(ListView):
    model = Post
    template_name = 'mainpost.html'
    login_url = 'login/'
    extra_context = {'comment_form': CommentCreateForm}

    def get_queryset(self):
        return super().get_queryset().filter(id=self.request.GET['post_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MainPostListView, self).get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(post_id=self.request.GET['post_id'])
        return context


class CreateCommentView(CreateView):
    form_class = CommentCreateForm
    success_url = '/'

    def form_valid(self, form):
        object = form.save(commit=False)
        object.post_id = self.request.POST['post_id']
        object.author_id = self.request.POST['author_id']
        object.save()
        return super().form_valid(form=form)


class MyPostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'myposts.html'
    login_url = 'login/'
    paginate_by = 5

    def get_queryset(self):
        return super().get_queryset().filter(author=self.request.user)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    login_url = 'login/'
    form_class = PostCreateForm
    success_url = '/'
    template_name = 'postupdate.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form=form)


class DeletePostView(PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'is_superuser'
    success_url = '/'
