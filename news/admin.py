from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from news.models import CategoryModel, TagModel, AuthorModel, NewsModel, NewsCollectionModel, ContactModel


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ('id', 'name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(AuthorModel)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('first_name', 'last_name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('name', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author__first_name', 'created_at',)
    ordering = ('-created_at',)
    search_fields = ('title', 'id',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'subject')
    ordering = ('-created_at',)
    search_fields = ('full_name', 'message',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)


admin.site.register(NewsCollectionModel)
