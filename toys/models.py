from django.db import models



class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name =  models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=150, blank=True)
    toy_category = models.CharField(max_length=150, blank=False)
    release_date = models.DateTimeField()
    included_inhome = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
