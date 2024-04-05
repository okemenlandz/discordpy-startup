import discord
import traceback
import random
from discord.ext import commands
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
version = 'ver 10.0'

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
		
@bot.command()
async def ver(ctx):
	await ctx.send(version)

@bot.command()
async def happy(ctx):
	happy_list = ['⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾','⸜(\*ˊᗜˋ*)⸝','٩(ˊᗜˋ*)و♪','(๑\'ᗢ\'๑)ฅ','（´⊙౪⊙）۶ｯｯｯｯｨｨｨｨｲｲｲｲﾖｯｼｬｱｱｱｱｧｧｧｧ!!!!',':v:(\'ω\':v: )三:v:(\'ω\'):v:三( :v:\'ω\'):v:']
	random.shuffle(happy_list)
	await ctx.send(happy_list[0])

@bot.command()
async def sad(ctx):
	sad_list = ['(｡•́︿•̀｡)','(๑ŏ _ ŏ๑)','(´இωஇ｀)',';(∩´﹏`∩);:','(∩´｡•﹏•｡`∩)','( ；o；)']
	random.shuffle(sad_list)
	await ctx.send(sad_list[0])

@bot.command()
async def doya(ctx):
	doya_list = ['(  ｰ̀֊ｰ́ )✧','╰(　・´ｰ・｀)╯','( ´･ ֊ ･` )ﾌｯ']
	random.shuffle(doya_list)
	await ctx.send(doya_list[0])

@bot.command()
async def nemochi(ctx):
	await ctx.send('ねもち…:yawning_face:')
		
@bot.command()
async def rtta(ctx, *args):
	if len(args) == 0:
		await ctx.send('りょった銅枠だし50じゃないし国士見破れないし（笑）')
	elif args[0].isdecimal():
		cnt = int(args[0])
		rtta_list = ['銅枠だし','童貞だし','50じゃないし','国士見破れないし']
		rtta_str = 'りょった'
		while cnt >= 1:
			rtta_str += rtta_list[random.randint(0, len(rtta_list)-1)]
			cnt -= 1
		await ctx.send(rtta_str + '（笑）')
	else:
		await ctx.send('りょった銅枠だし50じゃないし国士見破れないし（笑）')

@bot.command()
async def connect(ctx):
	await ctx.send('＿人人人人人人＿\n＞交わした約束＜\n￣Y^Y^Y^Y^Y￣\n\n　 n\n　( ｜　 ハハ\n　 ＼＼ ( ‘-^　 )\n　　 ＼￣￣　 )\n　　　 ７　　/\n\n＿人人人＿\n＞忘れた＜\n￣Y^Y^Y￣\n\n　ハ_ハ\n（ ‘-^ 　)　　n\n￣　　 ＼　( E)')

@bot.command()
async def beyond(ctx):
	byd_list = ['(:point_up:◞‸◟):point_up:ｺﾞｩ…ﾋﾞﾖﾝ… （:point_up:՞ਊ՞）:point_up:ｺﾞｩﾋﾞﾖﾝｗｗｗｗｗｗｗｗ (ఠ๑ఠ)ლლﾁｬｯ ლლ(ఠ๑ఠ)ﾁｬｯ (ఠ๑ఠ)ლლﾁｬｯ 三へ( へ՞ਊ ՞)へ ﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹｗｗｗｗｗｗｗｗ']
	random.shuffle(byd_list)
	await ctx.send(byd_list[0])
	
@bot.command()
async def oha(ctx):
	await ctx.send('おはよー')

@bot.command()
async def oya(ctx):
	await ctx.send('おやすみー')
	if len(args) == 0:
		await ctx.send('正しい数字を入れてください')
	elif args[0] == '1':
		await ctx.send('1')
	elif args[0] == '0':
		await ctx.send('0')
	elif args[0].isdecimal():
		first_flag = True
		res_prime = ''
		temp = int(args[0])
		for i in range(2, int(-(-int(args[0])**0.5//1))+1):
			if temp%i==0:
				while temp%i==0:
					if first_flag:
						first_flag = False
						res_prime += str(i)
						temp //= i
					else:
						res_prime += '\*'
						res_prime += str(i)
						temp //= i

		if temp!=1:
			if first_flag:
				first_flag = False
				res_prime += str(temp)
			else:
				res_prime += '\*'
				res_prime += str(temp)

		if res_prime=='':
			if first_flag:
				first_flag = False
				res_prime += args[0]
			else:
				res_prime += '\*'
				res_prime += args[0]

		await ctx.send(res_prime)
	else:
		await ctx.send('正しい数字を入れてください。')

@bot.command()
async def gag(ctx):
	per_seed = random.expovariate(0.1)
	per = round(per_seed,2)
	if per >= 100:
		per = 100
		await ctx.send(f'あなたのギャグは{per}%！:clap:')
	elif per >= 50:
		await ctx.send(f'あなたのギャグは{per}%です！')
	elif per <= 3:
		await ctx.send(f'あなたのギャグは{per}%です…あーあ')
	elif per <= 10:
		await ctx.send(f'あなたのギャグは{per}%です…')
	else:
		await ctx.send(f'あなたのギャグは{per}%です')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)