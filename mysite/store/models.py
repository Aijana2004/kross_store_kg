from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
    )
    user_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')
    phone_number = PhoneNumberField(region='KG', null=True, blank=True)


class Category(models.Model):
    category_name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Brand(models.Model):
    brand_name = models.CharField(max_length=55,unique=True)


class Store(models.Model):
    store_name = models.CharField(max_length=25, unique=True)
    store_image = models.ImageField(upload_to= 'store_image/')
    store_description = models.TextField()
    address = models.TextField()
    owner = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='store_owner')

    def __str__(self):
        return f'{self.store_name}'


class ContactInfo(models.Model):
    store_connect = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='contact_store')
    info = models.CharField(max_length=55)


class Shoes(models.Model):
    shoes_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category,related_name='shoes',on_delete=models.CASCADE)
    store_connect = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='store')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    shoes_video = models.FileField(verbose_name='video',null=True,blank=True)
    size = MultiSelectField(max_length= 100,max_choices= 62,choices=zip(range(35, 62), range(35, 62)))
    quantities = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.shoes_name}'


class ShoesPhotos(models.Model):
    product = models.ForeignKey(Shoes,related_name='product',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    color = models.CharField(max_length=50)


class Stock(models.Model):
    store_stock = models.ForeignKey(Store,on_delete=models.CASCADE,related_name='stock')
    start_date = models.DateTimeField()
    finish_date = models.DateTimeField()


class Cart(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name='cart')

    def __str__(self):
        return f' {self.user}'

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

    # def get_total_price(self):
    #     total_price = sum(item.get_total_price() for item in self.items.all())
    #     discount = 0
    #
    #     if self.user.status == 'gold':
    #         discount = 0.75
    #     if self.user.status == 'silver':
    #         discount = 0.50
    #     if self.user.status == 'bronze':
    #         discount = 0.25
    #
    #     final_price = total_price*(1-discount)
    #     return final_price


class CarItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='items')
    shoes = models.ForeignKey(Shoes,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def get_total_price(self):
        return self.shoes.price * self.quantity


class StoreReview(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='client')
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name='store_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.store} - {self.rating}'


class ShoesReview(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE,related_name='client_review')
    shoes = models.ForeignKey(Shoes, on_delete=models.CASCADE,related_name='shoes_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.user_name} - {self.shoes} - {self.rating}'


class Favorite(models.Model):
    shoes = models.ManyToManyField(Shoes)
    created_date = models.DateTimeField(auto_now_add=True)

