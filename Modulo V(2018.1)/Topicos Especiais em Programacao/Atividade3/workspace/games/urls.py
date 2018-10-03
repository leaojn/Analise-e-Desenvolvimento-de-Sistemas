"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from games import views

urlpatterns = [
    path('games/', views.game_list.as_view(),name=views.game_list.name),
    path('games/<int:pk>/', views.game_detail.as_view(), name=views.game_detail.name),
    path('gamescategory/', views.game_category_list.as_view(), name=views.game_category_detail.name),
    path('gamescategory/<int:pk>/', views.game_category_detail.as_view(), name=views.game_category_detail.name),
    path('score/', views.score_list.as_view(), name=views.score_list.name),
    path('score/<int:pk>/', views.score_detail.as_view(), name=views.score_detail.name),
    path('player/', views.player_list.as_view(), name=views.player_list.name),
    path('player/<int:pk>/', views.player_detail.as_view(), name=views.player_detail.name),
]
