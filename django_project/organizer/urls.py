from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.organizer_index, name='organizer_landing'),
]
