from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from .forms import CustomUserCreationForm
from .views import SignupPageView

# Note that the previous version of Django used in this textbook uses setUp(), but TestCase has been
# updated and setUpTestData() can be used to allow initial data creation and greatly increase speeds of
# test suites - look into for potential optimization

# Test cases for confirming that a new user and new superuser can be created
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


# Test cases for user signup (login and logout are implemented through Django's built-in
# auth functionality)
class SignupPageTests(TestCase):
    
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)
    
    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)