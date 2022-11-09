import discord
from discord.ext import commands, tasks
import logging
import os
import requests
import json
import random
from time import sleep
#from keep_alive import keep_alive
#from replit import db
import datetime
intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.',intents = intents)

record={} 

logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game(".ban @user")
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.command()
async def get_list(ctx):
   for member in ctx.guild.members():
     if member.joined_at() == datetime.today():
         await ctx.send(f'{member.id} {member.username}#{member.discrimimator}')
  await ctx.send("Done")
#ADD ACTUAL CODE HERE LATER



#keep_alive()
client.run("#YourToken")
