from replit import db
from config import parser_config
import discord
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)
    if ("campaigns" not in db):
        db["campaigns"] = {}


extensions = ['cogs.dev_commands', 'cogs.campaign']

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)

keep_alive()  # Starts a webserver to be pinged.
token = parser_config('token')
bot.run(token)  # Starts the bot
