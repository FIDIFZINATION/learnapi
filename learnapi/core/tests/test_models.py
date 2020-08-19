from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_authentication(self):
        """ Testing Authentication """
        email = "kaif@mail.com"
        password = "kaifkazi"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize(self):
        """Normalizing New User EmailField"""
        email = 'kaifka@s.com'
        user = get_user_model().objects.create_user(email, 'kaif123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Raises error if no email """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'kaif123')

    def test_create_superuser(self):
        """Creating new superusers"""
        user = get_user_model().objects.create_superuser(
            'kaazi@ma.com',
            'test1'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
