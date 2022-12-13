from discord.ext import commands
from replit import db


class CampaignCommands(commands.Cog, name='Campaign Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='add_campaign', aliases=['add_cg'])
    async def add_campaign(self, ctx, name):
        author_id = ctx.author.id
        if (str(author_id) not in db['campaigns']):
            db['campaigns'][str(author_id)] = {}
        if (name != '' and name is not None
                and name not in db['campaigns'][str(author_id)]):
            db['campaigns'][str(author_id)][str(name)] = {}
            await ctx.send("Campaign %s was added..." % name)
        elif (name != "" and name in db['campaigns'][str(author_id)]):
            await ctx.send("Campaign %s was already added..." % name)


def setup(bot):
    bot.add_cog(CampaignCommands(bot))
