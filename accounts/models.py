# from multiselectfield import MultiSelectField

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import transaction


class CustomAccountManager(BaseUserManager):

    def _create_user(self, phone, password, **extra_fields):
            """
            Creates and saves a User with the given email,and password.
            """
            if not phone:
                raise ValueError('The given email must be set')
            try:
                # email = self.normalize_email(email)
                with transaction.atomic():
                    user = self.model(phone=phone, **extra_fields)
                    user.set_password(password)
                    user.save(using=self._db)
                    return user
            except:
                raise

    def create_superuser(self, phone, password, **extra_fields):

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)

        # extra_fields.setdefault('roles', [0])

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self._create_user(phone, password=password, **extra_fields)
    
    def create_user(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(phone, password, **extra_fields)
        


class UserBase(AbstractBaseUser, PermissionsMixin):
    # platform_type = MultiSelectField(choices=platform_types, null = True, blank = True)

    is_active = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    email = models.EmailField(_('email address'))
    first_name = models.CharField(max_length=150, blank=True)
    last_name =  models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=150)
    payoutaddress = models.CharField(max_length=150, blank=True)
    amountmined =  models.CharField(max_length=150, blank=True)
    amountachievedafterded =  models.CharField(max_length=150, blank=True)
    currentcoin = models.CharField(max_length=150, blank=True)
    minespeed = models.CharField(max_length=150, blank=True)
    minerconnected = models.BooleanField(default=False)
    nextpayout =  models.CharField(max_length=150, blank=True)
    profit_today = models.CharField(max_length=150, blank=True)
    profit_yesterday = models.CharField(max_length=150, blank=True)

    watcherlink = models.CharField(max_length=250, blank=True)
    binance_profile_token = models.CharField(max_length=250, blank=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone'
    # REQUIRED_FIELDS = ['email']
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"
        db_table = 'auth_user'
        indexes = [
            models.Index(fields=['id', 'phone', 'first_name', 'last_name', 'email', 'is_active'])
        ]

    def __str__(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super(UserBase, self).save(*args, **kwargs)