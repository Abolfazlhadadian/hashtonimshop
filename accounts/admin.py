from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import Profile, User


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 0
    max_num = 1
    can_delete = False
    readonly_fields = [
        'created_at',
        'updated_at'
    ]


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    fieldsets = (
        ('اطلاعات حساب', {
            'fields': ('phone_number', 'email', 'password'),
            'description': 'اطلاعات اصلی ورود و حساب کاربر'
        }),
        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name'),
            'description': 'اطلاعات شخصی کاربر'
        }),
        ('دسترسی ها', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'description': 'سطح دسترسی و مجوزهای کاربر',
            'classes': ('collapse',)
        }),
        ('اطلاعات سیستم', {
            'fields': (
                'date_joined',
                'last_login'
            ),
            'classes': ('collapse',),
            'description': ('اطلاعات تاریخ و زمان')
        })
    )

    add_fieldsets = (
        (
            'اطلاعات حساب', {
            'fields': (
                'phone_number',
                'email',
                'password1',
                'password2'
            ),
        }
        ),
        (
            'دسترسی ها', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        }
        )
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = (
        'id',
        'phone_number',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        'is_superuser',
    )

    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )

    search_fields = (
        '=id',
        'phone_number',
        'email',
        'first_name',
        'last_name',
    )
    ordering = (
        'id',
        'first_name',
        'last_name'
    )
    list_editable = (
        'is_active',
    )
    readonly_fields = (
        'date_joined',
        'last_login',
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('اطلاعات پروفایل', {
            'fields': ('user',),
            'classes': ('collapse',)
        }),
        ('اطلاعات سیستم', {
            'fields': (
                'created_at',
                'updated_at'
            ),
            'classes': ('collapse',)
        })
    )

    list_display = ['id', 'user', 'created_at', 'updated_at']
    search_fields = [
        'user__id',
        'user__phone_number',
        'user__email',
        'user__last_name'
    ]

    ordering = [
        '-created_at',
        'updated_at'
    ]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, CustomUserAdmin)
