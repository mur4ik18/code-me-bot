import os
import discord
from settings import *
from discord.ext import commands
from discord_components import Button, DiscordComponents, ButtonStyle, InteractionType
from discord import channel
from discord.utils import get


client = discord.Client()
bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
    DiscordComponents(bot)
    
@bot.command(name='дай', help="Выдать роль")
async def price(ctx):
    if str(ctx.channel.id) == '877276649727590461':    
        await ctx.reply(
            f"Милорд, на какой товар Вам показать цены?",
            components=[
                [
                    Button(style=ButtonStyle.blue, label="Кодер", emoji="🎨"),
                    Button(style=ButtonStyle.blue, label="Анимешник", emoji="👧"),
                    Button(style=ButtonStyle.blue, label="Геймер", emoji="🎮"),
                    Button(style=ButtonStyle.blue, label="Зумер", emoji="👶"),
                    Button(style=ButtonStyle.blue, label="Бумер", emoji="👴")
                ]])
        result = await bot.wait_for("button_click")
        membeer = ctx.author
        print(result.component.label)
        role = discord.utils.get(ctx.guild.roles, name=result.component.label) 
        await membeer.add_roles(role ,atomic=False)
        await result.respond(
                        type=InteractionType.UpdateMessage,
                        content="Роль выдана, хорошего дня!",
                        components=[])
        
@bot.command(name='уу3321032',pass_context = True)
async def clear(ctx):
    mgs = [] #Empty list to put all the messages in the log
    async for x in ctx.message.channel.history(limit = 500):
        await x.delete()
bot.run(BOT_TOKEN)