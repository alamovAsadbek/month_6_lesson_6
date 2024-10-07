from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from news.models import CategoryModel


@register(CategoryModel)
class CategoryModelTranslationOptions(TranslationOptions):
    fields = ('name',)
