from django.db import models


class FormTemplate(models.Model):
    name = models.CharField(max_length=255)
    fields = models.JSONField()
