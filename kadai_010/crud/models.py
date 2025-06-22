from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    # �V�K�쐬�E�ҏW�������̃��_�C���N�g��
    def get_absolute_url(self):
        return reverse('list')
