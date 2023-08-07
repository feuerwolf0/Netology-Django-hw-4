from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ScopeArticle, Tag


class ScopeArticleInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_list = []
        for form in self.forms:
            if form.cleaned_data:
                main_list.append(form.cleaned_data['is_main'])

        # Получаю количество указанных основных разделов
        count_true = main_list.count(True)

        # Если выбрано несколько основных разделов
        if count_true > 1:
            raise ValidationError('Основным может быть только один раздел')
        # Если основной раздел не указан
        elif count_true < 1:
            raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeArticleInline(admin.TabularInline):
    model = ScopeArticle
    formset = ScopeArticleInlineFormset
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_display_links = ['id', 'title']
    inlines = [ScopeArticleInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']