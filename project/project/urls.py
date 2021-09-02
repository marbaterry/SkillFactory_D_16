"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import *
from CallBoard.views import *
from CallBoard.feed import LatestEntriesFeed
from django.conf.urls import url
from froala_editor import views


urlpatterns = [
    # path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='category/')),
    # path('category/', CategoryListView.as_view()),
    # path('post/', PostListView.as_view()),
    # path('post/new/', PostCreateView.as_view()),
    # path('post/<int:pk>/', PostDetailView.as_view()),
    # path('post/<int:pk>/edit', PostUpdateView.as_view()),
    # url(r'^latest/feed/', LatestEntriesFeed()),
    # # url(r'^category/(?P<sub_name>[-\w]+)/$', category, name='category'),

    path('category/', CategoryListView.as_view()),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<slug:slug>/<int:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('category/<slug:slug>/new_post', PostCreateView.as_view(), name='new_post'),
    path('froala_editor/', include('froala_editor.urls')),

    # path('response/new_resp/', ResponseCreateView.as_view(), name='new_response'),
    # path('response/<int:pk>/', ResponseDetailView.as_view(), name='detail_response'),
    path('category/<slug:slug>/<int:pk>/new_comment', CommentCreateView.as_view(), name='new_comment'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(),  name='profile'),
    # path('category/<slug:slug>/<int:pk>/edit', CommentUpdateView.as_view(), name='edit_post'),
    path('profile/comment/', comment_list,  name='comment_list'),
    path('profile/comment/<int:pk>/', CommentUpdateView.as_view(),  name='edit_post'),

]
