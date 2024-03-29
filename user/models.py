from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
import datetime
from utils.files import filename_generator

def avatar_filename_generator(x, y):
    return filename_generator(x, y, 'avatars')

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email,is_admin=None, user_type=None, password=None, user_id=None):
        """Creates User with first_name, last_name, email"""

        if not any([first_name, last_name, email,is_admin]):
            raise ValueError("First Name, Last Name, and Email are required fields!")

        args = {
            "first_name": first_name,
            "last_name":last_name,
            "email":self.normalize_email(email),
            "is_admin": is_admin,
            "user_type": user_type
        }
        args = {i:k for i,k in args.items() if k is not None}
        print("args:",args)
        user = self.model(**args)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        """Creates Superuser"""

        if kwargs.get('user_id'): del kwargs['user_id'] # remove id from kwargs as it is a required field because its username but its auto
        kwargs['is_admin'] = True
        user = self.create_user(*args, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """A custom user for authentication"""

    STUDENT = "S"
    TEACHER = "T"

    USER_TYPE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher')
    ]

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    avatar = models.ImageField(upload_to=avatar_filename_generator, default='default/images/default_avatar.png')
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10, unique=True, null=False, blank=False, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=2, choices=USER_TYPE_CHOICES, default=STUDENT, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return str(self.id)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def get_user_type(self):
        ut = self.user_type
        for k,val in self.USER_TYPE_CHOICES:
            if k == ut:
                return val
    @property
    def is_teacher(self):
        return self.user_type == self.TEACHER

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def save(self, *args, **kwargs):
        """Saves the user"""

        print("calledmodelsave")
        print("self.id:",self.id)
        super().save(*args, **kwargs)
        if self.user_id is None or self.user_id == "" or not self.user_id.startswith("BE"):
            user_id = 'BE/' + str(datetime.datetime.now().year)[-2:] + str(self.id).zfill(5)
            print("model save called: ", user_id)
            self.user_id = user_id
            self.save()
