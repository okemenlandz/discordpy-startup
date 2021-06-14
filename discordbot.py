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
version = 'ver 7.0 期待値'

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
    

        
           
bot.run(token)
