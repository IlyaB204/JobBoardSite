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
