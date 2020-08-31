# serializers.py
from rest_framework import serializers

from .models import *

class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeveloperContacts
        fields = ('id','name', 'phone_contact', 'email', 'country', 'developer_category',)
