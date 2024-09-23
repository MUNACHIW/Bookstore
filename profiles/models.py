from django.db import models


# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")


## while working with imagefield you need to install an extra package python -m pip install
## Pillow
