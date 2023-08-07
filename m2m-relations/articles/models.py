from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField('Название тега', max_length=64)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return f'({self.id}) {self.name}'


class ScopeArticle(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='scopes',
                            verbose_name='Раздел',
                            null=True,
                            blank=True)
    is_main = models.BooleanField('Основной', default=False)

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статей'
        ordering = ['-is_main', 'tag']