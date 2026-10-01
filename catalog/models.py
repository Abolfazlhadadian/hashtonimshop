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

    retail_available = models.BooleanField(
        default=True,
        verbose_name='فروش خرده مجاز'
    )

    retail_min_quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='حداقل تعداد خرید خرده'
    )

    retail_max_quantity = models.PositiveIntegerField(
        default=6,
        verbose_name='حداکثر تعداد خرید خرده'
    )

    wholesale_min_quantity = models.PositiveIntegerField(
        default=7,
        verbose_name='حداقل تعداد خرید عمده'
    )

    wholesale_max_quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name='حداکثر تعداد خرید عمده'
    )

    wholesale_package_size = models.PositiveIntegerField(
        default=10,
        verbose_name='اندازه بسته عمده'
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


class ProductImage(models.Model):
    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='محصول'
    )

    image = models.ImageField(
        upload_to='products/images/',
        verbose_name='تصویر'
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='متن جایگزین'
    )

    is_primary = models.BooleanField(
        default=False,
        verbose_name='تصویر اصلی'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ایجاد'
    )

    class Meta:
        verbose_name = 'تصویر محصول'
        verbose_name_plural = 'تصاویر محصولات'
        ordering = ['-is_primary', 'created_at']

    def __str__(self):
        return f'{self.product.name} - {self.pk}'
