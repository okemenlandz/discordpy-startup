import discord
import traceback
import random
import math
import requests
import json
import datetime
from discord.ext import commands
from os import getenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
version = 'ver 10.0'

@bot.event
async def on_command_error(ctx, error):
	orig_error = getattr(error, "original", error)
	error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
	alert_channel = bot.get_channel(1298134191418114180)
	await alert_channel.send(error_msg)

	err_list = ['(  ･᷄ᯅ･᷅ )？','( ；o；)？']
	random.shuffle(err_list)
	await ctx.send(err_list[0])

@bot.event
async def on_ready():
	
	msg = '起動しました。'
	
	alert_channel = bot.get_channel(854002265811451944)
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
	happy_list = ['⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾','⸜(\*ˊᗜˋ*)⸝','٩(ˊᗜˋ*)و♪','(๑\'ᗢ\'๑)ฅ','（´⊙౪⊙）۶ｯｯｯｯｨｨｨｨｲｲｲｲﾖｯｼｬｱｱｱｱｧｧｧｧ!!!!',':v:(\'ω\':v: )三:v:(\'ω\'):v:三( :v:\'ω\'):v:','(っ’ヮ’c)','(´-ᴗ-⸝⸝ก)']
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

@bot.command()
async def prime(ctx, *args):
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
		await ctx.send(f'{ctx.author}のギャグは{per}%！:clap:')
	elif per >= 50:
		await ctx.send(f'{ctx.author}のギャグは{per}%です！')
	elif per <= 3:
		await ctx.send(f'{ctx.author}のギャグは{per}%です…あーあ')
	elif per <= 10:
		await ctx.send(f'{ctx.author}のギャグは{per}%です…')
	else:
		await ctx.send(f'{ctx.author}のギャグは{per}%です')

@bot.command()
async def gb(ctx,*args):
	gap_list = [27,81,136,193,251,311,374,400]
	err_flg = False
	player_num = len(args)
	players = []
	gaps = [0,0,0,0]
	temp = 0
	message = ''

	if len(args) == 0:
		await ctx.send('正しい数字を入れてください')
	elif len(args) > 4:
		await ctx.send('パラメータが多すぎます')
	else:
		for i in range(player_num):
			if not (args[i].isdecimal()):
				err_flg = True
		if err_flg:
			await ctx.send('正しい数字を入れてください')
		else:
			for i in range(player_num):
				players.append(int(args[i]))

			for i in range(player_num):
				gaps[i] = 0
				for j in range(player_num):
					if players[i] > players[j]:
						temp = players[i] - players[j]
						for k in range(8):
							if temp <= gap_list[k]:
								break
							gaps[i] -= 1
					elif players[i] < players[j]:
						temp = players[j] - players[i]
						for k in range(8):
							if temp <= gap_list[k]:
								break
							gaps[i] += 1

				if not i == 0:
					message += "\n"
				message += str(gaps[i])
			await ctx.send(message)

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
async def god(ctx):
	flag = True
	normal_cnt = 0
	while flag:
		v = random.randint(0,8191)
		normal_cnt += 1
		if v == 8191:
			flag = False
	await ctx.send(f'[{ctx.author}] {normal_cnt}回転で当選しました。')


@bot.command()
async def symphogear(ctx):
	flag = True
	normal_cnt = 0
	while flag:
		v = random.randint(0,19979)
		normal_cnt += 1
		if v > 19879:
			flag = False
			
	in_money = math.ceil(normal_cnt / 10.5) * 500
	rest = math.ceil(((0 - (normal_cnt * 2)) % 21) * 125 / 21)
	await ctx.send(f'[{ctx.author}] {normal_cnt}回転で当選しました。')

	pl = f'[{ctx.author}] '
	judge = f'[{ctx.author}] '
	
	if v == 19980:
		cnt = [0,0,0,0,1]
		await ctx.send(f'[{ctx.author}] 全回転:tada:')
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
		judge = f'[{ctx.author}] '
		
	if cnt[0] == 5:
		await ctx.send(f'最終決戦終了\n投資:{in_money}円\n回収:{1480 + rest * 4}円\n収支:{1480 + rest * 4 - in_money}円')

		diff = 1480 + rest * 4 - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')
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
				judge = f'[{ctx.author}] '
				cnt[0] = 0
				cnt[4] += 1
			else:
				judge += f'({r_ch})'
				await ctx.send(judge)
				judge = f'[{ctx.author}] '
				cnt[0] = 0
				cnt[int(r_ch/4)] += 1
		await ctx.send(f'{judge}\n[{ctx.author}] シンフォギアチャンス　終了\n[{ctx.author}] FEVER×{cnt[1]+cnt[2]+cnt[3]+cnt[4]}\n[{ctx.author}] (4)×{cnt[1]}\n(8)×{cnt[2]}\n(12)×{cnt[3]}\n(15)×{cnt[4]}')
		total = (cnt[1]*370+cnt[2]*740+cnt[3]*1120+cnt[4]*1410+rest)*4
		await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')

		diff = total - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')

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
	await ctx.send(f'[{ctx.author}] {normal_cnt}回転で当選しました。')

	judge = f'[{ctx.author}] '
	
	if v == 65535:
		cnt = [0,0,1,0]
		await ctx.send(f'[{ctx.author}] ロングフリーズ:tada:')
	elif v > 65411:
		cnt = [0,0,1,0]
	else:
		cnt = [0,0,0,0]
		
	if cnt[2] == 0:
		await ctx.send(f'[{ctx.author}] チャレンジ失敗\n投資:{in_money}円\n回収:{2400 + rest * 4}円\n収支:{2400 + rest * 4 - in_money}円')
		
		diff = 2400 + rest * 4 - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')
	else:
		await ctx.send(f'[{ctx.author}] 超源RUSH 突入')
		cnt = [0,1,0,0]
		while(cnt[0] < 4):
			r_ch = right_g()
			if r_ch == 0:
				judge += ':x:'
				cnt[0] += 1
			else:
				judge += f'({r_ch})'
				await ctx.send(judge)
				judge = f'[{ctx.author}] '
				cnt[0] = 0
				cnt[int(r_ch/3)] += 1
		await ctx.send(f'{judge}\n[{ctx.author}] 超源RUSH　終了\n[{ctx.author}] 超源RUSH×{cnt[1]+cnt[2]}\n[{ctx.author}] 超源BONUS×{cnt[3]}')
		total = (cnt[1]*300+cnt[2]*600+cnt[3]*900+rest)*4
		await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')

		diff = total - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')

