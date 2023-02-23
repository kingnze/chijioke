from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import datetime
from django.contrib.auth.models import User

class Headline(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Headline, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Headline'
        managed = True
        verbose_name = 'Headline'
        verbose_name_plural = 'Headline'

class Comment(models.Model):
    body = models.TextField()
    usercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Headline,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'comments'
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Business(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Business, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Business'
        managed = True
        verbose_name = 'Business'
        verbose_name_plural = 'Business'

class BusinessComment(models.Model):
    body = models.TextField()
    Businessusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Business,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'BusinessComments'
        managed = True
        verbose_name = 'BusinessComment'
        verbose_name_plural = 'BusinessComments'

class Politics(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Politics, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Politics'
        managed = True
        verbose_name = 'Politics'
        verbose_name_plural = 'Politics'

class PoliticsComment(models.Model):
    body = models.TextField()
    Politicsusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Politics,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'PoliticsComments'
        managed = True
        verbose_name = 'PoliticsComment'
        verbose_name_plural = 'PoliticsComments'

class Bigstory(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Bigstory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Bigstory'
        managed = True
        verbose_name = 'Bigstory'
        verbose_name_plural = 'Bigstory'

class Commet(models.Model):
    body = models.TextField()
    usercommet = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Bigstory,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'commets'
        managed = True
        verbose_name = 'Commet'
        verbose_name_plural = 'Commets'

class Crime(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Crime, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Crime'
        managed = True
        verbose_name = 'Crime'
        verbose_name_plural = 'Crime'

class CrimeCommemt(models.Model):
    body = models.TextField()
    Crimeusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Crime,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'CrimeComments'
        managed = True
        verbose_name = 'CrimeComment'
        verbose_name_plural = 'CrimeComments'

class Environment(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Environment, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Environment'
        managed = True
        verbose_name = 'Environment'
        verbose_name_plural = 'Environment'

class EnvironmentComment(models.Model):
    body = models.TextField()
    Environmentusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Environment,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'EnvironmentComments'
        managed = True
        verbose_name = 'EnvironmentComment'
        verbose_name_plural = 'EnvironmentComments'

class Health(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Health, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Health'
        managed = True
        verbose_name = 'Health'
        verbose_name_plural = 'Health'

class HealthComment(models.Model):
    body = models.TextField()
    Healthusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Health,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'HealthComments'
        managed = True
        verbose_name = 'HealthComment'
        verbose_name_plural = 'HealthComments'

class Trending(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Trending, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Trending'
        managed = True
        verbose_name = 'Trending'
        verbose_name_plural = 'Trending'

class TrendingComment(models.Model):
    body = models.TextField()
    Trendingusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Trending,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'TrendingComments'
        managed = True
        verbose_name = 'TrendingComment'
        verbose_name_plural = 'TrendingComments'

class Tech(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    leadimg = models.ImageField()
    body = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Tech, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Tech'
        managed = True
        verbose_name = 'Tech'
        verbose_name_plural = 'Tech'

class TechComment(models.Model):
    body = models.TextField()
    Techusercomment = models.ForeignKey(User,on_delete=models.DO_NOTHING)  
    post = models.ForeignKey(Tech,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = 'TechComments'
        managed = True
        verbose_name = 'TechComment'
        verbose_name_plural = 'TechComments'
     
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

class Reply(models.Model):

    body = models.TextField()
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    replier = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'replies'
        managed = True
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'



