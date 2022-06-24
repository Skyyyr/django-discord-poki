import json
from random import randint

from discord.ext import commands
import requests


class PokemonEncounter(commands.Cog):
    """
    This is where we will 'encounter pokemon'
    """
    print(f"Loaded Handler: {__name__}")

    def __init__(self, client):
        self.client = client
        self._last_member = None
        print("Greetings initialized")

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
        """Test command to allow the user to pick which pokemon! name or id should work!"""
        pokemon = randint(1, 151)
        endpoint = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'

        API_response = requests.get(endpoint)
        responseJSON = API_response.json()

        # Pull the image url out
        image = responseJSON['sprites']['front_default']

        await ctx.send(image)


def setup(client):
    client.add_cog(PokemonEncounter(client))
