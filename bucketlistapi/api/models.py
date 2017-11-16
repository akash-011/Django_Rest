from django.db import models

class Bucketlist(models.model):

    name = model.CharField(max_length='255', blank=False, unique=True)
    date_created = model.DateTimeField(auto_now_add=True)
    date_modified = model.DateTimeField(auto_now=True)

    def __str__(self):
        return"{}".format(self.name)
