from django.shortcuts import render
from django.views.generic import *
from .models import *
from .filters import *
from .forms import *
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.urls import reverse
from froala_editor.widgets import FroalaEditor
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category
    paginate_by = 2


    def get_context_data(self, **kwargs):
        category = Category.objects.get(slug=(self.kwargs['slug']))
        context = super().get_context_data(**kwargs)
        context['Post_list'] = Post.objects.filter(postCategory=category)
        paginate_by = 2
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        post = self.object.id
        context = super().get_context_data(**kwargs)
        response_list = Comment.objects.filter(commentPost=post)
        context['response'] = response_list
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['postTitle', 'content']

    def form_valid(self, form):
        obj = form.save(commit=False)
        category = Category.objects.filter(slug=(self.kwargs['slug'])).values('id')
        obj.postCategory_id = category
        obj.postUser_id = self.request.user.id
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('detail_post', args=(self.kwargs['slug'], self.object.id))


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['commentText']

    def form_valid(self, form):
        print(self.kwargs)
        obj = form.save(commit=False)
        obj.commentPost_id = self.kwargs['pk']
        obj.commentUser_id = self.request.user.id
        return super(CommentCreateView, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('detail_post', args=(self.kwargs['slug'], self.kwargs['pk']))


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_context_data(self, **kwargs):
        request = self.request.user.id
        user = self.object.id
        if user == request:
            context = super().get_context_data(**kwargs)
            post_list = Post.objects.filter(postUser=user)
            comment_list = Comment.objects.filter(commentUser=user)
            print(post_list)
            print(comment_list)
            context['post'] = post_list
            context['comment'] = comment_list
            return context
        else:
            raise Http404("User does not exist")


class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['commentAllow']

    def get_success_url(self):
        print(self)
        return reverse('detail_post', args=(self.kwargs['slug'], self.kwargs['pk']))


def comment_list(request):
    user = request.user.id
    comments = Comment.objects.filter(commentUser=user)
    context = {
        'comments': comments,
    }
    return render(request, "CallBoard/comment_list.html", context)


def post_list(request):
    user = request.user.id
    comments = Comment.objects.filter(commentUser=user)
    context = {
        'comments': comments,
    }
    return render(request, "CallBoard/comment_list.html", context)








