from django.urls import path
from .views import home, about

urlpatterns = [
    path('', home, name='home'),      # Home page
    path('about/', about, name='about'),  # About page
]
