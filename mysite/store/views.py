from rest_framework import viewsets
from .serializers import *


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializers


class ContactInfoViewSet(viewsets.ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializers


class ShoesViewSet(viewsets.ModelViewSet):
    queryset = Shoes.objects.all()
    serializer_class = ShoesSerializers


class ShoesPhotosViewSet(viewsets.ModelViewSet):
    queryset = ShoesPhotos.objects.all()
    serializer_class = ShoesPhotosSerializers


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CarItem.objects.all()
    serializer_class = CartItemSerializers


class StoreReviewViewSet(viewsets.ModelViewSet):
    queryset = StoreReview.objects.all()
    serializer_class = StoreReviewSerializers


class ShoesReviewViewSet(viewsets.ModelViewSet):
    queryset = ShoesReview.objects.all()
    serializer_class = ShoesReviewSerializers


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers

