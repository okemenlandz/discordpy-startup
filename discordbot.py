from discord.ext import commands
from discord.ext import tasks
from datetime import datetime 
import os
import re
import random
import traceback
import math

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN'] #heroku
alarm_list = []
version = 'ver 8.0'

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

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
		else:
			msg = f'{member.name}は{before.channel.name}から{after.channel.name}に移動した！'
			await alert_channel.send(msg)
   
	if member.guild.id == 764512399301935134 and (before.channel != after.channel):
		alert_channel = bot.get_channel(741963356663185533)
		if before.channel is None:
			msg = f'{member.name}が{after.channel.name}で通話を開始した。'
			await alert_channel.send(msg)
		else:
			msg = f'{member.name}は{before.channel.name}から{after.channel.name}に移動した！'
			await alert_channel.send(msg)
            
@bot.command()
async def ping(ctx):
	await ctx.send('pong')

@bot.command()
async def pong(ctx):
	await ctx.send('ping\npong')
        
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
async def rico(ctx):
	rico_list = ['King of Drug','さんぱーみ','たべちゃった','せーのって言ってください:pleading_face:','スイッチ入れてなかった']
	random.shuffle(rico_list)
	await ctx.send(rico_list[0])
		
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
async def ast(ctx):
	ast_list = ['時計塔','布団なら俺の隣で寝てるよ','りょったは困ります','ごふいよ','(っ\'-\')╮ =͟͟͞:pig2:']
	random.shuffle(ast_list)
	await ctx.send(ast_list[0])
	
@bot.command()
async def nmki(ctx):
	nmki_list1 = ['実力','ラック']
	nmki_list2 = ['あり','なし']
	
	random.shuffle(nmki_list1)
	random.shuffle(nmki_list2)
	await ctx.send(nmki_list1[0] + nmki_list2[0] + nmki_list1[1] + nmki_list2[1])

@bot.command()
async def sex(ctx):
	sex_list = ['SEXをしましょう。','いざ尋常に、対戦よろしくお願いします']
	random.shuffle(sex_list)
	await ctx.send(sex_list[0])

@bot.command()
async def utamaru(ctx):
	await ctx.send('懺悔します')

@bot.command()
async def connect(ctx):
	await ctx.send('＿人人人人人人＿\n＞交わした約束＜\n￣Y^Y^Y^Y^Y￣\n\n　 n\n　( ｜　 ハハ\n　 ＼＼ ( ‘-^　 )\n　　 ＼￣￣　 )\n　　　 ７　　/\n\n＿人人人＿\n＞忘れた＜\n￣Y^Y^Y￣\n\n　ハ_ハ\n（ ‘-^ 　)　　n\n￣　　 ＼　( E)')

@bot.command()
async def beyond(ctx):
	byd_list = ['(:point_up:◞‸◟):point_up:ｺﾞｩ…ﾋﾞﾖﾝ… （:point_up:՞ਊ՞）:point_up:ｺﾞｩﾋﾞﾖﾝｗｗｗｗｗｗｗｗ (ఠ๑ఠ)ლლﾁｬｯ ლლ(ఠ๑ఠ)ﾁｬｯ (ఠ๑ఠ)ლლﾁｬｯ 三へ( へ՞ਊ ՞)へ ﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹﾃﾞｹｗｗｗｗｗｗｗｗ']
	random.shuffle(byd_list)
	await ctx.send(byd_list[0])
	
@bot.command()
async def prime(ctx, *args):
	if len(args) == 0:
		await ctx.send('数字を入れてください')
	elif args[0] == '1':
		await ctx.send('1')
	elif args[0] == '0':
		await ctx.send('0')
	elif args[0].isdecimal():
		prime_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
		temp = int(args[0])
		minus_flag = False
		if temp < 0:
			temp = 0 - temp
			minus_flag = True
		res_prime = ''
		first_flag = True
		for i in range(16):
			while (temp % prime_list[i-1]) == 0:
				if first_flag:
					first_flag = False
				else:
					res_prime += '\*'
				res_prime += str(prime_list[i-1])
				temp /= prime_list[i-1]
		if temp != 1:
			if first_flag:
				first_flag = False
			else:
				res_prime += '\*'
			res_prime += str(int(temp))
		if minus_flag:
			if first_flag:
				first_flag = False
			else:
				res_prime += '\*'
			res_prime += '-1'
		await ctx.send(res_prime)
	else:
		await ctx.send('数字を入れてください')

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

@bot.command()
async def wao(ctx,*args):
	if len(args) == 0:
		cnt = int(12)
		wow_list = ['合宿免許ワオ！！','ワオ','ワオワオワオ','ワオ！！','合宿免許','合宿','免許','応援','ガール','えなこ']
		wow_str = ''
		while cnt >= 1:
			random.shuffle(wow_list)
			while(random.randint(0,1) < 1):
				wow_str += wow_list[0]
				cnt -= 1
			wow_str += wow_list[0]
			cnt -= 1
		await ctx.send(wow_str)
	elif args[0].isdecimal():
		cnt = int(args[0])
		wow_list = ['合宿免許ワオ！！','ワオ','ワオワオワオ','ワオ！！','合宿免許','合宿','免許','応援','ガール','えなこ']
		wow_str = ''
		while cnt >= 1:
			random.shuffle(wow_list)
			while(random.randint(0,1) < 1):
				wow_str += wow_list[0]
				cnt -= 1
			wow_str += wow_list[0]
			cnt -= 1
		await ctx.send(wow_str)
	else:
		cnt = int(12)
		wow_list = ['合宿免許ワオ！！','ワオ','ワオワオワオ','ワオ！！','合宿免許','合宿','免許','応援','ガール','えなこ']
		wow_str = ''
		while cnt >= 1:
			random.shuffle(wow_list)
			while(random.randint(0,1) < 1):
				wow_str += wow_list[0]
				cnt -= 1
			wow_str += wow_list[0]
			cnt -= 1
		await ctx.send(wow_str)

@bot.command()
async def val(ctx,*args):
	machine_list1 = ['とある','大海物語','アクエリオン','ウルトラセブン','エヴァ','仮面ライダー','ゴルゴ','牙狼','仕置人','無双','乙女','タイガーマスク']
	machine_list2 = ['HOTD','まどか','モモキュン','ゆゆゆ','リングミドル','リングライトミドル','冬ソナ']
	machine_list = machine_list1 + machine_list2
	if len(args) == 0:
		await ctx.send('登録されている機種はこちらです')
		mc_disp = ''
		for mc in machine_list:
			mc_disp = mc_disp + '・' + mc + '\n'
		await ctx.send(mc_disp)

def right():
	right = random.randint(0,36)
	if right < 5:
		pl_rand = random.randint(0,99)
		if pl_rand < 40:
			return 16
		elif pl_rand < 43:
			return 12
		elif pl_rand < 50:
			return 8
		else:
			return 4
	return 0

