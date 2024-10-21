from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from .settings import DEBUG
from django.contrib.sitemaps.views import sitemap  # Sitemap için import
from .sitemaps import ProductSitemap  # Sitemap sınıfınızı ekleyin
from products.views import product_detail, products
from .views import home
from django.conf import settings

sitemaps = {
    "products": ProductSitemap,
}

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("products/", products, name="product_list"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path("<slug:code>/", product_detail, name="product_detail"),
]
if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
