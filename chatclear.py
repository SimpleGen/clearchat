import discord
from discord.ext import commands

TOKEN = "NDg0NzU4MjY5MTY5MTA2OTY0.Dmmqrw.zXqyRWzfNZw1--eb0YY0-G8thH0"
client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("bot online.")

@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say("DELETED")

client.run(TOKEN)
