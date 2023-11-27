from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    prompt = models.CharField(max_length=512)
    response = models.TextField()
    

    def __str__(self):
        return f"{self.prompt}: {self.response}"

class ChatingRoom(models.Model):
    name = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    temp2 = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return f'{self.user}-{self.name}'

class Message(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    ChatingRoom = models.ForeignKey(ChatingRoom, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.ChatingRoom}-{self.prompt}-{self.response}'



