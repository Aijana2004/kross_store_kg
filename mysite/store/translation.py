from .models import Store,Shoes,Category
from modeltranslation.translator import TranslationOptions,register


@register(Store)
class StoreTranslationOptions(TranslationOptions):
    fields = ('store_name', 'store_description')


@register(Shoes)
class ShoesTranslationOptions(TranslationOptions):
    fields = ('shoes_name', 'description')
