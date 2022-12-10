from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home),
    path('onas/', views.onas, name="onas"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('kategorie/<slug:val>', views.KategorieView.as_view(), name="kategorie"),
    path('tytul-kategorii/<val>', views.KategorieView.as_view(), name="tytul-kategorii"),
    path('product-desc/<int:pk>', views.ProductDesc.as_view(), name="product-desc"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
