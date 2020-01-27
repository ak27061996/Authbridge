
from django.conf.urls import url, include
from django.contrib import admin
from loanapp.views import loanApply, loanfilter
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^/', loanApply.as_view()),
    url(r'^apply-loan/', loanApply.as_view()),
    url(r'^loan/', loanfilter.as_view()),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),

]
