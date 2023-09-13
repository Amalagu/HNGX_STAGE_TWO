from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Person


class PersonAPITest(TestCase):
    def setUp(self):
        # Create some test data
        self.client = APIClient()
        self.valid_person_data = {
            "fullname": "John Doe",
            "gender": "Male",
            "email": "john@example.com",
            "address": "123 Main St"
        }
        self.invalid_person_data = {
            "fullname": "1234",  # Invalid fullname
            "gender": "Invalid",  # Invalid gender
            "email": "invalid-email",  # Invalid email
            "address": "Address123"  # Invalid address
        }
        self.valid_person = Person.objects.create(**self.valid_person_data)
    # test to create valid person instance

    def test_create_valid_person(self):
        response = self.client.post(
            '/api/', self.valid_person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # test that attempts to create an instance using invalid user data
    def test_create_invalid_person(self):
        response = self.client.post(
            '/api/', self.invalid_person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_person_list(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_person_detail_with_id(self):
        response = self.client.get(f'/api/{self.valid_person.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["fullname"], "John Doe")

    def test_get_person_detail_with_fullname(self):
        response = self.client.get(
            f'/api/?fullname={self.valid_person.fullname}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        self.assertEqual(response.data[0]["fullname"], "John Doe")

    def test_update_person(self):
        updated_data = self.valid_person_data
        updated_data['fullname'] = "Updated Name"
        response = self.client.put(
            f'/api/{self.valid_person.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["fullname"], "Updated Name")

    def test_delete_person(self):
        response = self.client.delete(f'/api/{self.valid_person.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)

    def test_invalid_person_detail(self):
        response = self.client.get('/api/9999/')  # Invalid ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
