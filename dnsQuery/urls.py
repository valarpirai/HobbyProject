from django.conf.urls import url

from dnsQuery import views

urlpatterns = [
    url(r'^', views.home),
]