def right_g2():
	right = random.randint(0,243) # 1/2.44
	if right < 80:
		return 3
	elif right < 100:
		return 9
	else:
		return 0

@bot.command()
async def gen2(ctx):
	flag = True # 通常時フラグ
	normal_cnt = 0
	while flag:
		v = random.randint(0,65535)
		normal_cnt += 1
		if v < 505: # 505個があたり
			flag = False
			
	in_money = math.ceil(normal_cnt / 9) * 500
	rest = math.ceil(((0 - normal_cnt) % 9) / 9 * 125) # 上皿に残ったやつ
	await ctx.send(f'[{ctx.author}] {normal_cnt}回転で当選しました。')

	judge = f'[{ctx.author}] '
	cnt = []
	
	if v < 283: # 突入
		cnt = [0,1,0]
	else: # 非突入
		cnt = [0,0,0]
		
	initial_payout = 210 * 4 # 初当たり出玉 
	if cnt[1] == 0:
		await ctx.send(f'[{ctx.author}] チャレンジ失敗\n[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{initial_payout + rest * 4}円\n[{ctx.author}] 収支:{initial_payout + rest * 4 - in_money}円')
		
		diff = initial_payout + rest * 4 - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')
	else:
		await ctx.send(f'[{ctx.author}] 超源RUSH 突入')
		cnt = [0,1,0,0]
		while(cnt[0] < 4):
			r_ch = right_g2()
			if r_ch == 0:
				judge += ':x:'
				cnt[0] += 1
			elif r_ch == 9:
				judge += f'({9})'
				await ctx.send(judge)
				judge = f'[{ctx.author}] '
				cnt[0] = 0
				cnt[2] += 1
				lt_lot = random.randint(0,9) # 10%引いたら0 LT
				if lt_lot == 0:
					await ctx.send(f'[{ctx.author}] :tada:ラッキートリガー発動:tada:')
					cnt[0] = -120 # 初回は127回回すまで終了しないよう調整
					while(cnt[0] < 6):
						r_ch = right_g2()
						if r_ch == 0:
							judge += ':x:'
							cnt[0] += 1
						else:
							judge += f'({r_ch})'
							await ctx.send(judge)
							judge = f'[{ctx.author}] '
							cnt[0] = 0
							cnt[int((r_ch+3)/6)] += 1
					cnt[0] = 3 # 下位ラッシュのファイナルジャッジと同じ状態にして親ループに戻る
			else:
				judge += f'({3})'
				await ctx.send(judge)
				judge = f'[{ctx.author}] '
				cnt[0] = 0
				cnt[1] += 1
		await ctx.send(f'{judge}\n[{ctx.author}] 超源RUSH　終了\n[{ctx.author}] 超源RUSH×{cnt[1]}\n[{ctx.author}] 超源BONUS×{cnt[2]}')
		total = (cnt[1]*210+cnt[2]*630+rest)*4
		await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')
		
		diff = total - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')

def left_aria():
	right = random.randint(0,99)
	if right < 10:
		return 45
	elif right < 50:
		return 30
	elif right < 55:
		return 15
	else:
		return 0

# 1500回数を返す
def right_aria():
	flag = True
	cnt = 1
	while flag:
		flag = False
		quarter = random.randint(0,3)
		if quarter == 0:
			cnt += 1
			flag = True
	return cnt


