from django.contrib.sitemaps import Sitemap
from products.models import Product

class ProductSitemap(Sitemap):
    changefreq = "daily"  # İçerik değişim sıklığı
    priority = 0.8  # Sayfa önceliği (0 ile 1 arasında)

    def items(self):
        return Product.objects.filter(isActive=True)  # Yalnızca aktif ürünleri ekle

    def lastmod(self, obj):
        return obj.updated_at  # Ürünlerin son güncelleme tarihi
