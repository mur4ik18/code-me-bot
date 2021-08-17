import os
import discord
from settings import *


intents = discord.Intents.default()
intents.members = True
bot = discord.Client(intents=intents)
@bot.event
async def on_member_join(member):
    if welcome_channel := member.guild.get_channel(877256999409168436):
        await welcome_channel.send(f"Welcome, {member.mention} to {member.guild.name}")
        print(f"Welcome, {member.mention} to {member.guild.name}")
bot.run(BOT_TOKEN)