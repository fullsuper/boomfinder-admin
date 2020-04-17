from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
  """hello """
  def test_create_user_with_email_successful(self):
    email = 'dong@fullduper.com'
    password = 'dong123'
    user = get_user_model().objects.create_user(
      email = email,
      password = password
    )

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    """ Tesst"""
    email = "test@gmail.com"
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email(self):
    """abc"""
    with self.assertRaises(ValueError):
      get_user_model().objects.create_user(None, '123')

  def test_create_new_super_user(self):
    """xyz"""
    user = get_user_model().objects.create_superuser(
      'test@gmail.com',
      'test123'
    )

    self.assertTrue(user.is_superuser)
    self.assertTrue(user.is_staff)