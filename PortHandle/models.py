from time import strftime
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    mail = models.CharField(max_length=30)
    subject = models.CharField(max_length=150)
    msg = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        x = self.timestamp
        date = x.strftime("%m/%d/%Y at %H:%M:%S %p")
        
        
        return 'Message From ' + self.mail +' on ' + date
