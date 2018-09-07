from django.test import TestCase
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from service_area.test_constants import *


class TestCaseWithFixtures(TestCase):
    """Intial fixtures loading"""
    fixtures = ['data']


class CreateCompany(TestCase):
    """This test is for create company API"""

    def test_success(self):
        """Test Success"""
        r = self.client.post('/api/company/', CREATE_COMPANY_OBJECT_SUCCESS)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

    def test_fail(self):
        """Test Failure"""
        r = self.client.post('/api/company/', CREATE_COMPANY_OBJECT_FAILURE)
        self.assertFalse(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)


class Login(TestCaseWithFixtures):
    """
    This test is for login API
    """

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS, content_type='application/json')
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_202_ACCEPTED)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_FAILURE, content_type='application/json')
        self.assertFalse(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_401_UNAUTHORIZED)


class GetCompany(TestCase):
    """
    This test is to get all companies
    """

    def test_success(self):
        """Test Success"""
        r = self.client.get('/api/company/')
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)


class GetCompany(TestCaseWithFixtures):
    """
    This test is to get a single company
    """

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS, content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.get('/api/my-company/', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS, content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}12'.format(token=token)}
        r = self.client.get('/api/my-company/', **header)
        self.assertIsInstance(r.data["detail"], ErrorDetail)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)


class UpdateCompany(TestCaseWithFixtures):
    """
    This test is to update company details
    """

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.put('/api/my-company/', UPDATE_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        r = self.client.get('/api/my-company/', **header)
        self.assertEqual('Lazy Panda 8013', r.data['data']['name'])

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.put('/api/my-company/', UPDATE_COMPANY_OBJECT_FAILURE,
                            content_type='application/json', **header)
        self.assertFalse(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(r.data['data']['language'][0], ErrorDetail)


class DeleteCompany(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.delete('/api/my-company/',
                               content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        r = self.client.get('/api/my-company/', **header)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)
        self.assertIsInstance(r.data["detail"], ErrorDetail)


class DeleteServiceArea(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.delete(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84dd4/',
            content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}12'.format(token=token)}
        r = self.client.delete(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84d32/',
            content_type='application/json', **header)
        self.assertIsInstance(r.data["detail"], ErrorDetail)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)


class CreateServiceArea(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.post('/api/service-area/', CREATE_SERVICE_AREA_OBJECT_SUCCESS,
                             content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.post('/api/service-area/', CREATE_SERVICE_AREA_OBJECT_FAILURE,
                             content_type='application/json', **header)
        self.assertFalse(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(r.data['data']['price'][0], ErrorDetail)


class GetServiceArea(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.get(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84dd4/',
            content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.get(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84d32/',
            content_type='application/json', **header)
        self.assertFalse(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_204_NO_CONTENT)


class UpdateServiceArea(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.put(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84dd4/',
            UPDATE_SERVICE_AREA_OBJECT_SUCCESS,
            content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}12'.format(token=token)}
        r = self.client.put(
            '/api/my-service-area/efcb0080-1ce9-47a0-8299-15c126b84dd4/',
            UPDATE_COMPANY_OBJECT_FAILURE, content_type='application/json', **header)
        self.assertIsInstance(r.data["detail"], ErrorDetail)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)


class GetAllServiceArea(TestCaseWithFixtures):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}'.format(token=token)}
        r = self.client.get('/api/service-area/', content_type='application/json', **header)
        self.assertTrue(r.data["success"])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/company/', LOGIN_COMPANY_OBJECT_SUCCESS,
                            content_type='application/json')
        token = r.data['data']['access_token']
        header = {'HTTP_AUTHORIZATION': 'Bearer {token}12'.format(token=token)}
        r = self.client.get('/api/service-area/',
                            content_type='application/json', **header)
        self.assertIsInstance(r.data["detail"], ErrorDetail)
        self.assertEqual(r.status_code, status.HTTP_403_FORBIDDEN)


class SearchServiceArea(TestCase):

    def test_success(self):
        """Test Success"""
        r = self.client.put('/api/search/', SEARCH_SEARVICE_AREA_OBJECT_SUCCESS,
                            content_type='application/json')
        self.assertTrue(r.data['success'])
        self.assertEqual(r.status_code, status.HTTP_200_OK)

    def test_failure(self):
        """Test Failure"""
        r = self.client.put('/api/search/', SEARCH_SEARVICE_AREA_OBJECT_FAILURE,
                            content_type='application/json')
        self.assertFalse(r.data['success'])
        self.assertEqual(r.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(r.data['data']['latitude'][0], ErrorDetail)
