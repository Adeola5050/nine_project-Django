from django.db import models 
from natives .models import Native

# Create your models here.
class Project(models.Model):
    native = models.ForeignKey(Native, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description =  models.TextField()
    technology = models.CharField(max_length=20)
    image= models.TextField(
        default="https://www.google.com/search?q=project+pictures&sxsrf=APq-WBsU6Suf488SX_2ObVXe3_1rZz1RxA:1650975930475&tbm=isch&source=iu&ictx=1&vet=1&fir=-fYMhJVy5RCEEM%252CNUk3eASDzWDK0M%252C_%253Bo0zll3oqw4j-eM%252CUifZyDUnlSYq7M%252C_%253BG0mLAvJ6uYLasM%252CsdRkupVb-Ty4CM%252C_%253B3_4T0zmNGf7tXM%252CGOC80YKbPOQbTM%252C_%253BbWZj52nNJUNDDM%252CNUk3eASDzWDK0M%252C_%253BzRlpGKZhW8xYrM%252CGOC80YKbPOQbTM%252C_%253BD46w2ar0ouC2QM%252CUifZyDUnlSYq7M%252C_%253B7XaUuN4a8a5XeM%252CKFCt2xvBxTJaeM%252C_%253BTYeIvhdXFlnFNM%252CR7aC3OmqWI11TM%252C_%253BHa0G5lnFRIkHBM%252Cl1MmW4-skzeskM%252C_%253BH0u5UrGzSQFfqM%252Chpi2UnhFj1_G0M%252C_%253BD-DJaUG_iv0MyM%252CGOC80YKbPOQbTM%252C_&usg=AI4_-kSziPnjBWIc06pILNCMfHiRsGCWzQ&sa=X&ved=2ahUKEwjB6_jO3LH3AhXkg_0HHVbjB6oQ9QF6BAggEAE#imgrc=G0mLAvJ6uYLasM"

    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
