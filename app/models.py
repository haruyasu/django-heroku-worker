from django.db import models


class WorkerResults(models.Model):
    result = models.CharField(max_length=255, default=None)
    url = models.CharField(max_length=255, default=None)
