from django.db import models
import uuid


class BaseModel(models.Model):
    
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default = uuid.uuid4, unique = True, editable=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(blank = True, null = True)
   

class State(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class City(BaseModel):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Specialization(BaseModel):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

