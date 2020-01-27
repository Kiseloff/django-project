from django.urls import path
from testurlapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^user/(\d+)/$', views.home, name='home'),
]