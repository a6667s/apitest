from django.db.models import fields
from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['id','name']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields =['id','title','job_type','description','start_data','education','experience','external_title']
    def to_representation(self, instance):
        self.fields['job_type'] =  CategorySerializer(read_only=True)
        return super(JobSerializer, self).to_representation(instance)
