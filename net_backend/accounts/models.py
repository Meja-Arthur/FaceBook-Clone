from typing import Any, Optional
from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone
# Create your models here.


class CustomUserManager(UserManager):
    
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
    def create_user(self, email=None, password=None, **extra_fields):
        # this handles the normal user 
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        # so this helps in creation of the superuser in the admin section 
        # Inshort we are overiding the create superuser function here
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if not email:
            raise ValueError("You must provide an email for the superuser.")
        
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True, default='', null=True)
    avator = models.ImageField(upload_to="avators", blank=True, null=True)
    friends = models.ManyToManyField('self')
    friends_count = models.IntegerField(default=0)
    
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)  
    last_login = models.DateTimeField(blank=True, null=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class FriendlyRequest(models.Model):
    SENT = 'sent'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    
    STATUS_CHOICES = {
        (SENT, 'sent'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected')
    }
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_for = models.ForeignKey(User, related_name='recieved_friendlyrequests', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add= True)
    created_by = models.ForeignKey(User, related_name='created_friendlyrequests', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=SENT)