from django.db import models

# Create your models here.

class pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()

class basestats(models.Model):
    poke_id = models.ForeignKey(pokemon, on_delete=models.CASCADE)
    stat = models.CharField(max_length=50)

class evolutions(models.Model):
    poke_id = models.ForeignKey(pokemon, on_delete=models.CASCADE)
    evolution_secuence = models.IntegerField()
    evolution = models.CharField(max_length=50)