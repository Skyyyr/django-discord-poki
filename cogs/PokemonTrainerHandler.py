import json
from random import randint

import requests
from discord.ext import commands

from my_classes.pokemon_trainer import PokemonTrainer

# Starter pokemon by ID
STARTER_POKEMON = [
    1,  # Bulbasaur
    4,  # Charmander
    7,  # Squirtle
]


class PokemonTrainers(commands.Cog):
    """
    This is where we will 'Create and Manage our pokemon trainers'
    """
    print(f"Loaded Handler: {__name__}")

    def __init__(self, client):
        self.client = client
        print("PokemonTrainers initialized")

    @commands.command()
    async def become_trainer(self, ctx):
        """Let's try to add new trainer to stored json"""
        pokemon_id = randint(0, len(STARTER_POKEMON) - 1)
        endpoint = f'https://pokeapi.co/api/v2/pokemon/{STARTER_POKEMON[pokemon_id]}'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']
        pokemon_name = responseJSON['species']['name']

        # Let's add the trainer with their new starter
        AddNewTrainerJson(ctx.author.name, STARTER_POKEMON[pokemon_id])

        output = f'Your starter pokemon is: {pokemon_name}!'
        # Send the text output first
        await ctx.send(output)
        # We send the image separately due to the URL being displayed when used in a string. (visual bug)
        await ctx.send(image)

    @commands.command()
    async def find_trainer_by_id(self, ctx, trainer_id):
        for trainer in PokemonTrainer.all_trainers[0]:
            if trainer.trainer_id == int(trainer_id):
                return await ctx.send(trainer)
        return await ctx.send(f"No trainer found by that id, max trainer IDs: {len(PokemonTrainer.all_trainers[0])}")

    @commands.command()
    async def find_trainer_by_name(self, ctx, trainer_name):
        for trainer in PokemonTrainer.all_trainers[0]:
            if trainer.trainer_name.lower() == trainer_name.lower():
                return await ctx.send(trainer)
        return await ctx.send(f"No trainer found by that name.")


def AddNewTrainerJson(trainer_name, starter_id):
    with open('data/trainers/pokemon_trainers.json', 'r+') as file:
        trainer_data = json.load(file)
        print(len(trainer_data[0]))
        new_trainer = {
            "trainer_id": len(PokemonTrainer.all_trainers[0]) + 1,
            "trainer_name": trainer_name,
            "trainer_pokedex": [],
            "trainer_inventory": [],
            "trainer_current_pokemon": starter_id
        }
        trainer_data.append(new_trainer)
        file.seek(0)
        json.dump(trainer_data, file, indent=4)

        # Create an instance of the new trainer
        instance_trainer = PokemonTrainer(**new_trainer)
        # Add it to our list of trainer instances
        PokemonTrainer.all_trainers[0].append(instance_trainer)


def setup(client):
    client.add_cog(PokemonTrainers(client))
