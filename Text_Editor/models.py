from django.db import models

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    query = models.CharField(max_length=5000)

    def __str__(self):
        return self.name
