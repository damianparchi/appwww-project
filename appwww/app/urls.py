from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm

urlpatterns = [
    path('', views.home),
    path('onas/', views.onas, name="onas"),
    path('kontakt/', views.kontakt, name="kontakt"),
    path('kategorie/<slug:val>', views.KategorieView.as_view(), name="kategorie"),
    path('tytul-kategorii/<val>', views.KategorieView.as_view(), name="tytul-kategorii"),
    path('product-desc/<int:pk>', views.ProductDesc.as_view(), name="product-desc"),
    path('register/', views.RegistrationView.as_view(), name='userregister'),
    path('user/login/', auth_view.LoginView.as_view(template_name='app/loginform.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name = 'app/password_reset.html', form_class = MyPasswordResetForm), name='password_reset')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
