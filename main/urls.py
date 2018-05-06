
from django.urls import path

from . import views

urlpatterns = [
    # Class based
    path('', views.HomeView.as_view(), name='index'),

    # Function based
    # path('', views.index, name='index'),
]