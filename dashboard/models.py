# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class todotask(models.Model):

    todo_status = (
        ('pending','Pending'),
        ('done','Done')
    )
    hidestatus = (
        ('1','Show'),
        ('0','Hide'),
    )

    taskname        = models.CharField(max_length=500)
    taskDescription = models.TextField()
    addedDate       = models.DateTimeField(auto_now_add=True,null=True)
    taskStatus      = models.CharField(max_length=20,choices=todo_status,default='pending')
    hidestatus      = models.CharField(max_length=20,choices=hidestatus,default='1')
    addedBy         = models.ForeignKey(User,null=True)

    def __str__(self):
        return self.taskname



