from django.db import models

class Currency(models.Model):
    code = models.CharField(unique=True,max_length=3)
    name = models.CharField(max_length=100,null=True)
    rate = models.FloatField(null=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code