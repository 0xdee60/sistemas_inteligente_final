from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("",views.home_prueba, name='home_prueba'),
    path("realizar_prueba/", views.realizar_prueba, name="realizar_prueba"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




