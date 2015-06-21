from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.login_index, name='login_landing'),
]
