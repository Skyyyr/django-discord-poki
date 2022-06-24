import discord
from discord.ext import commands


class Greetings(commands.Cog):
    """
    This is an example from the api documentation with some added prints and a test command
    This should be used as a starting point or reference when making additional cogs
    """
    print(f"Loaded Handler: {__name__}")

    def __init__(self, client):
        self.client = client
        self._last_member = None
        print("Greetings initialized")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command()
    async def test(self, ctx):
        print("Test command")
        await ctx.send("Responding...")


def setup(client):
    client.add_cog(Greetings(client))
