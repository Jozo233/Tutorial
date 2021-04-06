import discord

from discord.ext import commands, tasks

client = discord.Client()
client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    activity = discord.Activity(name='xxx', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Main.py | ✅")

@client.command()
async def ip(ctx):
    em = discord.Embed(title=" ", colour=0xa48ff)
    em.set_author(name="")
    em.add_field(name="Ip", value="Ip je <vaše ip>")
    await ctx.send(embed=em) 

  

client.run('TOKEN') 
