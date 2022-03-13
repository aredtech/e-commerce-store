from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list, name="prouct-list"),
    path("collections/", views.collection_list, name="collection-list"),
    path("products/<int:pk>/", views.product_details, name="product-detail"),
    path("collections/<int:pk>/", views.collection_details, name="collection-detail")
]
