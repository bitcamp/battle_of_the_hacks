from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_index, name='login_landing'),
    url(r'^check_email', views.check_email, name='login_check_email'),
]
