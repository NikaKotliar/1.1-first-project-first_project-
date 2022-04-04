from django.contrib import admin

from .models import Article, Tags


#
# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             form.cleaned_data
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()  # вызываем базовый код переопределяемого метода
#
#
# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#     formset = RelationshipInlineFormset
# @admin.register(Tags)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
