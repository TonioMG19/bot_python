import discord
import asyncio

client = discord.Client()

prefix = '!'

@client.event
async def on_ready():
	print("Capitaine Salamèche à l'écoute !")

@client.event
async def on_message(message):
	if message.content.startswith(prefix+"hello"):
		await message.channel.send("Bonjour humain !")
	elif message.content.startswith(prefix+"carapuce"):
		await message.channel.send("Beurkkkk")

client.run("TOKEN")