from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from apps.home.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField

class Role(BaseModel):
    name = models.CharField(max_length=10, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class CustomUserManager(BaseUserManager):

    def create_user(self, email, name,  password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password, **extra_fields):
      
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField(verbose_name='Email Address', unique=True, null=False, blank=False)
    name = models.CharField(verbose_name='Full Name', max_length = 255, null=False, blank=False)
    mobile_number = PhoneNumberField(verbose_name="Contact Number", unique=True, blank=True, null=True, region="IN")
    profile_image = models.ImageField(default='default_profile.jpg', upload_to="user_profile")
    role_assigned = models.ForeignKey(Role, null = True, blank=True, on_delete = models.CASCADE)
    
    is_verified = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    verbose_name_plural = "Users"

    objects = CustomUserManager()

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return self.profile_image.url

