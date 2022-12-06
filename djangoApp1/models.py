from django.db import models

# Create your models here.
class usersN(models.Model):
    name=models.TextField(name='name',max_length=300)

    def __str__(self):
        return self.name
