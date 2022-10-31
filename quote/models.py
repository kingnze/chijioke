from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class quote(models.Model):
    body = RichTextField()
    date_posted = models.DateTimeField(default=datetime.now())
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'quote'
        managed = True
        verbose_name = 'quotes'
        verbose_name_plural = 'quotes'


class Freequote(models.Model):
    body = models.TextField()
    date_posted = models.DateTimeField(default=datetime.now(),null=True,blank=True)
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'Freequote'
        managed = True
        verbose_name = 'Freequotes'
        verbose_name_plural = 'Freequotes'        