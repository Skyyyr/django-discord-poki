from django.db import models


# Create your models here.

class SeenPokemon(models.Model):
    pokemon_name = models.CharField(max_length=50)
    last_seen_date = models.DateTimeField()

    def __str__(self):
        return f'Name: {SeenPokemon.pokemon_name}'
