from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from datetime import datetime

# Create your models here.

class Event(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='events')
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    groups = models.ManyToManyField(Group)
    allday = models.BooleanField(default=True)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=10000, null=True, blank=True)
    url = models.URLField(max_length=200, null=True, blank=True)
    background_color = models.CharField(max_length=7, default='#03a9f3')

class Class(models.Model):
    days = models.CharField(max_length=13) # day number, seperated by comma. Sunday is 0
    meeting_id = models.CharField(max_length=42)
    subject = models.CharField(max_length=50)
    event = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.subject + " " + self.created_by.get_full_name()

    def is_on_day(self, day): # Day is an int representing day of the week. SUnday is 0, Monday 1, etc.
        if day in self.on_days:
            return True

    @property
    def is_today(self):
        print("performing is_today")
        today = datetime.today().weekday()
        print("today is: " + str(today))
        print("days is: " + str(self.on_days))
        if today in self.on_days:
            print("is_today is true")
            return True
        print("is_today is false")

    @property
    def on_days(self):
        return [int(d) for d in self.days.split(",")]
