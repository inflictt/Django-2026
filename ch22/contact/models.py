from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name=models.CharField(max_length=199)    
    message=models.TextField()    
    created_at=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name