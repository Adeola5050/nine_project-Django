from django.db import models

# Create your models here.

GENDER=(
        ('male','male'),
        ('female', 'female'),
        ('others', 'others')
    )
    
    
class Cohort(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    date_created = models. DateTimeField(auto_now_add=True)


    
class Native(models.Model):
    cohort= models.ForeignKey(Cohort, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
    first_name= models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number= models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='others')
    date_of_birth= models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name+" " + self.last_name
