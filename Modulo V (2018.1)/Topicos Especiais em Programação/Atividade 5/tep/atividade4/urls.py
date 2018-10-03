"""atividade4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from users import views
from tep import views as viewstep
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.authtoken import views as rest_framework_views
from users.views import TokenCustom, ApiRoot
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ApiRoot.as_view()),
    path('get_auth_token/',  TokenCustom.as_view(), name='get_auth_token'),
    path('servidor/profiles/', views.user_list.as_view(), name=views.user_list.name),
    path('servidor/profiles/<int:pk>/', views.user_detail.as_view(), name=views.user_detail.name),
    path('servidor/profiles/<int:pk>/detail', views.user_detail_count.as_view(), name=views.user_detail.name),
    path('servidor/profile-posts/<int:pk>/', views.profile_user_detail.as_view(), name="detail-profile"),
    path('servidor/profile-posts/', views.profile_user_list.as_view(), name=views.profile_user_list.name),
    path('servidor/profiles/<int:pk>/posts', viewstep.posts_user.as_view(), name='list-post-user'),
    path('servidor/profiles/<int:pk>/posts/<int:post_id>/', viewstep.posts_user_detail.as_view(), name='post-user-detail'),
    path('servidor/profiles/<int:pk>/posts/<int:post_id>/comments/', viewstep.comment_list.as_view(), name='post-user-detail-comment'),
    path('servidor/profiles/<int:pk>/posts/<int:post_id>/comments/<int:comment_id>', viewstep.posts_comment_detail.as_view(), name='post-user-detail-comment'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
