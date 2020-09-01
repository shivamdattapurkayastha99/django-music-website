
from django.urls import path
from . import views

urlpatterns = [
    path('songs',views.songs,name='songs'),
    path('songs/<int:id>',views.songpost,name='songpost'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('watchlater',views.watchlater,name='watchlater'),

    
]
