from django.urls import path
from django.conf.urls import url
from chat_app import views
from account import views as account_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),


]
