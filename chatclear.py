import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["CUNT", "BITCH", "FOTZE", "NIGGER", "JUDE", "SS", "HITLER", "ADOLF", "ADOLF HITLER", "NIGGA", "SLAVE", "SKLAVE", "JEWS", "KZ"]
bypass_list = []

@client.event
async def on_ready():
    print("Bot is online and connected to Discord")

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**YOU ARE CUTE**")
                except discord.errors.NotFound:
                    return 

client.run("NTI1OTMzNjE0NjQzMjgxOTMx.Dv91aA.xtpbWF1-fA8xRTiy7GVe7de4w9E")
