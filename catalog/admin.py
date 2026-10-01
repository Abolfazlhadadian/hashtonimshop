from django.contrib import admin

from .models import Category, Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

    list_display = (
        'id',
        'name',
        'retail_price',
        'wholesale_price',
        'stock_quantity',
        'retail_available',
        'is_active',
    )

    list_filter = (
        'is_active',
        'retail_available',
        'categories',
    )

    search_fields = (
        'name',
        'slug',
        'categories__name',
    )

    filter_horizontal = (
        'categories',
    )

    ordering = (
        'name',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
        'slug',
    )

    ordering = (
        'name',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'image',
        'is_primary',
        'created_at',
    )

    list_filter = (
        'is_primary',
    )

    search_fields = (
        'product__name',
    )

    readonly_fields = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )
