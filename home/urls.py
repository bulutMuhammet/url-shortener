from django.urls import path
from home.views import ShortenURL, ShortenURLTemplateView, RedirectURLView

urlpatterns = [
    path('api',ShortenURL.as_view(),name='create_short_url_api'),
    path('<str:short_code>', RedirectURLView.as_view(), name='get_original_url'),
    path('',ShortenURLTemplateView.as_view(),name='create_short_url'),


]
