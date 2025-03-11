from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet, product_list_view, product_detail_view

router = DefaultRouter()
router.register(r'categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('product/', include(router.urls)),  # API Endpoints
    path('productslist/', product_list_view, name='product-list-html'),  # HTML Page
    path('products/<uuid:pk>/', product_detail_view, name='product-detail-html'),
]

