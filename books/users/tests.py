from django.test import TestCase
from django.contrib.auth import get_user_model

# Two test cases for confirming that a new user and new superuser can be created
# To run, use 'python manage.py test' >> if in docker, prefix this command with 'docker-compose exec web'
class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='bob',
            email='bob@email.com',
            password='testpassword'
        )

        self.assertEqual(user.username, 'bob')
        self.assertEqual(user.email, 'bob@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        super_user = User.objects.create_superuser(
            username='super',
            email='super@email.com',
            password='sup13579'
        )

        self.assertEqual(super_user.username, 'super')
        self.assertEqual(super_user.email, 'super@email.com')
        self.assertTrue(super_user.is_active)
        self.assertTrue(super_user.is_staff)
        self.assertTrue(super_user.is_superuser)