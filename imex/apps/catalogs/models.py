from django.db import models
from django.urls import reverse


class ProductsModel(models.Model):
    photo = models.ImageField(verbose_name='Фото', upload_to='resource/product/', default='None')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.description}"

    def get_absolute_url(self):
        return reverse('products', kwargs={"product_id": self.pk})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"