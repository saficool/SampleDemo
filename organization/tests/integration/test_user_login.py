from http import client
from unittest import result
from rest_framework.test import APIClient
from organization.tests import base_test


class UserLoginTestCase(base_test.NewUserTestCase):
    """
    This si class is used to test the login functionality and
    chaeck whether a user is successfulyy  getting logged in to the system
    """

    def setUp(self) -> None:
        super().setUp()

    def test_user_login(self):
        client = APIClient()
        user_credential = {
            'username': self.username,
            'password': self.password
        }
        result = client.post('/api/v1/user/login/',
                             user_credential, format='json')
        self.assertEquals(result.status_code, 200)
        self.assertTrue('access' in result.json())
        self.assertTrue('refresh' in result.json())

    def tearDown(self) -> None:
        self.client.logout()
        super().tearDown()
