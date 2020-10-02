from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phonenumber_field import modelfields


class Product(models.Model):
    name        = models.CharField(max_length=32)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10)
    qty         = models.PositiveSmallIntegerField()
    color       = models.CharField(max_length=20)
    size        = models.DecimalField(decimal_places=2, max_digits=5)


class MyAccountManager(BaseUserManager):
    def create_user(self, username, phone, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not phone:
            raise ValueError('Users must have a phone number')

        user = self.model(username=username, phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, phone, password):
        user = self.create_user( username=username, phone=phone, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username       = models.CharField(max_length=30, unique=True)
    phone          = modelfields.PhoneNumberField(null=False, blank=False, unique=True)
    date_joined    = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login     = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin       = models.BooleanField(default=False)
    is_active      = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY
    def has_module_perms(self, app_label):
        return True
