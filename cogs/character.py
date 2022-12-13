from discord.ext import commands
from replit import db


class CharacterCommands(commands.Cog, name='Character Commands'):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(CharacterCommands(bot))
