from rest_framework import serializers
from myapp.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'pfile']