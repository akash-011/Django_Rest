from django.test import TestCase
from .models import bucketlist


class ModelTestCase(TestCase):
    "Tests for Bucketlist Model"

    def setUp(self):
        self.bucketlist_name = "Go to Old Trafford"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_create_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.Bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)

    
