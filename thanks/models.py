from django.db import models

# Create your models here.
class customer(models.Model):
    name = models.CharField(max_length = 30)
    # email = models.EmailField(max_length = 200)
    message = models.CharField(max_length = 270)
    # ph = models.IntegerField()

    def __str__(self):
        return self.name 