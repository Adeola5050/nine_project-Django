from django.contrib import admin
from natives .models import Native, Cohort

# Register your models here.
admin.site.register(Cohort)
admin.site.register(Native)