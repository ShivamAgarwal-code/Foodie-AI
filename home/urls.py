from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin', views.login, name='signin'),
    path('profile', views.profile, name='profile'),
    path('home', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('loyalty', views.loyalty, name='loyalty'),
    path('offer', views.offer, name='offer'),
    path('signout', views.logout, name='signout'),
    path('emergency', views.emergency, name='emergency'),
    path('callback', views.callback, name='callback'),
    path('offers', views.offers, name='offers'),
    path('feedback', views.feedback, name='feedback'),
    path('orderhistory', views.orderhistory, name=' orderhistory'),
    path('profile_management', views.profile_management, name='profile_management'),
    
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
]