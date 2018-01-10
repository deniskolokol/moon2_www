from django.db import models


class SocialResource(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(max_length=500)
    img_url = models.CharField(max_length=500)
    order_id = models.IntegerField(default=0, help_text='Order in which logo appears in the stripe')

    def __unicode__(self):
        return "%s: %s" % (self.name, self.title)


class MenuItem(models.Model):
    """
    Menu items supporting tree structure.
    Submenu for a particlar item:
    MenuItem.objects.get(pk=XXX).children.all()
    """
    label = models.CharField(max_length=20)
    uri = models.CharField(max_length=20)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    order_id = models.IntegerField(default=0, help_text='Order id on its level')
    is_active = models.BooleanField(default=True)

    @classmethod
    def active(cls):
        return cls.objects.filter(is_active=True)

    def __unicode__(self):
        return "%s: %s" % (self.label, self.uri)
