from datetime import datetime
from django.db import models
from django.utils.text import slugify
from pytils.translit import slugify as pytils_slugify

class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)

    def __str__(self):
        return self.name

class Board(models.Model):
    # title, category, description, image, author_name, author_phone, price, is_related_price
    title = models.CharField("Заголовок", max_length=200)
    category = models.CharField("Категория", max_length=255)
    description = models.TextField("Описание")
    image = models.CharField("URL изображения", max_length=500)
    # необязательное поле
    price = models.IntegerField("Цена", null=True, blank=True)
    is_related_price = models.BooleanField("Цена", default=False, null=True, blank=True)
    author_name = models.CharField("Автор", max_length=50)
    author_number = models.CharField("Номер телефона", max_length=20)
    posted_date = models.DateTimeField("Дата и время публикации", default=datetime.now)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерируем slug из заголовка
            self.slug = pytils_slugify(self.title)

            # Проверяем на уникальность и добавляем суффикс, если необходимо
            while Board.objects.filter(slug=self.slug).exists():
                self.slug += '-'

        super().save(*args, **kwargs)

    def str(self):
        return self.title

