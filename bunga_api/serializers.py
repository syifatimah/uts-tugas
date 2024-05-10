from rest_framework import serializers
from .models import Bunga, Pemesanan, Pelanggan

class BungaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bunga
        fields = '__all__'

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = '__all__'

class PemesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pemesanan
        fields = '__all__'
