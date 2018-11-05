import discord, asyncio, os, re, datetime, random, datetime, string
from pathlib import Path
import mysql.connector
from discord.utils import get
from discord.ext import commands
import hashlib
from discord.ext.commands import Bot
prefix = "!"
bot = commands.Bot(command_prefix=prefix)
TOKEN="NTA4MjA1MTQ5MTQ4MjgyODkx.DsEUoQ.bU0FAE03dEPrwK72BwJfCYSSoWY"
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
async def vote(ctx, votetitle, time, format):
	await bot.delete_message(ctx.message)
	print(ctx.message.content)
	print("vote began")
	message=ctx.message.content
	channel = ctx.message.channel
	choices = { 
				"❎": "No",
				"✅": "Yes",	
				}
	regex = re.compile('[^a-zA-Z0-9 ]')
	format = regex.sub('', format.strip())
	if format == "seconds":
		time2=str(int(time))
	elif format == "minutes":
		time2=str(int(time)*60)
	elif format == "hours":
		time2=str(int(time)*3600)
	elif format == "days":
		time2=str(int(time)*86400)
	else:
		warningmsg = await bot.say("Your format doesn't work! \nYou used: **"+format+"**.\nWe take: \n seconds\n minutes\n hours\n days")
		await asyncio.sleep(3)
		await bot.delete_message(warningmsg)
		return;
	
	vote = discord.Embed(title="**VOTE IN PROGRESS**", description="**"+str(ctx.message.author.name)+"** Has Created a Poll\nVoting Time Expires in "+time+" "+format, color=0x00ffff)
	print(time2)
	value = "\n".join(" {} \n{}".format(*item) for item in choices.items()) 
	vote.add_field(name="**"+votetitle+"**", value=value, inline=True)

	message_1 = await bot.send_message(channel, embed=vote)

	for choice in choices:
		await bot.add_reaction(message_1, choice)

	await asyncio.sleep(int(time2))
	message_1 = await bot.get_message(channel, message_1.id)

	
	counts = {react.emoji: react.count for react in message_1.reactions}
	totalReactions=-2
	for react in message_1.reactions:
		totalReactions=totalReactions+react.count
	totalReactions=totalReactions
	print(totalReactions)
	winner = max(choices, key=counts.get)
	members=len(ctx.message.server.members)
	
	print(str(counts)[3:].strip())
	if totalReactions > 0:
		if winner == "✅":
			verdict=discord.Embed(title="**"+votetitle+"** ENDED", description="The action was **approved**.\nThere were "+str(totalReactions)+" votes total.", color=0x00ff00)
			await bot.send_message(discord.Object(id='508860940133859389'), embed=verdict)
		else:
			verdict=discord.Embed(title="**"+votetitle+"** ENDED", description="The action was **denied**.\nThere were "+str(totalReactions)+" votes total.", color=0xff0000)
			await bot.send_message(discord.Object(id='508860940133859389'), embed=verdict)
	else:
		verdict=discord.Embed(title="**"+votetitle+" ENDED:**", description="Insufficient amount of votes! \nThere were "+str(totalReactions)+".", color=0x000000)
		await bot.send_message(discord.Object(id='508860940133859389'), embed=verdict)
	await bot.delete_message(message_1)
	print("vote ended")
	#await ctx.message.clear_reactions
def setup(bot):
    bot.add_cog(QuickPoll(bot))

bot.run(TOKEN)
