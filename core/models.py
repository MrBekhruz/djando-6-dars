from django.db import models
import uuid
 
class Company(models.Model):
    name = models.CharField(max_length=255)
    about = models.TextField()
    logo = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    def __str__(self):
        return self.name