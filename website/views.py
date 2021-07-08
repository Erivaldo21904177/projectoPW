from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_page_view, name="base"),
    path('', views.index_page_view, name="index"),
    path('', views.informacoes_page_view, name="informacoes"),
    path('', views.material_page_view, name="material"),
    path('', views.multimedia_page_view, name="multimedia"),
    path('', views.quizz_page_view, name="quizz"),
]