from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import *


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(SocialLink)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(Review)