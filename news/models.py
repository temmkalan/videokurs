from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Наименование')
    content = models.TextField(blank=True, verbose_name= 'Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name= 'Дата публикации')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name= 'Фото', blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


