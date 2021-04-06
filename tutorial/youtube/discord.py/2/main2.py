import discord

from discord.ext import commands, tasks

client = discord.Client()
client = commands.Bot(command_prefix="?")
client.remove_command("help")

@client.event
async def on_ready():
    activity = discord.Activity(name='LIKE', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    print("Main.py | ✅")

@client.command()
async def ip(ctx):
    em = discord.Embed(title=" ", colour=0xa48ff)
    em.set_author(name="")
    em.add_field(name="Ip", value="Ip je play.kaktusekplay.tk")
    await ctx.send(embed=em) 

@client.command()  
async def like(ctx):
  em = discord.Embed(title=" ", colour=0xa48ff)
  em.set_author(name="")  
  em.add_field(name="Like", value="Dej 👍🏻")
  await ctx.send(embed=em)

@client.command()
async def tutorial(ctx):
  embed=discord.Embed(title="Discord tutoriál", description="part 2", color=0xd0095e)
  embed.add_field(name="Dej like", value="👍🏻", inline=False)
  await ctx.send(embed=embed)
  

client.run('TOKEN') 