@bot.command()
async def aria(ctx):
	flag = True # 通常時フラグ
	normal_cnt = 0
	normal_total = 0
	st_cnt = 0
	charge_cnt = 0
	max_cnt = 1 # 最大獲得数
	cnt1500 = 0
	cnt3000 = 0
	cntover = 0 # 4500以降

	while flag:
		v = random.randint(0,65535)
		normal_cnt += 1
		if v < 164: # 164個があたり
			flag = False
			normal_total += normal_cnt
		elif v < 340: # 176個が緋弾チャージ
			await ctx.send(f'[{ctx.author}] {normal_cnt}G 緋弾チャージ')
			charge_cnt += 1
			normal_total += normal_cnt
			normal_cnt = 0

	in_money = math.ceil(normal_total / 8) * 500
	rest = math.ceil(((0 - normal_total) % 8) / 8 * 125) # 上皿に残ったやつ
	await ctx.send(f'[{ctx.author}] {normal_cnt}Gで当選しました。')

	status = left_aria()
	if status == 0:
		await ctx.send(f'[{ctx.author}] SCARLET BONUS')
		cnt1500 += 1
	elif status == 15:
		await ctx.send(f'[{ctx.author}] HYPER SCARLET BONUS')
		cnt1500 += 1
	elif status == 30:
		await ctx.send(f'[{ctx.author}] HYPER SCARLET GOD BONUS 3000')
		cnt3000 += 1
	elif status == 45:
		await ctx.send(f'[{ctx.author}] HYPER SCARLET GOD BONUS 4500')
		cnt3000 += 1
		cntover += 1

	# チャンスタイム
	if status == 0:
		await ctx.send(f'[{ctx.author}] チャンスタイム　突入')
		flag = True
		while flag:
			st_cnt += 1
			if st_cnt >= 71:
				await ctx.send(f'[{ctx.author}] チャンスタイム　終了')
				await ctx.send(f'[{ctx.author}] TOTAL　{cnt1500*1500 + cnt3000*3000 + cntover*1500}')
				await ctx.send(f'[{ctx.author}] 最大獲得　{max_cnt*1500}')
				await ctx.send(f'[{ctx.author}] 3000×{cnt3000}　1500×{cnt1500}')

				total = (charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest)*4
				await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')
				
				diff = total - in_money
				new_balance, status = save_balance(diff, ctx)
				if status == 200:
					await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
				else:
					status = auto_regist(ctx, ctx.author.global_name)
					if status != 200:
						await ctx.send('残高アカウント登録エラー')
						return 
					new_balance, status = save_balance(diff, ctx)
					if status == 200:
						await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
					else:
						await ctx.send('残高登録エラー')
				return
			
			v = random.randint(0,65535)
			if v < 164: # 164個があたり
				flag = False
				r = right_aria()
				if r == 1:
					cnt1500 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET BONUS')
				elif r == 2:
					cnt3000 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS 3000')
				else:
					cnt3000 += 1
					cntover += r-2
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS {r*1500}')
				
				if max_cnt < r:
					max_cnt = r
				
				
				status = 45
	
	# LBR
	if (status==15) or (status==30):
		await ctx.send(f'[{ctx.author}] LIGHTNING BULLET RUSH　突入')
		flag = True
		while flag:
			st_cnt += 1
			if st_cnt >= 71:
				await ctx.send(f'[{ctx.author}] LIGHTNING BULLET RUSH　終了')
				await ctx.send(f'[{ctx.author}] TOTAL　{cnt1500*1500 + cnt3000*3000 + cntover*1500}')
				await ctx.send(f'[{ctx.author}] 最大獲得　{max_cnt*1500}')
				await ctx.send(f'[{ctx.author}] 3000×{cnt3000}　1500×{cnt1500}')

				total = (charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest)*4
				await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')
				
				diff = total - in_money
				new_balance, status = save_balance(diff, ctx)
				if status == 200:
					await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
				else:
					status = auto_regist(ctx, ctx.author.global_name)
					if status != 200:
						await ctx.send('残高アカウント登録エラー')
						return 
					new_balance, status = save_balance(diff, ctx)
					if status == 200:
						await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
					else:
						await ctx.send('残高登録エラー')
					return

			v = random.randint(0,65535)
			if v < 624: # 624個があたり
				flag = False
				r = right_aria()
				if r == 1:
					cnt1500 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET BONUS')
				elif r == 2:
					cnt3000 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS 3000')
				else:
					cnt3000 += 1
					cntover += r-2
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS {r*1500}')
				
				if max_cnt < r:
					max_cnt = r
				
				status = 45
			
			

	# 超LBR
	if status == 45:
		await ctx.send(f'[{ctx.author}] 超LIGHTNING BULLET RUSH　突入')
		flag = True
		while st_cnt < 167:
			v = random.randint(0,65535)
			st_cnt += 1
			if v < 624: # 624個があたり
				r = right_aria()
				if r == 1:
					cnt1500 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET BONUS')
				elif r == 2:
					cnt3000 += 1
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS 3000')
				else:
					cnt3000 += 1
					cntover += r-2
					await ctx.send(f'[{ctx.author}] {st_cnt}G HYPER SCARLET GOD BONUS {r*1500}')
				
				if max_cnt < r:
					max_cnt = r

				st_cnt = 0
	
		await ctx.send(f'[{ctx.author}] 超LIGHTNING BULLET RUSH　終了')
		await ctx.send(f'[{ctx.author}] TOTAL　{cnt1500*1500 + cnt3000*3000 + cntover*1500}')
		await ctx.send(f'[{ctx.author}] 最大獲得　{max_cnt*1500}')
		await ctx.send(f'[{ctx.author}] 3000×{cnt3000}　1500×{cnt1500}')

		total = (charge_cnt*420 + cnt1500*1400 + cnt3000*2800 + cntover*1400 + rest)*4
		await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')

		diff = total - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')

