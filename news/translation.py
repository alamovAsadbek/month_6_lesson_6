from modeltranslation.translator import TranslationOptions, register

from news.models import CategoryModel


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ('name',)
