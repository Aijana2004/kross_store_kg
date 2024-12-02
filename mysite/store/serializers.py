from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class StoreSerializers(serializers.ModelSerializer):
    owner = UserProfileSimpleSerializers()

    class Meta:
        model = Store
        fields = ['store_name','store_description','store_image','address','owner']


class ContactInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ShoesPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShoesPhotos
        fields = ['image']


class ShoesSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    date = serializers.DateTimeField(format='%Y-%m-%d %H:%M')

    class Meta:
        model = Shoes
        fields = ['shoes_name','category','store_connect','price','description','active',
                  'date','shoes_video','size','quantities']


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CarItem
        fields = '__all__'


class StoreReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = '__all__'


class ShoesReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShoesReview
        fields = '__all__'


class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'