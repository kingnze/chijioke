from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class worldnews(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(worldnews, self).save(*args, **kwargs)

    class Meta:
        db_table = 'worldnews'
        managed = True
        verbose_name = 'worldnews'
        verbose_name_plural = 'worldnews'



class worldnewsComment(models.Model):
    body = models.TextField()
    worldnewsusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(worldnews,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'worldnewsComments'
        managed = True
        verbose_name = 'worldnewsComment'
        verbose_name_plural = 'worldnewsComments'  
        
