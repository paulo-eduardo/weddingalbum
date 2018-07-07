from rest_framework.test import APITestCase
from django.test import RequestFactory
from pictures.models import Pictures
from rest_framework import status
import json 

from rest_framework_jwt import utils, views
from rest_framework_jwt.compat import get_user_model
from rest_framework_jwt.settings import api_settings, DEFAULTS

User = get_user_model()

class PicturesTests(APITestCase):
    token = ''
    def setUp(self):
        self.email = 'teste@teste.com'
        self.username = 'noivo'
        self.password = 'senhaNoivo'
        self.user = User.objects.create_user(username=self.username,password=self.password)

        self.data = {
            'username': self.username,
            'password': self.password
        }

        self.factory = RequestFactory()
        self.user = Pictures.objects.create(name = 'teste1.jpg')
        self.user = Pictures.objects.create(name = 'teste2.jpg', status=True)


    def test_can_get_file_not_aproved(self):  
        # Arrange      
        resp = self.client.post('/api-token-auth/', self.data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT '+ resp.data['token'])

        # Act
        response = self.client.get('/pictures/toApprove/')
        

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNone(response.data[0]["status"])

    def test_can_get_file_aproved(self):
        # Act
        response = self.client.get('/pictures/approved/')
        
        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["status"], True)



    def test_can_get_aprove_picture(self):
        # Arrange
        resp = self.client.post('/api-token-auth/', self.data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='JWT '+ resp.data['token'])
        response = self.client.get('/pictures/toApprove/')
        picture = response.data[0]
        picture['status'] = True

        # Act
        response = self.client.put('/pictures/toApprove/', picture, format='json')

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        notAprovedPicture = Fotos.objects.filter(status=None).exists()
        self.assertFalse(notAprovedPicture)

    def test_can_give_like_to_picture(self):
        # Arrange
        responseAprovados = self.client.get('/pictures/approved/')
        picture = responseAprovados.data[0]
        picture['likes'] = 1
        
        # Act
        response = self.client.put('/pictures/approved/', picture, format='json')

        # Assert
        responseAprovados = self.client.get('/pictures/approved/')
        picture = responseAprovados.data[0]
        self.assertEqual(picture['likes'], 1)