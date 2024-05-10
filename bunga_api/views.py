from rest_framework import generics
from .models import Bunga, Pemesanan, Pelanggan
from .serializers import BungaSerializer, PemesananSerializer, PelangganSerializer

class BungaListCreate(generics.ListCreateAPIView):
    queryset = Bunga.objects.all()
    serializer_class = BungaSerializer

class PelangganListCreate(generics.ListCreateAPIView):
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer

class PemesananListCreate(generics.ListCreateAPIView):
    queryset = Pemesanan.objects.all()
    serializer_class = PemesananSerializer
