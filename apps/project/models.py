from __future__ import unicode_literals
from ..login.models import User
from django.db import models
import datetime
from datetime import datetime, date


class AppointManager(models.Manager):
    def addAppoint(self, postData):
        data = {
            'valid':False,
            'errors': [],
        }
        if not postData:
            data['errors'].append('post data only')
            return data

        if len(postData['tasks']) < 1:
            data['errors'].append('tasks cannot be empty')

        if postData['date'] == "":
            data['errors'].append('dates cannot be empty')


        if postData['time'] == "":
            data['errors'].append('time cannot be empty')


        if postData['date'] < {date}:
            data['errors'].append('dates cannot be empty')





        if data['errors']:
            return data

        else:
            data['valid'] = True
            user = User.objects.get(id = postData['user_id'])
            newTask = Appoint.objects.create(tasks = postData['tasks'], time = postData['time'], status = postData['status'], date = postData['date'], planned_by = user)

            return data




class Appoint(models.Model):
    tasks = models.CharField(max_length=100)
    status = models.TextField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    planned_by = models.ForeignKey(User, related_name='AP_made')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = AppointManager()
