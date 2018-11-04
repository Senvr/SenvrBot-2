import discord, asyncio, os, re, datetime, random, datetime, string
from pathlib import Path
import mysql.connector
from discord.utils import get
from discord.ext import commands
import hashlib
from discord.ext.commands import Bot
prefix = "%"

bot = commands.Bot(command_prefix=prefix)
TOKEN="REPLACEME"

def readFileVar(varName):
	if Path(var).is_file():
		v=open(var,"r")
		print(var);
		v.close
		return var;
	else:
		print("ERROR: "+var+" unset!");
		return None;
def writeFileVar(var, varcontent):
	v=open(var,"w")
	v.write(str(varcontent))
	v.close
	print(var)
	return None;
def titleToId(title):
	ID=re.sub('[abcdefghijklmnopqrstuvwxyz]', '',str(hashlib.sha224(title.encode('utf-8')).hexdigest())).strip()
	return ID;
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
@bot.command(pass_context=True)
async def say(ctx, repeats):
	while int(repeats) > 0:
		repeats=int(repeats) - 1
		bot.say(str(ctx.message.content))
	
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
@bot.command(pass_context=True)
async def quickpoll(ctx, votetitle, time):
	if votetitle == "":
		bot.say("You need to input a votetitle.")
		return
	if time == "":
		bot.say("You need to input a time.")
		return
	message=ctx.message.content
	channel = ctx.message.channel
	choices = {"🇦": "Approve",
				"🇧": "Deny",
				"🇨": "Abstain"}

	vote = discord.Embed(title="**[POLL]**", description=" ", color=0x00ff00)
	value = "\n".join("- {} {}".format(*item) for item in choices.items()) 
	vote.add_field(name=votetitle, value=value, inline=True)

	message_1 = await bot.send_message(channel, embed=vote)

	for choice in choices:
		await bot.add_reaction(message_1, choice)

	await asyncio.sleep(int(time))
	message_1 = await bot.get_message(channel, message_1.id)


	counts = {react.emoji: react.count for react in message_1.reactions}
	winner = max(choices, key=counts.get)

	await bot.send_message(channel, "Option '{}' has won!".format(choices[winner]))
	#await ctx.message.clear_reactions
def setup(bot):
    bot.add_cog(QuickPoll(bot))

bot.run(TOKEN)
