import discord
from discord.ext import commands 

bot = commands.bot("!")

@bot.event
async def on_ready():
    print("Estou pronto! Estou conectado como {bot.user}")

bot.run("ODkzMTEyNjU5MzY3NTgzNzU0.YVWt-w.B1pKSMr91fq85_95ZiN9wsFGJUU")