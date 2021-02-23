from django.urls import path
from . import views
from .views import PetDetail, PetCreate
from django.conf.urls.static import static
from django.conf import settings

app_name = 'shelter'

urlpatterns = [
   path('', views.index, name="index"),
   path('contacts/', views.contact, name="contact"),
   path('pet/<int:pk>/detail/', PetDetail.as_view(), name='pet_detail'),
   path('about/', views.about, name='about'),
   path('create/', PetCreate.as_view(), name='create'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)