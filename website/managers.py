from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, name,phno,date_of_birth,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,
        name=name,phno=phno,date_of_birth=date_of_birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password,name,phno,date_of_birth):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            name=name,
            phno=phno,
            date_of_birth=date_of_birth,
            email=email,
            password=password
            )
        user.is_staff=True
        user.is_active=True
        user.is_superuser=True

        user.save(using= self._db)
        return user
