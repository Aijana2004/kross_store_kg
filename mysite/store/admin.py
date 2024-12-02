from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ContactInfoInline(admin.TabularInline):
    model = ContactInfo
    extra = 1


class ShoesPhotosInline(admin.TabularInline):
    model = ShoesPhotos
    extra = 1


@admin.register(Store)
class StoreAdmin(TranslationAdmin):

    inlines = [ContactInfoInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Shoes)
class ShoesAdmin(TranslationAdmin):
    inlines = [ShoesPhotosInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


admin.site.register(UserProfile)
admin.site.register(ShoesReview)
admin.site.register(StoreReview)
admin.site.register(Cart)
admin.site.register(CarItem)
admin.site.register(Brand)
admin.site.register(Stock)
admin.site.register(Favorite)
# admin.site.register(ShoesPhotos)