@bot.command()
async def symphogear(ctx):
	flag = True
	normal_cnt = 0
	while flag:
		v = random.randint(0,19980)
		normal_cnt += 1
		if v > 19879:
			flag = False
			
	in_money = math.ceil(normal_cnt / 10.5) * 500
	rest = math.ceil(((0 - (normal_cnt * 2)) % 21) * 125 / 21)
	await ctx.send(f'{normal_cnt}回転で当選しました。')

	pl = ''
	judge = ''
	
	if v == 19980:
		cnt = [0,0,0,0,1]
		await ctx.send('全回転:tada:')
	else:
		cnt = [0,1,0,0,0]

		for i in range(5):
			r_ch = right()
			if r_ch == 0:
				cl = random.randint(0,9999)
				if cl < 4910:
					pl += ':blue_square:'
				elif cl < 9420:
					pl += ':green_square:'
				elif cl < 9987:
					pl += ':red_square:'
				else:
					pl += ':yellow_square:'
				judge += ':x:'
				cnt[0] += 1
			elif r_ch == 16:
				cl = random.randint(0,39)
				if cl < 3:
					pl += ':rainbow:'
				else:
					cl = random.randint(0,97)
					if cl < 29:
						pl += ':blue_square:'
					elif cl < 58:
						pl += ':green_square:'
					elif cl < 82:
						pl += ':red_square:'
					else:
						pl += ':yellow_square:'
				judge += '(15)'
				cnt[0] = 0
				cnt[4] += 1
			else:
				cl = random.randint(0,97)
				if cl < 29:
					pl += ':blue_square:'
				elif cl < 58:
					pl += ':green_square:'
				elif cl < 82:
					pl += ':red_square:'
				else:
					pl += ':yellow_square:'
				judge += f'({r_ch})'
				cnt[0] = 0
				cnt[int(r_ch/4)] += 1

		await ctx.send(f'{pl}.')
		await ctx.send(f'{judge}.')
		judge = ''
		
	if cnt[0] == 5:
		await ctx.send(f'最終決戦終了\n投資:{in_money}円\n回収:{1480 + rest * 4}円\n収支:{1480 + rest * 4 - in_money}円')
	else:
		await ctx.send('シンフォギアチャンス　突入')
		while(cnt[0] < 11):
			r_ch = right()
			if r_ch == 0:
				judge += ':x:'
				cnt[0] += 1
			elif r_ch == 16:
				judge += '(15)'
				await ctx.send(judge)
				judge = ''
				cnt[0] = 0
				cnt[4] += 1
			else:
				judge += f'({r_ch})'
				await ctx.send(judge)
				judge = ''
				cnt[0] = 0
				cnt[int(r_ch/4)] += 1
		await ctx.send(f'{judge}\nシンフォギアチャンス　終了\nFEVER×{cnt[1]+cnt[2]+cnt[3]+cnt[4]}\n(4)×{cnt[1]}\n(8)×{cnt[2]}\n(12)×{cnt[3]}\n(15)×{cnt[4]}')
		total = (cnt[1]*370+cnt[2]*740+cnt[3]*1120+cnt[4]*1410+rest)*4
		await ctx.send(f'投資:{in_money}円\n回収:{total}円\n収支:{total - in_money}円')

def right_g():
	right = random.randint(0,205)
	if right < 80:
		return 3
	elif right < 100:
		return 9
	else:
		return 0

@bot.command()
async def gen(ctx):
	flag = True
	normal_cnt = 0
	while flag:
		v = random.randint(0,65535)
		normal_cnt += 1
		if v > 65329:
			flag = False
			
	in_money = math.ceil(normal_cnt / 10.5) * 500
	rest = math.ceil(((0 - (normal_cnt * 2)) % 21) * 125 / 21)
	await ctx.send(f'{normal_cnt}回転で当選しました。')

	pl = ''
	judge = ''
	
	if v == 65535:
		cnt = [0,0,1,0]
		await ctx.send('全回転:tada:')
	elif v > 65411:
		cnt = [0,0,1,0]
	else:
		cnt = [0,0,0,0]
		
	if cnt[2] == 0:
		await ctx.send(f'チャレンジ失敗\n投資:{in_money}円\n回収:{2640 + rest * 4}円\n収支:{2640 + rest * 4 - in_money}円')
	else:
		await ctx.send('超源RUSH 突入')
		while(cnt[0] < 4):
			r_ch = right_g()
			if r_ch == 0:
				judge += ':x:'
				cnt[0] += 1
			else:
				judge += f'({r_ch})'
				await ctx.send(judge)
				judge = ''
				cnt[0] = 0
				cnt[int(r_ch/3)] += 1
		await ctx.send(f'{judge}\n超源RUSH　終了\n超源RUSH×{cnt[1]+cnt[2]}\n超源BONUS×{cnt[3]}')
		total = (cnt[1]*330+cnt[2]*660+cnt[3]*990+rest)*4
		await ctx.send(f'投資:{in_money}円\n回収:{total}円\n収支:{total - in_money}円')
		
bot.run(token)
