from rest_framework import serializers
from .models import Drone, DroneCategory, Pilot, Competition

from django.contrib.auth.models import User


class UserDroneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drone
        fields = ('url', 'name')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    drones = UserDroneSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'drones')



class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='drone-detail')

    class Meta:
        model = DroneCategory
        fields = (
            'url',
            'pk',
            'name',
            'drones')


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    # Display the category name
    drone_category = serializers.SlugRelatedField(queryset=DroneCategory.objects.all(),
                                                  slug_field='name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Drone
        fields = (
            'url',
            'name',
            'drone_category',
            'owner',
            'manufacturing_date',
            'has_it_competed',
            'inserted_timestamp')


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    # Display all the details for the related drone
    drone = DroneSerializer()

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_feet',
            'distance_date',
            'drone')


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(
        choices=Pilot.GENDER)
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True)

    class Meta:
        model = Pilot
        fields = (
            'url',
            'name',
            'gender',
            'gender_description',
            'races_count',
            'inserted_timestap',
            'competitions')


class PilotCompetitionSerializer(serializers.ModelSerializer):
    # Display the pilot's name
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(), slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(), slug_field='name')

    class Meta:
        model = Competition
        fields = (
            'url',
            'pk',
            'distance_feet',
            'distance_date',
            'pilot',
            'drone')

