description = """ree"""

# discord system imports
import discord
from discord.ext import commands

# python stdlib imports
import random
import asyncio
from io import BytesIO
from datetime import datetime

# file imports
import connec4

# bot init
bot = commands.Bot(command_prefix="ree ", description=description)

TOKEN = input("Enter token > ").strip()

@bot.event
async def on_ready():

    await bot.get_channel(740143419975925841).send("Yall thought i was gone but i'm back nerds")

    activity = discord.Game(name="with your feelings", type=3)
    await bot.change_presence(activity=activity)

    print(f'Success. Welcome {bot.user} to the real world.')
    bot.add_cog(connec4.connec4(bot))

@bot.command(description="ping the bot")
async def ping(ctx):
    await ctx.send(f"{ctx.author.mention}, reeeee")

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content.lower().find("i am ") != -1 and message.author.id!=199769557768994817:
        await message.channel.send("hi " + message.content[ message.content.lower().find("i am ")+5:])

    if message.content.lower().find("i'm ") != -1 and message.author.id!=199769557768994817:
        await message.channel.send("hi " + message.content[ message.content.lower().find("i'm ")+4:])

    if message.content.lower().find("im ") != -1 and message.author.id!=199769557768994817:
        await message.channel.send("hi " + message.content[ message.content.lower().find("im ")+3:])

    await bot.process_commands(message)

bot.run(TOKEN)
