from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
# MVC MODEL VIEW CONTROLLER

# -*- coding: utf-8 -*-
#####################################
class Keywords(models.Model):
    keyword = models.CharField(max_length=120)
    키워드검색 = models.CharField(max_length=120, null=True)
    유사어검색 = models.CharField(max_length=120, null=True)

    def __str__(self):
        return self.keyword
#####################################

#####################################
class Sentence(models.Model):
    s_id = models.CharField(max_length=120, null=True)
    s_fileid = models.CharField(max_length=120, null=True)
    s_content = models.TextField(null=True)

    def __str__(self):
        return self.s_fileid
#####################################


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):
    fileid = models.CharField(max_length=120, null=True)
    title = models.TextField(null=True)
    subtitle = models.TextField(null=True)

    # image = models.ImageField(upload_to=upload_location,
    #         null=True, blank=True,
    #         width_field='width_field',
    #         height_field='height_field',
    #         )
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)

    content = models.TextField()
    # content2 = models.TextField(null=True)
    # content3 = models.TextField(null=True)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    class Meta:
        ordering = ["-timestamp", "-updated"]