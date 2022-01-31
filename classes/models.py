from django.db import models
from django.conf import settings
from django.contrib.auth.models import Group
from datetime import datetime

# Create your models here.
class Class(models.Model):

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name='classes')
    starts_at = models.TimeField()
    days = models.CharField(max_length=13) # day number, seperated by comma. Sunday is 0
    meeting_id = models.CharField(max_length=42)
    groups = models.ManyToManyField(Group)
    subject = models.CharField(max_length=50)

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