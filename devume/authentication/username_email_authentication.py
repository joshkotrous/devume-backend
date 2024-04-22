from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if username is provided
        if username is not None:
            # Attempt to authenticate using username
            user = UserModel.objects.filter(username=username).first()
            if user and user.check_password(password):
                return user

        # Check if email is provided
        if "@" in username:
            # Attempt to authenticate using email
            user = UserModel.objects.filter(email=username).first()
            if user and user.check_password(password):
                return user

        # Neither username nor email matched, return None
        return None
