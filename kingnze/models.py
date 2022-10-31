from django.db import models

# Create your models here.


class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fullname} {self.phone}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts' 
