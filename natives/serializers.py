from rest_framework import serializers

from .models import Native, Cohort

class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cohort
        fields= "__all__"

        

class NativeSerializer(serializers.ModelSerializer):
    cohort= serializers.SerializerMethodField()
    remark= serializers.SerializerMethodField()

    class Meta:
        model= Native
        fields ="__all__"
  

    def get_cohort(obj):
        return obj.cohort.name

    def get_remark(self, obj):
        return "Trust the process"


        # ('id', 'email', 'first_name', 'last_name', 'gender', 'date_of_birth', 'cohort', 'date_created')