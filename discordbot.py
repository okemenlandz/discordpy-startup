import discord
from discord.ext import commands
from discord.ext import tasks
from datetime import datetime 
import os
import re
import random
import traceback
import math
import packages.mysql.connector as mydb

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN'] #heroku
version = 'ver 8.0'

bot.run(token)
