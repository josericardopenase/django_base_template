from email.policy import default
from typing import Iterable, Optional
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.db import (
    router,
)
from django.db.models.deletion import CASCADE, Collector


class ScheduleModel(models.Model):

    calendar_frame = models.IntegerField(default=45)

    monday = models.BooleanField(default=True)
    monday_start = models.TimeField(default="8:00")
    monday_finish = models.TimeField(default="18:00")

    tuesday = models.BooleanField(default=True)
    tuesday_start = models.TimeField(default="8:00")
    tuesday_finish = models.TimeField(default="18:00")

    thursday = models.BooleanField(default=True)
    thursday_start = models.TimeField(default="8:00")
    thursday_finish = models.TimeField(default="18:00")

    wednesday = models.BooleanField(default=True)
    wednesday_start = models.TimeField(default="8:00")
    wednesday_finish = models.TimeField(default="18:00")

    friday = models.BooleanField(default=True)
    friday_start = models.TimeField(default="8:00")
    friday_finish = models.TimeField(default="18:00")

    saturday = models.BooleanField(default=True)
    saturday_start = models.TimeField(default="8:00")
    saturday_finish = models.TimeField(default="18:00")

    sunday = models.BooleanField(default=False)
    sunday_start = models.TimeField(default="8:00")
    sunday_finish = models.TimeField(default="13:00")

    class Meta:
        abstract = True


class ReceiverModel(models.Model):
    def on_save(self, instance):
        pass

    def pre_save(self):
        pass

    def on_update(self, instance):
        pass

    def on_delete(self, instance):
        pass

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.pre_save(self)
        new_instance = super().save(force_insert, force_update, using, update_fields)
        self.on_save(self, new_instance)
        return new_instance

    def delete(self, using=None, keep_parents=False):
        # TODO: WESTWORLD
        if self.pk is None:
            raise ValueError(
                "%s object can't be deleted because its %s attribute is set "
                "to None." % (self._meta.object_name, self._meta.pk.attname)
            )
        using = using or router.db_for_write(self.__class__, instance=self)
        collector = Collector(using=using, origin=self)
        collector.collect([self], keep_parents=keep_parents)
        coll = collector.delete()
        self.on_delete(self, self)
        return coll

    class Meta:
        abstract = True


class BaseModel(models.Model):
    """

    Abstract class that makes herency from other classes
    in the django app

    """

    created = models.DateTimeField(
        "created at",
        auto_now_add=True,
        help_text="Date time on which the object was created",
    )

    modified = models.DateTimeField(
        "Modified at",
        auto_now=True,
        help_text="Date time on which the object was modified",
    )

    extra_field = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        abstract = True
        get_latest_by = "created"
        ordering = ["-created", "-modified"]
