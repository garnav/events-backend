from django.db import models
from django.utils import timezone
import datetime
from simple_history.models import HistoricalRecords

MAX_NAME_LENGTH = 100
MAX_DESC_LENGTH = 500
MAX_TAG_LENGTH = 50
MAX_CONTACT_LENGTH = 100
UPLOAD_USER_IMAGE = None

class Event(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    num_attendees = models.IntegerField()
    is_public = models.BooleanField()
    organizer = models.ForeignKey('Org', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length = MAX_TAG_LENGTH)

    def __str__(self):
        return self.name

class Event_Tags(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE, related_name = "event_tags")
    tags_id = models.ForeignKey('Tag',on_delete=models.CASCADE)

class Org(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    description = models.CharField(max_length = MAX_DESC_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    verified = models.BooleanField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name

class Event_Org(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    org_id = models.ForeignKey('Org',on_delete=models.CASCADE)

class Location(models.Model):
    building = models.CharField(max_length = MAX_NAME_LENGTH)
    room = models.CharField(max_length = MAX_NAME_LENGTH)
    place_id = models.CharField(max_length = MAX_NAME_LENGTH)

    def __str__(self):
        return self.room + " " + self.building

class Users(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    contact = models.EmailField(max_length = MAX_CONTACT_LENGTH)
    date_added = models.DateField(auto_now_add = True)
    url = models.ImageField(upload_to = UPLOAD_USER_IMAGE)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    num_interested = models.IntegerField()
    num_going = models.IntegerField()

    def __str__(self):
        return self.num_going

class Media(models.Model):
    name = models.CharField(max_length = MAX_NAME_LENGTH)
    file = models.FileField(upload_to="cu_events_images", blank = False)
    uploaded_by = models.ForeignKey('Org',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Event_Media(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE, related_name = "event_media")
    media_id = models.ForeignKey('Media',on_delete=models.CASCADE)

class Org_Media(models.Model):
    org_id = models.ForeignKey('Org', on_delete=models.CASCADE)
    media_id = models.ForeignKey('Media',on_delete=models.CASCADE)
