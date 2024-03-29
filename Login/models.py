# from django.db import models
# from django.contrib.auth.models import User, AbstractBaseUser,PermissionsMixin, BaseUserManager
#
# # Create your models here.
#
# class UserProfileManager(BaseUserManager):
#     def create_user(self, email, name, password=None):
#
#         if not email:
#             raise ValueError('user must have an email')
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name)
#
#
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#     def create_superuser(self, email, name, password):
#
#         user = self.cerate_user(email, name, password)
#
#         user.is_superuser = True
#         user.is_staff = True
#
#         user.save()
#         return user
#
#         pass
#
#
#
#
#
#
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#
#     email = models.EmailField(max_length=255, unique = True)
#     name = models.CharField(max_length = 255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#
#     objects = UserProfileManager()
#
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = ['name']
#
#     def get_full_name(self):
#         return self.name
#
#     def __str__(self):
#         return self.email
