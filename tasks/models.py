# coding:utf-8
from django.db import models

from users.models import UserProfile
from projects.models import Project, BaseModel

class Task(BaseModel):
    name = models.CharField(
        max_length = 128,
        verbose_name = "Nom de la tâche"
    )
    duration = models.PositiveIntegerField(
        verbose_name = "Durée",
        null = True,
        blank = True
    )
    project = models.ForeignKey(
        Project,
        verbose_name="Projet",
        null = True,
        blank = True
    )
    task_type = models.ForeignKey(
        "TaskType",
        verbose_name="Type de tâche",
        null = True,
        blank = True
    )
    user_add = models.ForeignKey(
        UserProfile,
        verbose_name="Ajoutée par",
        related_name="user_add",
        null = True
    )
    userprofile = models.ForeignKey(
        UserProfile,
        verbose_name="Effectuée par",
        related_name="userprofile",
        null = True,
        blank = True
    )
    execution_date = models.DateField(
        verbose_name="Date d'éxecution",
        null = True,
        blank = True
    )
    details = models.TextField(
        verbose_name="Détails",
        null = True
    )

    def __str__(self):
        return self.name

class TaskType(BaseModel):
    name = models.CharField(
        max_length = 128,
        verbose_name = "Nom du type de tâche"
    )
    def __str__(self):
        return self.name
