from django.test import TestCase

import json

from rest_framework.test import APIClient
from rest_framework import status

from cardverifier.constants import API_SERVICE
from decouple import config

class JBCTestCase(TestCase):

    #Consult a valid card number
    def test_control(self):
        client = APIClient()

        test_consult_data = {
            "card_number": "3109668855491963"
        }

        service = config('HOSTING') + API_SERVICE
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['emisor'], 'JCB')


    #Consult a valid spaced card number
    def test_spaced(self):
        client = APIClient()

        test_consult_data = {
            "card_number": "3109 6688 5549 1963"
        }

        service = config('HOSTING') + API_SERVICE
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['emisor'], 'JCB')


    #Consult a not valid card number
    def test_wrong_number(self):
        client = APIClient()

        test_consult_data = {
            "card_number": "3109668855491960"
        }

        service = config('HOSTING') + API_SERVICE
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['valid'], False)


    #Wrong consult
    def test_alpha_numercial_number(self):
        client = APIClient()

        test_consult_data = {
            "card_number": "3109668855491963ww"
        }

        service = config('HOSTING') + API_SERVICE
        response = client.post(
            service, 
            test_consult_data,
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
