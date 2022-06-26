from random import randint
from discord.ext import commands
import requests

from my_classes.pokemon_trainer import PokemonTrainer


class PokemonEncounter(commands.Cog):
    """
    This is where we will 'encounter pokemon'
    """
    print(f"Loaded Handler: {__name__}")

    def __init__(self, client):
        self.client = client
        print("PokemonEncounter initialized")

    @commands.command()
    async def test_static(self, ctx):
        """Test command to generate a hard coded pokemon"""
        endpoint = 'https://pokeapi.co/api/v2/pokemon/1'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']
        await ctx.send(image)

    @commands.command()
    async def test_pick(self, ctx, message):
        """Test command to allow the user to pick which pokemon! name or id should work!"""
        endpoint = f'https://pokeapi.co/api/v2/pokemon/{message}'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']

        await ctx.send(image)

    @commands.command()
    async def test_random(self, ctx):
        """Test command to randomly select a pokemon for the user! """
        pokemon = randint(1, 151)
        endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']
        pokemon_name = responseJSON['species']['name']

        output = f'You found a random {pokemon_name}!'
        # Send the text output first
        await ctx.send(output)
        # We send the image separately due to the URL being displayed when used in a string. (visual bug)
        await ctx.send(image)

    @commands.command()
    async def test_rand_dex(self, ctx):
        """Test command to randomly select a pokemon for the user and update the pokedex! """
        pokemon = randint(1, 151)
        endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']
        pokemon_name = responseJSON['species']['name']

        print(ctx.author.name)
        # PokemonTrainers.find_trainer_by_id(message.author)
        # PokemonTrainer.UpdatePokedex()

        output = f'You found a random {pokemon_name}!'
        # Send the text output first
        await ctx.send(output)
        # We send the image separately due to the URL being displayed when used in a string. (visual bug)
        await ctx.send(image)

    @commands.command()
    async def find_pokemon(self, ctx):
        pass



def setup(client):
    client.add_cog(PokemonEncounter(client))
