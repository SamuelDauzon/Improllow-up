# coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

from projects.models import Project, BaseModel

class UserProfile(AbstractUser, BaseModel):
    boss = models.ForeignKey(
        "UserProfile",
        null = True, 
        blank = True,
        verbose_name = "Supérieur hiérarchique",
        related_name = "user_boss"
    )
    hiring_date = models.DateTimeField(
        verbose_name = "Date d'arrivée",
        null = True, 
        blank = True
    )

    def __str__(self):
        return self.first_name+" "+self.last_name+" ("+self.username+")"

        