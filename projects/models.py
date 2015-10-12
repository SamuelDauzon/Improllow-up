# coding:utf-8
from django.db import models

from customers.models import Customer, BaseModel

class Project(BaseModel):
    name = models.CharField(
        max_length = 127,
        verbose_name = "Nom"
    )
    customer = models.ForeignKey(Customer, verbose_name="Client")

    def __str__(self):
        return self.name
