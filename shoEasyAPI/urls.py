from django.urls import path
from .views import ProductReview_APIView
from . import views

urlpatterns = [
    path('', ProductReview_APIView.as_view()),
    path('test/', views.test, name='test'),
]