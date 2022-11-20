import discord
from discord.ext import commands
import logging
import random
import datetime

intents = discord.Intents(guilds = True, reactions = True, members = True, presences = True, messages = True)
client = commands.Bot(command_prefix = '.', intents = discord.Intents.all())

record={} 

#logging.basicConfig(level=logging.INFO)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game(".b(an) @user")
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.command()
async def get_list(ctx):
    for member in ctx.guild.members():
     if member.joined_at() == datetime.today():
         await ctx.send(f'{member.id} {member.username}#{member.discrimimator}')
    await ctx.send("Done")
#ADD ACTUAL CODE HERE LATER

@client.command(aliases=['b','ben','bann','ba','nab', 'n'])
async def ban(ctx, member : discord.Member):
    try:
        await member.ban(reason="Banned by BanBot", delete_message_days=0)
        await ctx.send(f'{member} has been banned by {ctx.author}')
        await ctx.message.delete()
        record[ctx.author.id] = member.id
    except Exception:
        await ctx.send(f"{ctx.author} failed to ban {member.name}#{member.discriminator}")
        return

@client.command()
async def reset(ctx):
    print('resetting')
    async for ban in ctx.guild.bans():
        await ban.unban()
    channel = ctx.guild.get_channel(828418370776989719)
    await channel.purge(limit=1000)
    await channel.set_permissions(ctx.guild.default_role, view_channel=False)
    msg = 'Current Score: \n'
    score = {}
    for person in record:
        if person not in score:
            score[person] = 1
        else:
            score[person] += 1
    for member in score:
        msg = msg + f'`<@{member}>` banned **{score[member]}** users. \n'
    msg = msg + '\n'
    await channel.send(msg)
    record.clear()
    await ctx.send('Reset Complete.')

@client.command()
async def start(ctx):
    invites = await ctx.guild.invites()
    if invites != []:
        for invite in invites:
            await invite.delete()
    channel = ctx.guild.get_channel(828418370776989719)
    await channel.send('Starting BanBot Game')
    await channel.set_permissions(ctx.guild.default_role, view_channel=True)
    await ctx.send('@everyone THE GAMES HAVE BEGUN. BAN YOUR FRIENDS')

#ADD YOUR TOKEN!
client.run("#YourToken")
