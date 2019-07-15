from rest_framework import serializers

from .models import Toy


class ToySerializer(serializers.ModelSerializer):

    class Meta:
        model = Toy
        fields = ('id', 'name', 'description', 'release_date', 'toy_category', 'included_inhome')


