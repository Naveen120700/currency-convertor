from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime
from .models import Currency
import datetime

class APITest(TestCase):
    # def setUp(self):
    #     # Create sample data for testing
    #     self.currency_usd = Currency.objects.create(code='USD', name='US Dollar', rate=1.0)
    #     self.currency_eur = Currency.objects.create(code='EUR', name='Euro', rate=0.85)

    def test_update_exchange_rates(self):
        url = reverse('update_exchange_rates')  # Update with your actual URL name
        response = self.client.get(url)
        # self.assertEqual(response.data,{})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['status'])
        self.assertEqual(response.data['msg'], 'Exchange rates updated successfully.')

    def test_last_updated_valid_code(self):
        url = reverse('last-updated', kwargs={'code': 'USD'})  # Update with your actual URL name and code
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['status'])
        self.assertEqual(response.data['msg'], 'OK')
        self.assertIsInstance(response.data['data'], str)  # Assuming your get_last_updated function returns a string

    def test_last_updated_invalid_code(self):
        url = reverse('last-updated', kwargs={'code': 'XYZ'})  # Update with your actual URL name and an invalid code
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['status'])
        self.assertEqual(response.data['msg'], 'Please provide valid code.')
        self.assertEqual(response.data['data'], [])

    def test_convert_currency(self):
        url = reverse('convert-currency')  # Update with your actual URL name
        params = {'source': 'USD', 'target': 'EUR', 'amount': 100}
        response = self.client.get(url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['status'])
        self.assertEqual(response.data['msg'], 'OK')
        self.assertIn('data', response.data)
        self.assertIsInstance(response.data['data'], int)  # Assuming your get_conversion function returns an integer

    def test_convert_currency_invalid_input(self):
        url = reverse('convert-currency')  # Update with your actual URL name
        params = {'source': 'USD', 'target': 'EUR'}  # Missing 'amount'
        response = self.client.get(url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['status'])
        self.assertEqual(response.data['msg'], 'Please provide valid input.')
        self.assertEqual(response.data['data'], [])

    def test_convert_currency_invalid_codes(self):
        url = reverse('convert-currency')  # Update with your actual URL name
        params = {'source': 'XYZ', 'target': 'ABC', 'amount': 100}
        response = self.client.get(url, params)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['status'])
        self.assertEqual(response.data['msg'], 'Please provide valid source, target code.')
        self.assertEqual(response.data['data'], [])