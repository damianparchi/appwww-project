from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('kategorie/<slug:val>', views.KategorieView.as_view(), name="kategorie"),
]
