import json
import os

from discord.ext import commands

from my_classes.pokemon_trainer import PokemonTrainer

"""
    This is our base file for our bot
    We want to keep this as clean, and minimal as possible
        'minimal' -> Don't add additional features directly in this file, 
                                but instead attach them or call them here.
"""


def get_prefix_and_token():
    """
        Since each token is unique we don't want to publicly store the token variable
        so it's secured in a json file along with our prefix
    :return: prefix, token
    """
    with open('token.json') as f:
        data = json.load(f)
        token = data["TOKEN"]
        prefix = data["PREFIX"]
        return prefix, token


# Grab the data from json
PREFIX, TOKEN = get_prefix_and_token()

# Apply our prefix to the bot
client = commands.Bot(command_prefix=PREFIX)


@client.event
async def on_ready():
    """
    When the discord bot comes online this happens...
    :return:
    """
    print(f"we have logged in as {client}")
    # We load any cogs
    load_extensions()
    load_trainers()


@client.event
async def on_message(message):
    """
    Whenever a message is sent in any channel the discord bot has access to
    :param message: the message any user or bot has sent
    :return:
    """
    if message.author == client.user:
        return

    # Split the username right after the # and use that
    username = str(message.author).split('#')[0]
    # Grab the message
    user_message = str(message.content)
    # Grab the channel
    channel = str(message.channel.name)
    # Display it to the console
    print(f'{username}: {user_message} ({channel})')
    # Process any potential commands (cogs)
    await client.process_commands(message)


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} reacted with {reaction.emoji}')


@client.command()
async def load(ctx, cog_handler):
    """Manually load a cog"""
    client.load_extension(f'cogs.{cog_handler}')


@client.command()
async def unload(ctx, cog_handler):
    """Manually unload a cog"""
    client.unload_extension(f'cogs.{cog_handler}')


def load_extensions():
    """
    Load all cogs
    :return:
    """
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            # cut off the .py
            client.load_extension(f'cogs.{filename[:-3]}')


def load_trainers():
    cur_path = os.path.abspath(os.path.dirname(__file__))
    trainer_path = os.path.join(cur_path, "data/trainers/pokemon_trainers.json")

    loaded_trainers = []
    with open(trainer_path) as data_file:
        reader = json.load(data_file)
        for row in reader:
            trainer = PokemonTrainer(**row)
            loaded_trainers.append(trainer)
    PokemonTrainer.all_trainers.append(loaded_trainers)
    # print(len(PokemonTrainer.all_trainers[0]))


# Keep this at the bottom - it is the direct link to the bot to turn it online
client.run(TOKEN)
