from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model where the email address is the unique identifier
    and has an is_admin field to allow access to the admin app
    """
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be set")
        if not password:
            raise ValueError("The password must be set")
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # def create_company(self, email, password, **extra_fields):
    #
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_active', True)
    #
    #     return self._create_user(email, password, **extra_fields)

    def create_users(self, email, password, **extra_fields):

        extra_fields.setdefault('is_active', True)

        return self._create_user(email, password, **extra_fields)
