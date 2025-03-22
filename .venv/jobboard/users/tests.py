from http.client import responses

from django.test import TestCase
from django.urls import reverse

class TestLoginAndRegister(TestCase):

    def test_register_status_code(self):
        response = self.client.post(reverse('register'), {
            'username': 'Ilua',
            'password1':'secret',
            'password2':'secret',
            'name': 'name2',
            'email': 'email@gmail.com',
            'first_name': 'Konst',
            'last_name': 'Kent',
        })

        self.assertEqual(response.status_code, 302)

    def test_register_view_status_code(self):
        response = self.client.get(reverse('register'))
        no_response = self.client.get('jobboard/users/registers.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)

    def test_login_view_status_code(self):
        response = self.client.get(reverse('login'))
        no_response = self.client.get('users/logins.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_status_code(self):
        response = self.client.post(reverse('login'),{
            'username': 'asus',
            'password': 'secret',
        })
        self.assertEqual(response.status_code, 302)

    def  test_logout_view_status_code(self):
        response = self.client.get(reverse('logout'))
        no_response = self.client.get('users/logouts.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, 'users/logout.html')


    def test_edit_view_status_code(self):
        response =self.client.get(reverse('edit'))
        no_response = self.client.get('users/edits.html')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response,'users/edit.html')

