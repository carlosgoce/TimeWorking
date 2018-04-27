from django.test import TestCase
from rest_framework.test import APITestCase, 


from django.urls import include, path, reverse
# Create your tests here.


class RequestTests(APITestCase):
    
    def test_request(self)
        response=self.client.get(reverse('api:project-list'))
        assert response.status_code==403