@bot.command()
async def goyoku(ctx):
	flag = True
	normal_cnt = 0
	cnt1500 = 0
	cntover = 0
	bonus_max = 3000
	while flag:
		v = random.randint(0,65535)
		normal_cnt += 1
		if v < 188:
			flag = False
			
	in_money = math.ceil(normal_cnt / 8.5) * 500
	rest = math.ceil(((0 - (normal_cnt * 2)) % 17) * 125 / 17)
	await ctx.send(f'[{ctx.author}] {normal_cnt}回転で当選しました。')
	
	if v > 104:
		cnt = [0,0,0,1]
	else:
		cnt = [0,0,1,0]
		
	if cnt[2] == 1: # 1500のとき非突入
		await ctx.send(f'[{ctx.author}] 大兎殲滅戦 終了\n[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{6000 + rest * 4}円\n[{ctx.author}] 収支:{6000 + rest * 4 - in_money}円')
		
		diff = 6000 + rest * 4 - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')
	else:
		cnt1500 = 2
		flag = True
		while flag:
			flag = False
			quarter = random.randint(0,3)
			if quarter == 0:
				flag = True
				cnt1500 += 1
				cntover += 1
		await ctx.send(f'[{ctx.author}] 超強欲 {cnt1500 * 1500} BONUS')
		await ctx.send(f'[{ctx.author}] 強欲RUSH 突入')
		while(cnt[0] < 145):
			right = random.randint(0,9999)
			cnt[0] += 1
			if right < 20:
				cnt[1] += 1
				await ctx.send(f'[{ctx.author}] {cnt[0]}G 2R')
			elif right < 75:
				cnt[2] += 1
				await ctx.send(f'[{ctx.author}] {cnt[0]}G Re:ゼロ BONUS')
			elif right < 100:
				cnt[3] += 1
				
				cnt1500 = 2
				flag = True
				while flag:
					flag = False
					quarter = random.randint(0,3)
					if quarter == 0:
						flag = True
						cnt1500 += 1
						cntover += 1
				await ctx.send(f'[{ctx.author}] {cnt[0]}G 超強欲 {cnt1500 * 1500} BONUS')
				if cnt1500 * 1500 > bonus_max:
					bonus_max = cnt1500 * 1500
			else:
				continue

			cnt[0] = 0
		
		await ctx.send(f'[{ctx.author}] 強欲RUSH　終了\n[{ctx.author}] RUSH × {cnt[1]+cnt[2]+cnt[3]}\n[{ctx.author}] 超強欲 3000 BONUS × {cnt[3]}\n[{ctx.author}] 超強欲最高記録 {bonus_max}pt')
		total = (cnt[1]*300+cnt[2]*1500+cnt[3]*3000+cntover*1500)
		await ctx.send(f'[{ctx.author}] TOTAL {total}pt')
		total = (cnt[1]*280+cnt[2]*1400+cnt[3]*2800+cntover*1400+rest)*4
		await ctx.send(f'[{ctx.author}] 投資:{in_money}円\n[{ctx.author}] 回収:{total}円\n[{ctx.author}] 収支:{total - in_money}円')

		diff = total - in_money
		new_balance, status = save_balance(diff, ctx)
		if status == 200:
			await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
		else:
			status = auto_regist(ctx, ctx.author.global_name)
			if status != 200:
				await ctx.send('残高アカウント登録エラー')
				return 
			new_balance, status = save_balance(diff, ctx)
			if status == 200:
				await ctx.send(f'[{ctx.author}] 残高:{new_balance}円') 
			else:
				await ctx.send('残高登録エラー')

def auto_regist(ctx, *args):
	url = "https://okemenlandz.sakura.ne.jp/okemenlandz/public/api/moneys"
	name = ""

	if len(args) == 0:
		name = ctx.author.global_name
	else:
		name = args[0]

	data = {
		"user_id": ctx.author.id,
		"name": name
	}
	res = requests.post(url, data=data)

	return res.status_code

def save_balance(diff, ctx):
	"""
	Parameters
	----------
	diff : int
    	登録する差分(金額)
	ctx : Context

	Returns
	-------
	int
		もともとの残高に差分を加算したもの
	status
		APIのステータスコード
	"""

	url = "https://okemenlandz.sakura.ne.jp/okemenlandz/public/api/moneys/" + str(ctx.author.id)
	res = requests.get(url)
				
	status = res.status_code

	if status == 200:
		res = json.loads(res.text)
		balance = res[0]["balance"]
		data = {
			'balance': balance + diff
		}
		res = requests.post(url, data=data)
		return balance + diff, status
	else:
		return 0, status

