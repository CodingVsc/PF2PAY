import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, AbstractUser
from django.db import models
from django.utils import timezone


def user_avatar_file(instance, filename):
    return '/'.join(['images', str(instance.name), filename])


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, blank=False, unique=True)
    avatar = models.ImageField(upload_to=user_avatar_file, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_seller = models.BooleanField(default=False)
    balance = models.FloatField(default=0)
    phone = models.CharField(max_length=30)

    product_count = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)


    def get_avatar(self):
        if self.avatar:
            return 'http://127.0.0.1:8000' + self.avatar.url
        else:
            return 'https://sun6-21.userapi.com/s/v1/if1/zJ1bldH0s_clKHi40' \
                   'sTI-LOoHeFzwmUyT3FBrzDLqTz4G68HAsuwJCL2yk8NkSEXcakoXW7D.jpg?si' \
                   'ze=200x200&quality=96&crop=36,0,215,215&ava=1'


class Content(models.Model):
    service_name = models.CharField(max_length=50)


class Permissions(models.Model):
    name = models.CharField(max_length=50)
    code_name = models.CharField(max_length=50)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='perms')


class UserPermission(models.Model):
    permission_id = models.ForeignKey(Permissions, on_delete=models.CASCADE, related_name='user_perms_id')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_perms_user_id')


class Reviews(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')




