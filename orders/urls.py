import imp
from django.urls import path
from . import views
from .views import EsewaRequestView, EsewaVerifyView
urlpatterns = [
    path('place_order/', views.place_order, name='place_order'),
    path('esewa-request/', EsewaRequestView.as_view(), name='esewarequest'),
    path('esewa-verify/', EsewaVerifyView.as_view(), name='esewaverify'),


]