@bot.command()
async def jantama(ctx,*args):
	s4t1 = [25,35,55,70,75]
	s4n1 = [35,55,95,125,135]
	s4t2 = [10,15,25,35,35]
	s4n2 = [15,25,45,60,65]
	s3t1 = [30,45,70,90,135]
	s3n1 = [45,75,120,175,255]
	if args[0] == '4':
		if args[1] == 'sh':
			req = 24100 + (int(args[2]) - s4t1[0]) * 1000
			if req < 30000:
				await ctx.send(f'銅東 トップ')
			else:
				await ctx.send(f'銅東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[0]) * 1000
			if req <= 40000:
				await ctx.send(f'銅東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[0]) * 1000
			if req < 30000:
				await ctx.send(f'銅南 トップ')
			else:
				await ctx.send(f'銅南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[0]) * 1000
			if req <= 40000:
				await ctx.send(f'銅南 {req}点2着')
		elif args[1] == 'si':
			req = 24100 + (int(args[2]) - s4t1[0]) * 1000
			if req < 30000:
				await ctx.send(f'銅東 トップ')
			else:
				await ctx.send(f'銅東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[0]) * 1000
			if req <= 40000:
				await ctx.send(f'銅東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[0]) * 1000
			if req < 30000:
				await ctx.send(f'銅南 トップ')
			else:
				await ctx.send(f'銅南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[0]) * 1000
			if req <= 40000:
				await ctx.send(f'銅南 {req}点2着')

			req = 24100 + (int(args[2]) - s4t1[1]) * 1000
			if req < 30000:
				await ctx.send(f'銀東 トップ')
			else:
				await ctx.send(f'銀東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[1]) * 1000
			if req <= 40000:
				await ctx.send(f'銀東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[1]) * 1000
			if req < 30000:
				await ctx.send(f'銀南 トップ')
			else:
				await ctx.send(f'銀南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[1]) * 1000
			if req <= 40000:
				await ctx.send(f'銀南 {req}点2着')
		elif args[1] == 'k':
			req = 24100 + (int(args[2]) - s4t1[1]) * 1000
			if req < 30000:
				await ctx.send(f'銀東 トップ')
			else:
				await ctx.send(f'銀東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[1]) * 1000
			if req <= 40000:
				await ctx.send(f'銀東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[1]) * 1000
			if req < 30000:
				await ctx.send(f'銀南 トップ')
			else:
				await ctx.send(f'銀南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[1]) * 1000
			if req <= 40000:
				await ctx.send(f'銀南 {req}点2着')

			req = 24100 + (int(args[2]) - s4t1[2]) * 1000
			if req < 30000:
				await ctx.send(f'金東 トップ')
			else:
				await ctx.send(f'金東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[2]) * 1000
			if req <= 40000:
				await ctx.send(f'金東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[2]) * 1000
			if req < 30000:
				await ctx.send(f'金南 トップ')
			else:
				await ctx.send(f'金南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[2]) * 1000
			if req <= 40000:
				await ctx.send(f'金南 {req}点2着')
		elif args[1] == 'g':
			req = 24100 + (int(args[2]) - s4t1[2]) * 1000
			if req < 30000:
				await ctx.send(f'金東 トップ')
			else:
				await ctx.send(f'金東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[2]) * 1000
			if req <= 40000:
				await ctx.send(f'金東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[2]) * 1000
			if req < 30000:
				await ctx.send(f'金南 トップ')
			else:
				await ctx.send(f'金南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[2]) * 1000
			if req <= 40000:
				await ctx.send(f'金南 {req}点2着')

			req = 24100 + (int(args[2]) - s4t1[3]) * 1000
			if req < 30000:
				await ctx.send(f'玉東 トップ')
			else:
				await ctx.send(f'玉東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[3]) * 1000
			if req <= 40000:
				await ctx.send(f'玉東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[3]) * 1000
			if req < 30000:
				await ctx.send(f'玉南 トップ')
			else:
				await ctx.send(f'玉南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[3]) * 1000
			if req <= 40000:
				await ctx.send(f'玉南 {req}点2着')
		elif args[1] == 's':
			req = 24100 + (int(args[2]) - s4t1[3]) * 1000
			if req < 30000:
				await ctx.send(f'玉東 トップ')
			else:
				await ctx.send(f'玉東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[3]) * 1000
			if req <= 40000:
				await ctx.send(f'玉東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[3]) * 1000
			if req < 30000:
				await ctx.send(f'玉南 トップ')
			else:
				await ctx.send(f'玉南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[3]) * 1000
			if req <= 40000:
				await ctx.send(f'玉南 {req}点2着')

			req = 24100 + (int(args[2]) - s4t1[4]) * 1000
			if req < 30000:
				await ctx.send(f'王東 トップ')
			else:
				await ctx.send(f'王東 {req}点トップ')
			req = 24100 + (int(args[2]) - s4t2[4]) * 1000
			if req <= 40000:
				await ctx.send(f'王東 {req}点2着')
			req = 24100 + (int(args[2]) - s4n1[4]) * 1000
			if req < 30000:
				await ctx.send(f'王南 トップ')
			else:
				await ctx.send(f'王南 {req}点トップ')
			req = 24100 + (int(args[2]) - s4n2[4]) * 1000
			if req <= 40000:
				await ctx.send(f'王南 {req}点2着')
	elif args[0] == '3':
		if args[1] == 'sh':
			req = 34100 + (int(args[2]) - s3t1[0]) * 1000
			if req < 40000:
				await ctx.send(f'銅東 トップ')
			else:
				await ctx.send(f'銅東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[0]) * 1000
			if req < 40000:
				await ctx.send(f'銅南 トップ')
			else:
				await ctx.send(f'銅南 {req}点トップ')
		elif args[1] == 'si':
			req = 34100 + (int(args[2]) - s3t1[0]) * 1000
			if req < 40000:
				await ctx.send(f'銅東 トップ')
			else:
				await ctx.send(f'銅東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[0]) * 1000
			if req < 40000:
				await ctx.send(f'銅南 トップ')
			else:
				await ctx.send(f'銅南 {req}点トップ')

			req = 34100 + (int(args[2]) - s3t1[1]) * 1000
			if req < 40000:
				await ctx.send(f'銀東 トップ')
			else:
				await ctx.send(f'銀東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[1]) * 1000
			if req < 40000:
				await ctx.send(f'銀南 トップ')
			else:
				await ctx.send(f'銀南 {req}点トップ')
		elif args[1] == 'k':
			req = 34100 + (int(args[2]) - s3t1[1]) * 1000
			if req < 40000:
				await ctx.send(f'銀東 トップ')
			else:
				await ctx.send(f'銀東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[1]) * 1000
			if req < 40000:
				await ctx.send(f'銀南 トップ')
			else:
				await ctx.send(f'銀南 {req}点トップ')

			req = 34100 + (int(args[2]) - s3t1[2]) * 1000
			if req < 40000:
				await ctx.send(f'金東 トップ')
			else:
				await ctx.send(f'金東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[2]) * 1000
			if req < 40000:
				await ctx.send(f'金南 トップ')
			else:
				await ctx.send(f'金南 {req}点トップ')
		elif args[1] == 'g':
			req = 34100 + (int(args[2]) - s3t1[2]) * 1000
			if req < 40000:
				await ctx.send(f'金東 トップ')
			else:
				await ctx.send(f'金東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[2]) * 1000
			if req < 40000:
				await ctx.send(f'金南 トップ')
			else:
				await ctx.send(f'金南 {req}点トップ')

			req = 34100 + (int(args[2]) - s3t1[3]) * 1000
			if req < 40000:
				await ctx.send(f'玉東 トップ')
			else:
				await ctx.send(f'玉東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[3]) * 1000
			if req < 40000:
				await ctx.send(f'玉南 トップ')
			else:
				await ctx.send(f'玉南 {req}点トップ')
		elif args[1] == 's':
			req = 34100 + (int(args[2]) - s3t1[3]) * 1000
			if req < 40000:
				await ctx.send(f'玉東 トップ')
			else:
				await ctx.send(f'玉東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[3]) * 1000
			if req < 40000:
				await ctx.send(f'玉南 トップ')
			else:
				await ctx.send(f'玉南 {req}点トップ')

			req = 34100 + (int(args[2]) - s3t1[4]) * 1000
			if req < 40000:
				await ctx.send(f'王東 トップ')
			else:
				await ctx.send(f'王東 {req}点トップ')
			req = 34100 + (int(args[2]) - s3n1[4]) * 1000
			if req < 40000:
				await ctx.send(f'王南 トップ')
			else:
				await ctx.send(f'王南 {req}点トップ')

@bot.command()
async def hanabi(ctx,*args):
	game_cnt = int(args[0])
	bita = float(args[1])
	rate = int(args[2])

	wari = (bita - 75) / 25 * 2
	val = math.floor( (wari / 100 * game_cnt * 3) / rate * 1000)
	await ctx.send(f'機械割：{100 + round(wari, 2)}% 期待値：{val}円')

@bot.command()
async def disc(ctx,*args):
	game_cnt = int(args[0])
	bita = float(args[1])
	rate = int(args[2])

	wari = (bita - 58) / 42 * 3
	val = math.floor( (wari / 100 * game_cnt * 3) / rate * 1000)
	await ctx.send(f'機械割：{100 + round(wari, 2)}% 期待値：{val}円')

@bot.command()
async def nori(ctx,*args):
	
	# 子カウントと合計出す
	total = 0
	c = 0
	p_list = []
	for i in range(0,len(args),3):
		total += int(args[i+1])
		if int(args[i+2]) != 0: # 子の時
			c += 1
			total -= int(args[i+2])
		else: # 親の時
			p_list.append(i)
	
	p = len(p_list)

	# 1人当たり
	per = math.floor(total / p)
	amari = total - (per * p)
	if amari == 0:
		toku_list = []
	else:
		toku_list = random.sample(p_list, amari)

	# 人数分ループ
	outputstr = "```"
	for i in range(0,len(args),3):
		if int(args[i+2]) != 0: # 子の時
			outputstr += f'{args[i].ljust(5,"　")} {args[i+1].rjust(4)} {args[i+2].rjust(4)} {str(int(args[i+2]) - int(args[i+1])).rjust(4)}\n'
		else: # 親の時
			if i in toku_list:
				outputstr += f'{args[i].ljust(5,"　")} {args[i+1].rjust(4)} {str(per + 1).rjust(4)} {str(per - int(args[i+1]) + 1).rjust(4)}\n'
			else:
				outputstr += f'{args[i].ljust(5,"　")} {args[i+1].rjust(4)} {str(per).rjust(4)} {str(per - int(args[i+1])).rjust(4)}\n'

	await ctx.send(outputstr + "```")

@bot.command()
async def dice(ctx, *args):
    if len(args) != 1:
        # エラー処理
        return
    count = [0,0,0,0,0,0]
    emoji = [":one: ",":two: ",":three: ",":four: ",":five: ",":six: "]
    txt = ""

    for i in range(int(args[0])):
        r = random.randint(0, 5)
        txt += emoji[r]
        count[r] += 1

    # 出力
    await ctx.send(txt)
    await ctx.send(f'{count[0]}-{count[1]}-{count[2]}-{count[3]}-{count[4]}-{count[5]}\n合計: {count[0]+count[1]*2+count[2]*3+count[3]*4+count[4]*5+count[5]*6}')

@bot.command()
async def gochi(ctx, *args):
    player_num = len(args) - 1
    last = int(args[0])
	
    # player.nameのみのlist作成
    l = []
    for i in range(1, len(args)):
        l.append(args[i])
	
    # 混ぜる
    r = random.sample(l, len(args)-1)
	
    i = 0
    gochi = 0
    for name in r:
        i += 1
        if i == player_num:
            break # 最後の1人は残り

        keta = len(str(last))
        unit = pow(10, keta-1)
        maxi = last - (last % unit)

        if random.randint(1, 5) < 3:
            gochi = maxi
        else:
            gochi = random.randint(0, int(maxi / unit)) * unit

        last -= gochi
        await ctx.send(f'{name}: {gochi}')
    
    name = r[player_num - 1]
    await ctx.send(f'{name}: {last}')

@bot.command()
async def heiten(ctx, args):
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    last = int(args[0])
    last_seconds = (((last - (last % 100)) / 100) - hour) * 3600 + (last % 100 - minute) * 60 + second
    await ctx.send(f'残り{last_seconds // 4.1}回転')

@bot.command()
async def judge(a):
    rank = 0
    f = 0
    pairList = [0,0,0,0,0]
    flash = False
    straight = False
    four = False
    three = False
    pair = False
    nopair = False
    min = 14
    max = 0
    for i in range(5):
        if a[i][1] == a[4][1]:
            f += 1
        for j in range(5):
            if a[i][0] == a[j][0]:
                pairList[i] += 1
        if min > a[i][0]:
            min = a[i][0]
        if max < a[i][0]:
            max = a[i][0]
	
    nopairCnt = 0
    pairCnt = 0
    for i in range(5):
        if pairList[i] == 1:
            nopairCnt += 1
        elif pairList[i] == 2:
            pair = True
            pairCnt += 1
        elif pairList[i] == 3:
            three = True
        elif pairList[i] == 4:
            four = True

    if nopairCnt == 5:
        nopair = True

    if nopair:
        if min == max - 4:
            straight = True
        if min == 1:
            straightCnt = 0
            for i in range(10,14):
                for j in range(5):
                    if a[j][0] == i:
                        straightCnt += 1
            if straightCnt == 4:
                straight = True

    if f == 5:
        flash = True

    if flash & straight:
        rank = 8
    elif four:
        rank = 7
    elif three & pair:
        rank = 6
    elif flash:
        rank = 5
    elif straight:
        rank = 4
    elif three:
        rank = 3
    elif pairCnt == 4:
        rank = 2
    elif pair:
        rank = 1
    else:
        rank = 0

    return rank

def rate(ctx, *args):
    return

def binomial_pmf(k, n, p):
    """二項分布の確率質量関数 P(X=k | n, p)"""
    if p < 0 or p > 1 or k > n:
        return 0
    comb = math.comb(n, k)
    return comb * (p ** k) * ((1 - p) ** (n - k))

import json
import math
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

def binomial_pmf(k, n, p):
    """二項分布の確率質量関数"""
    if p < 0 or p > 1 or k > n:
        return 0
    comb = math.comb(n, k)
    return comb * (p ** k) * ((1 - p) ** (n - k))

@bot.command()
async def hanbetsu(ctx, *, json_text: str):
    """
    JSON形式の9×n二次元配列を受け取り、各設定(1〜6)における尤度を計算する。

    各行は:
    [タイトル, 設定1確率, ..., 設定6確率, 起こった回数, 試行回数]
    """
    try:
        matrix = json.loads(json_text)

        if not all(isinstance(row, list) and len(row) == 9 for row in matrix):
            await ctx.send("各行は9要素（タイトル＋設定1〜6＋発生回数＋試行回数）である必要があります。")
            return

        total_likelihoods = [1.0 for _ in range(6)]  # 各設定の累積尤度
        results = []

        for row in matrix:
            title = str(row[0])
            theoretical = row[1:7]
            k = int(row[7])
            n = int(row[8])

            if n <= 0:
                await ctx.send(f"{title}: 試行回数が0以下です。")
                continue

            # 各設定の尤度
            likelihoods = [binomial_pmf(k, n, p) for p in theoretical]
            total = sum(likelihoods)
            normalized = [l / total if total > 0 else 0 for l in likelihoods]

            # 累積尤度
            for i in range(6):
                total_likelihoods[i] *= likelihoods[i]

            results.append({
                "title": title,
                "probabilities": normalized
            })

        # 総合結果
        total_sum = sum(total_likelihoods)
        total_probs = [l / total_sum for l in total_likelihoods] if total_sum > 0 else [0] * 6

        # 出力整形
        msg = "```\n"
        for r in results:
            msg += f"{r['title']}\n"
            for i, p in enumerate(r["probabilities"], 1):
                bar_len = int((p * 100) / 5)
                bar = "█" * bar_len
                percent_str = f"{p*100:.2f}%"
                int_part = int(p*100)
                if int_part < 10:
                    percent_str = " " + percent_str
                msg += f"設定{i}: {percent_str} {bar}\n"
            msg += "\n"

        msg += "――――――――――――――――――\n"
        msg += "【総合判定（全データを統合）】\n"
        for i, p in enumerate(total_probs, 1):
            bar_len = int((p * 100) / 5)
            bar = "█" * bar_len
            percent_str = f"{p*100:.2f}%"
            int_part = int(p*100)
            if int_part < 10:
                percent_str = " " + percent_str
            msg += f"設定{i}: {percent_str} {bar}\n"
        msg += "```"

        await ctx.send(msg)

    except json.JSONDecodeError:
        await ctx.send("JSON形式が正しくありません。[[...],[...]] の形式で送ってください。")

    """
    JSON形式の8×n二次元配列を受け取り、
    各設定(1〜6)における「観測結果が起こる確率（尤度）」を計算する。

    各行は:
    [設定1確率, ..., 設定6確率, 起こった回数, 試行回数]

    例:
    !hanbetsu [[0.1,0.2,0.3,0.15,0.15,0.1,12,100],
               [0.05,0.1,0.2,0.3,0.25,0.1,18,100]]
    """
    try:
        matrix = json.loads(json_text)

        if not all(isinstance(row, list) and len(row) == 8 for row in matrix):
            await ctx.send("各行は8要素（設定1〜6＋発生回数＋試行回数）である必要があります。")
            return

        # 各設定の総合尤度（掛け合わせ）
        total_likelihoods = [1.0 for _ in range(6)]

        msg = ""

        for row_index, row in enumerate(matrix):
            theoretical = row[:6]
            k = int(row[6])
            n = int(row[7])

            if n <= 0:
                await ctx.send(f"{row_index+1}行目: 試行回数が0以下です。")
                continue

            observed_p = k / n

            # 各設定の尤度を計算
            likelihoods = [binomial_pmf(k, n, p) for p in theoretical]

            # 正規化（確率としての比率表示）
            total = sum(likelihoods)
            normalized = [l / total if total > 0 else 0 for l in likelihoods]

            # 総合尤度を掛け合わせて累積（多データ統合）
            for i in range(6):
                total_likelihoods[i] *= likelihoods[i]

            msg += f"第{row_index+1}行: 実測 {k}/{n} (={observed_p:.3f})\n"
            for i, l in enumerate(normalized, 1):
                msg += f"設定{i}: {l*100:.2f}% "
            msg += f"\n→ 最も尤もらしい設定: {normalized.index(max(normalized)) + 1}\n\n"

        # 総合結果
        total_sum = sum(total_likelihoods)
        if total_sum > 0:
            total_probs = [l / total_sum for l in total_likelihoods]
        else:
            total_probs = [0] * 6

        msg += "――――――――――――――――――\n"
        msg += "【総合判定（全データを統合）】\n"
        for i, p in enumerate(total_probs, 1):
            msg += f"設定{i}: {p*100:.4f}% "
        msg += f"\n→ 総合的に最も可能性が高い設定: {total_probs.index(max(total_probs)) + 1}"

        await ctx.send(msg)

    except json.JSONDecodeError:
        await ctx.send("JSONの形式が正しくありません。[[...],[...]] の形式で送ってください。")


"""
@bot.command()
async def mahjong(ctx, *args):
    if len(args) % 5 != 0:
        await ctx.send("リストの長さは5の倍数である必要があります。")
        return
	
    guild = ctx.guild.id
    
    n = len(args) // 5
    result = [args[i*5:(i+1)*5] for i in range(n)]
    return
"""

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)