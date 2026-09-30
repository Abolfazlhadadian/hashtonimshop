from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('شماره موبایل باید وارد شود')
        if email:
            email = self.normalize_email(email)

        user = self.model(
            phone_number=phone_number,
            email=email,
            **extra_fields
        )

        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError('شماره موبایل باید وارد شود')
        if not password:
            raise ValueError('پسورد باید وارد شود')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_active') is not True:
            raise ValueError('کاربر باید فعال باشد')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('یوزر ادمین باید حتما عضویت داشته باشد')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('یوزر ادمین باید حتما سوپر یوزر باشد')
        return self.create_user(
            phone_number=phone_number,
            password=password,
            **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        verbose_name='شماره موبایل',
        validators=[
            RegexValidator(
                regex=r'^09[0-9]{9}$',
                message='لطفا شماره موبایل 11 رقمی خود را با عدد 0 وارد کنید'
            )
        ]

    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        verbose_name='ایمیل'
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='نام'
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='نام خانوادگی'
    )
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    is_staff = models.BooleanField(default=False, verbose_name='کارمند')

    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ثبت نام'
    )

    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.phone_number


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    display_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='نام نمایشی'
    )
    biography = models.TextField(
        blank=True,
        verbose_name='درباره من'
    )
    avatar = models.ImageField(
        upload_to='profiles/avatars/',
        blank=True,
        verbose_name='تصویر پروفایل'
    )
    province = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='استان'
    )
    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='شهر'
    )
    address = models.TextField(
        blank=True,
        verbose_name='آدرس کامل'
    )
    postal_code = models.CharField(
        max_length=11,
        blank=True,
        verbose_name='کد پستی'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')

    def __str__(self):
        return f' پروفایل{self.user.phone_number}'
