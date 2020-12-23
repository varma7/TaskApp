from django.db import models

# Create your models here.
class TODOM(models.Model):
    title = models.CharField(max_length=30,null=True)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


