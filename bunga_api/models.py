from django.db import models

class Bunga(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField()

    def __str__(self):
        return self.nama

class Pemesanan(models.Model):
    bunga = models.ForeignKey(Bunga, related_name='pemesanan', on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, related_name='pemesanan', on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    tanggal_pemesanan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pemesanan {self.jumlah} {self.bunga.nama} oleh {self.pelanggan.nama}"
