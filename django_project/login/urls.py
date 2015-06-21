from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_index, name='user_landing'),
    url(r'^denied', views.denied, name='denied_user'),
]
