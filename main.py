import discord, asyncio, os, re, datetime, random
from discord.ext import commands
from discord.ext.commands import Bot
prefix = "$"

bot = commands.Bot(command_prefix=prefix)
TOKEN="NTA4MjA1MTQ5MTQ4MjgyODkx.Dr72hQ.Pg6XyqE3FDqCC1Olhfbxc8V7wKQ"
@bot.event
async def on_ready():
	print('------')

	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	await bot.change_presence(game=discord.Game(name='you suck'))
	p=open("pid","w")
	p.write(str(os.getpid())+'\n')
	p.close
	print("pid="+str(os.getpid()))

	print('------')
@bot.command()
async def test():
	await bot.say(bot.user.name+" is alive!")
async def pid():
	await bot.say(str(os.getpid()))
@bot.command()
async def github():
	await bot.say("https://github.com/Senvr/SenvrBot-2")
@bot.event
async def on_command_error(error, ctx):
	await bot.send_message(ctx.message.channel, "`"+str(error)+"`")
	print(error)

bot.run(TOKEN)
