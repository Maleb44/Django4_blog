# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

class Message(models.Model):
    order = models.IntegerField( default=0)
    text = models.CharField(max_length=200,null=True)

    def __unicode__(self):
        return self.text

    class Meta:
        ordering = ['order']

class Post(models.Model):
    
    title   = models.CharField(max_length=100, unique=True)
    slug    = models.SlugField(max_length=100, unique=True,editable=False)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return '%s' % self.title
       
    class Meta:
        ordering = ['date']    



@receiver(pre_save,sender=Post)
def my_callback(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)