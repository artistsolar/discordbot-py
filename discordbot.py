from cmath import log
from distutils.sysconfig import PREFIX
import discord
from discord.ext import commands
import requests
from dotenv import load_dotenv
import os
load_dotenv()
import requests

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']      

bot = commands.Bot()

bot.slash_command(name="first_slash", guild_ids=[...]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
