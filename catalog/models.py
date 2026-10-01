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
