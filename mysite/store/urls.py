from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'brand', BrandViewSet, basename='brand')
router.register(r'store', StoreViewSet, basename='store')
router.register(r'shoes', ShoesViewSet, basename='shoes')
router.register(r'favorite', FavoriteViewSet, basename='favorite')
router.register(r'shoes_review', CategoryViewSet, basename='shoes_review')
router.register(r'store_review', StoreReviewViewSet, basename='store_review')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')

urlpatterns = [
    path('', include(router.urls)),

]