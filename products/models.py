from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=32)
    brand = models.CharField(max_length=32)
    code = models.CharField(max_length=32, unique=True)
    isActive = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)  # Son güncelleme zamanı

    def save(self, *args, **kwargs):
        # Alanları düzenle ve büyük/küçük harfe uygun şekilde kaydet
        self.name = self.name.upper()
        self.brand = self.brand.upper()
        self.code = self.code.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # Her ürünün detay sayfasının URL'sini döndür
        return reverse("product_detail", args=[self.code])

    class Meta:
        verbose_name_plural = "Ürünler"
        verbose_name = "Ürün"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="products/"
    )  # Resimler "products" klasörüne kaydedilecek

    def __str__(self):
        return f"{self.product.name} - {self.id}"

    class Meta:
        verbose_name_plural = "Ürün Resimleri"
        verbose_name = "Ürün Resmi"
