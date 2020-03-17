from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from rest_framework.reverse import reverse as api_reverse


class Property(models.Model):
    area = models.FloatField(_("Area"), blank = True, null = True)
    sector = models.CharField(_("Sector"), blank = True, null = True, max_length = 255)
    url = models.URLField(_("Url"), blank=True, null = True)
    # Date & Time
    created = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name = _('Created'))
    updated = models.DateTimeField(auto_now_add = False, auto_now = True, verbose_name = _('Updated'))

    def get_absolute_url(self):
        return reverse("App:detail", kwargs={"id": self.id})

    def get_api_url(self, request = None):
        return api_reverse("App:detail_api", kwargs={"id": self.id}, request = request)


    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
        ordering = ['-created',]


    # str
    def __str__(self):
        return (self.sector)


    # OverRiding Save Method
    # https://docs.djangoproject.com/en/2.1/topics/db/models/#overriding-predefined-model-methods
    def save(self, *args, **kwargs):
        # Call the "real" save() method.
        super().save(*args, **kwargs)
        # do_something_else()

