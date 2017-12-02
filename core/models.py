from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


COLUMNS_MAX = 5


class Unit(models.Model):
    token = models.CharField(max_length=20, blank=False, null=False, db_index=True)
    title = models.CharField(max_length=1024, blank=True, null=True, db_index=True)
    annotation = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        """"Update timestamps on save."""
        # XXX - update all corresponding Sections here
        return super(Unit, self).save(*args, **kwargs)

    def __unicode__(self):
        if self.title:
            return "%s: %s" % (self.token, self.title)
        return self.token


class Section(models.Model):
    label = models.CharField(max_length=20, blank=False, null=False, db_index=True)
    bg_image = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    updated = models.DateTimeField()
    units = models.ManyToManyField(Unit, through='Content')

    def save(self, *args, **kwargs):
        """"Update timestamps on save."""
        self.updated = timezone.now()
        return super(Section, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.label


class Content(models.Model):
    section = models.ForeignKey(Section, null=True, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, null=True, on_delete=models.CASCADE)
    column = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(COLUMNS_MAX-1) # this refers to index, not number
            ]
        )
    order_id = models.IntegerField(default=0, help_text='Order in a column')

    def save(self, *args, **kwargs):
        """"Update timestamps on save."""
        # XXX - update all corresponding Sections here
        return super(Content, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s: %s" % (self.section.label, self.unit.token)

    @classmethod
    def get_columns(cls, **filters):
        qs = cls.objects.filter(**filters).order_by('column', 'order_id')
        columns = [[] for _ in range(COLUMNS_MAX)]
        for unit in qs:
            columns[unit.column].append(unit)
        return columns


class SocialResource(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=500)
    img_url = models.CharField(max_length=500)
    order_id = models.IntegerField(
        default=0,
        help_text='Order in which logo appears in the stripe'
        )

    def __unicode__(self):
        return "%s: %s" % (self.name, self.title)
