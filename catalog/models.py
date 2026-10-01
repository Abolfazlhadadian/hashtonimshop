from django.core.validators import MinValueValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='نام دسته'
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='اسلاگ فیلد'
    )
    description = models.TextField(
        blank=True,
        verbose_name='توضیحات'
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ بروز رسانی'
    )

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    categories = models.ManyToManyField(
        to='Category',
        related_name='products',
        verbose_name='دسته بندی ها'
    )

    name = models.CharField(
        max_length=255,
        verbose_name='نام محصول'
    )

    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='اسلاگ'
    )

    description = models.TextField(
        blank=True,
        verbose_name='توضیحات'
    )

    retail_price = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[MinValueValidator(0)],
        verbose_name='قیمت خرده فروشی'
    )

    wholesale_price = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[MinValueValidator(0)],
        verbose_name='قیمت عمده فروشی'
    )

    wholesale_min_quantity = models.PositiveIntegerField(
        default=7,
        verbose_name='حداقل تعداد خرید عمده'
    )

    wholesale_package_size = models.PositiveIntegerField(
        default=10,
        verbose_name='تعداد در بسته عمده'
    )

    retail_available = models.BooleanField(
        default=True,
        verbose_name='فروش خرده مجاز'
    )

    stock_quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='موجودی'
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name='فعال'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ بروزرسانی'
    )

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['name']

    def __str__(self):
        return self.name