from django.conf.urls import url
from hwajong import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]