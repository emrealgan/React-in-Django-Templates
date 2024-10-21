from django.shortcuts import render, get_object_or_404
from .models import Product
import json


def product_detail(request, code):
    product = get_object_or_404(Product, code=code)
    images = product.images.all()
    images_list = [{"id": image.id, "image": image.image.url} for image in images]

    product_data = {
        "id": product.id,
        "name": product.name,
        "brand": product.brand,
        "code": product.code,
        "images": images_list,
    }

    product_json = json.dumps(product_data)

    return render(request, "product_detail.html", {"product_json": product_json, "product": product})


def products(request):
    all_products = Product.objects.all()

    product_data_list = []
    for product in all_products:
        images = product.images.all()
        images_list = [{"id": image.id, "image": image.image.url} for image in images]

        product_data_list.append(
            {
                "id": product.id,
                "name": product.name,
                "brand": product.brand,
                "code": product.code,
                "images": images_list,
            }
        )

    products_json = json.dumps(product_data_list)
    return render(
        request,
        "products.html",
        {"products_json": products_json},
    )
