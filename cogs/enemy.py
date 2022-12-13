from discord.ext import commands
from replit import db


class EnemyCommands(commands.Cog, name='Enemy Commands'):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(EnemyCommands(bot))