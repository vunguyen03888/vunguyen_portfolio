from django.contrib import admin
from home.models import SlideIcon, Blog, Setting, ContactMessage, CatalogProView, ProductView
# Register your models here.

class CatalogProViewAdmin(admin.ModelAdmin):
    list_display = ['title', 'update_at']
    list_filter = ['update_at']

class ProductViewAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'update_at']
    list_filter = ['title']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'sapo','status', 'update_at']
    list_filter = ['update_at']

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company', 'update_at','status']

class SlideIconAdmin(admin.ModelAdmin):
    list_display = ['title','sapo','icon']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject', 'note','status']
    readonly_fields =('name','subject','email','messages','ip')
    list_filter = ['status']

admin.site.register(CatalogProView,CatalogProViewAdmin)
admin.site.register(ProductView,ProductViewAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Setting,SettingAdmin)
admin.site.register(SlideIcon,SlideIconAdmin)
admin.site.register(ContactMessage,ContactMessageAdmin)
