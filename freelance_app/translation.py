from .models import Project
from modeltranslation.translator import TranslationOptions,register


@register(Project)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
