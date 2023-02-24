from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class Hiro (models.Model):
    """Класс сохранения данных о Геороях."""
    cd_hero = models.UUIDField(primary_key=True, default=uuid.uuid4())
    nm_hero = models.CharField(max_length=255)
    age = models.IntegerField()


# class Slrace (models.Model):
#     """Справочник рассы."""

