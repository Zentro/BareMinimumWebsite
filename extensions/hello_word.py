import discord
from discord.ext import commands
from discord.ext.commands import Context

class HelloWorld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot