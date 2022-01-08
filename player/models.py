from django.db import models

class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    playname = models.CharField(max_length=60)

    def __str__(self):
        return self.playname
