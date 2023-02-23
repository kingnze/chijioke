from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User



class localnews(models.Model):
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
        super(localnews, self).save(*args, **kwargs)

    class Meta:
        db_table = 'localnews'
        managed = True
        verbose_name = 'localnews'
        verbose_name_plural = 'localnews'


class localnewsComment(models.Model):
    body = models.TextField()
    localnewsusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(localnews,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'localnewsComments'
        managed = True
        verbose_name = 'localnewsComment'
        verbose_name_plural = 'localnewsComments'        