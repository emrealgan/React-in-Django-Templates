from django.contrib.sitemaps import Sitemap
from products.models import Product

class ProductSitemap(Sitemap):
    changefreq = "daily"  
    priority = 0.8

    def items(self):
        return Product.objects.filter(isActive=True)

    def lastmod(self, obj):
        return obj.updated_at


