from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# get_user_model looks to the AUTH_USER_MODEL config in settings.py


# Extend the user creation form; note that password field is implicitly included by default
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


# Extend the user change form; note that password field is implicitly included by default
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)