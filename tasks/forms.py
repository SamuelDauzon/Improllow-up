# coding:utf-8
from bootstrap3_datetime.widgets import DateTimePicker

from projects.forms import FormBase, ModelFormBase
from .models import Task

class TaskForm(ModelFormBase):
    """
    Mise à jour d'un compte
    """
    class Meta:
        model = Task
        widgets = {
            'execution_date': DateTimePicker(
                options = {
                    "format": "YYYY-MM-DD",
                    "pickTime": False
                }
            )
        }
        fields = {
            'name',
            'duration',
            'project',
            'userprofile',
            'execution_date',
            'details',
            'task_type',
        }

