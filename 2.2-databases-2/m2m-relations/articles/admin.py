from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tags, Tags_position


class Tags_positionInlineFormset(BaseInlineFormSet):
    def clean(self):
        forms_not_deleted = [f for f in self.forms if not f.cleaned_data['DELETE']]
        forms_main = [f for f in forms_not_deleted if f.cleaned_data['is_main'] ]
        if len(forms_main) > 1:
            raise ValidationError('Че то не так')
        return super().clean()


class Tags_positionInline(admin.TabularInline):
    model = Tags_position
    extra = 0
    formset = Tags_positionInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [Tags_positionInline]
    pass
