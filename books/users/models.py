from django.contrib.auth.models import AbstractUser
from django.db import models

# New custom user model that extends abstract user (abstract base user is even more granular
# and flexible but requires more work, can be added later if needed)
class CustomUser(AbstractUser):
    pass