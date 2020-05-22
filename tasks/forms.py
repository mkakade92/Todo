from django import forms
from django.forms import ModelForm
from .models import task

class TaskForm(ModelForm):

    class Meta:
        model =task
        fields = "__all__"


class UpdateTaskForm(ModelForm):
    class Meta:
        model = task
        fields =['title','description']