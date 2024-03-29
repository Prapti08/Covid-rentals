from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your tests here.

class AuthTestCase(TestCase):
    def setUp(self):
        User=get_user_model()
        self.u = User.objects.create_user('test@dom.com', 'test@dom.com', 'pass','9898989898','2000-10-10')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='test@dom.com', password='pass')
