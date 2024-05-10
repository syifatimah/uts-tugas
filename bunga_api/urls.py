from django.urls import path
from . import views

urlpatterns = [
    path('bunga/', views.BungaListCreate.as_view(), name='bunga-list-create'),
    path('pelanggan/', views.PelangganListCreate.as_view(), name='pelanggan-list-create'),
    path('pemesanan/', views.PemesananListCreate.as_view(), name='pemesanan-list-create'),
]
