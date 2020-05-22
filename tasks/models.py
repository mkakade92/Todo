from django.db import models

# Create your models here.

class task(models.Model):
    title = models.CharField(max_length=200)
    status = models.BooleanField(default= False)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

