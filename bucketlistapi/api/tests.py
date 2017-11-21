from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    "Tests for Bucketlist Model"

    def setUp(self):
        self.bucketlist_name = "Go to Old Trafford"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_create_bucketlist_model(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)

class ViewTestCase(TestCase):


    def setUp(self):
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Score a goal'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_api_create_bucketlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
