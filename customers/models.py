# coding:utf-8
from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="Date de création"
    )
    modified = models.DateTimeField(
        auto_now = True, 
        verbose_name="Date de modification"
    )

    class Meta:
        abstract = True
        ordering = ("-created", )

class Customer(BaseModel):
    corporate_name = models.CharField(
        max_length = 255,
        verbose_name = "Nom"
    )
    def __str__(self):
        return self.corporate_name