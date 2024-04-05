import discord
import traceback
from discord.ext import commands
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_command_error(ctx, error):
	#orig_error = getattr(error, "original", error)
	#error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	#await ctx.send(error_msg)
	sad_list = ['(｡•́︿•̀｡)','(๑ŏ _ ŏ๑)','(´இωஇ｀)',';(∩´﹏`∩);:','(∩´｡•﹏•｡`∩)','( ；o；)']
	random.shuffle(sad_list)
	await ctx.send(sad_list[0])

@bot.event
async def on_ready():
	
	msg = '起動しました。'
	
	alert_channel = bot.get_channel(744596357561712785)
	await alert_channel.send(msg)
	await alert_channel.send(version)
	
	alert_channel = bot.get_channel(741963356663185533)
	await alert_channel.send(msg)
	await alert_channel.send(version)
	
@bot.event
async def on_voice_state_update(member, before, after): 
	if member.guild.id == 744596357561712782 and (before.channel != after.channel):
		alert_channel = bot.get_channel(744596357561712785)
		if before.channel is None:
			msg = f'{member.name}は{after.channel.name}'
			await alert_channel.send(msg)
		elif after.channel is None:
			msg = f'{member.name}はいなくなった。'
			await alert_channel.send(msg)
		else:
			msg = f'{member.name}は{before.channel.name}から{after.channel.name}に移動した！'
			await alert_channel.send(msg)
   
	if member.guild.id == 764512399301935134 and (before.channel != after.channel):
		alert_channel = bot.get_channel(862005213233938443)
		if before.channel is None:
			msg = f'{member.name}が{after.channel.name}で通話を開始した。'
			await alert_channel.send(msg)
		elif after.channel is None:
			msg = f'{member.name}はいなくなった。'
			await alert_channel.send(msg)
		else:
			msg = f'{member.name}は{before.channel.name}から{after.channel.name}に移動した！'
			await alert_channel.send(msg)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)