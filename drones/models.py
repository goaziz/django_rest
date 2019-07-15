from django.db import models


class DroneCategory(models.Model):
    name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Drone(models.Model):
    name = models.CharField(max_length=150, unique=True)
    drone_category = models.ForeignKey(DroneCategory, related_name='drones', on_delete=models.CASCADE)
    manufacturing_date = models.DateTimeField()
    has_it_competed = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='drones', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Pilot(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    )

    name = models.CharField(max_length=150, blank=False, unique=True)
    gender = models.CharField(max_length=8, choices=GENDER, default=MALE)
    races_count = models.IntegerField()
    inserted_timestap = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Competition(models.Model):
    pilot = models.ForeignKey(Pilot, related_name='competitions', on_delete=models.CASCADE)
    drone = models.ForeignKey(Drone, on_delete=models.CASCADE)
    distance_feet = models.IntegerField()
    distance_date = models.DateTimeField()

    class Meta:
        ordering = ('-distance_feet',)