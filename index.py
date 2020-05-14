import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
	print("Capitaine Salamèche à l'écoute !")

@client.event
async def on_message(message):
	print(message.content)

client.run("NzEwNDA2MDAwMDk1NjU4MDQ4.Xr0AYg.UxYrg8ji4Mb4pnlVgqf6WcBtoIU")