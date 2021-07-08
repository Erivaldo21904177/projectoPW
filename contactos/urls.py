from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contactos/', views.home_view, name="users"),
    path('contactos/login', views.login_view, name="login"),
    path('contactos/registro', views.register_view, name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
