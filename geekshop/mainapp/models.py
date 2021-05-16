from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='имя',
        max_length=64,
        unique=True,
    )

    description = models.TextField(
        verbose_name='описание товара',
        blank=True,
    )

    def __str__(self):
        return f"{self.name} {self.id} {self.created.date()}"

    created = models.DateTimeField(
        auto_now_add=True
    )

    updated = models.DateTimeField(
        auto_now=True
    )


class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория'
    )
    name = models.CharField (
        verbose_name='название товара',
        max_length=256,
    )
    image = models.ImageField(
        upload_to='products_img',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='краткое описание продукта',
        max_length=128,
        blank=True
    )
    description = models.TextField(
        verbose_name='описание продукта',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='цена товара',
        max_digits=8,
        decimal_places=2,
        null=True,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество на складе',
        default=0
    )

    def __str__(self):
        return f"{self.name} ({self.category.name})"
