from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Restaurant(AbstractUser):
    restaurant_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u"{}".format(self.username)


class Table(models.Model):
    table_name = models.CharField(max_length=10, help_text="example: 103 (do not put 'table 103' just '103'")
    seats = models.SmallIntegerField(help_text="number of maximum available seats at the table")
    x_position = models.SmallIntegerField(help_text="grid", default=0)
    y_position = models.SmallIntegerField(help_text="grid", default=0)
    premise = models.ForeignKey(Restaurant, related_name='tables')

    def __unicode__(self):
        return u"{}".format(self.table_name)


class Party(models.Model):
    party_name = models.CharField(max_length=50, help_text="enter this if you know the name of the party so you can save their data", blank=True)
    number_of_males = models.CharField(max_length=2)
    number_of_females = models.CharField(max_length=2)
    number_of_children = models.CharField(max_length=2)
    lunch = models.BooleanField(help_text="check true for lunch or false for dinner", default=False)
    # dinner = models.BooleanField(help_text="check true for dinner", default=False)
    monday_to_thursday = models.BooleanField(help_text="check true for Monday to Thursday or false for Friday to Sunday", default=False)
    # friday_to_sunday = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True, null=True)
    reservation_time = models.DateTimeField(null=True)
    predicted_end_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    total_time = models.CharField(max_length=2, blank=True)
    seated_table = models.ForeignKey(Table, related_name='parties')

    def __unicode__(self):
        return u"pk:{} name:{}".format(self.pk, self.party_name)
