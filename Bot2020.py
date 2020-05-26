import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from discord.ext.commands import Bot

URL = 'https://news.google.com/topics/CAAqBwgKMIXDmAswuMmwAw?hl=ru&gl=RU&ceid=RU%3Aru'
HEADERS={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'accept': '*/*'} 
TOKEN='NzAyMDkyODQyODE3OTQ1Njkw.Xp7BNQ.cObzDjzVJgQVfZsEiIchVBSgd4g'
Bot = commands.Bot(command_prefix= '!')
Bot.remove_command('help')


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('h3', class_='ipQwMb ekueJc gEATFF RD0gLb')
    x=0
    last_news=[]
    for item in items:
        x+=1
        if x<=4:
            last_news.append({
            'news': item.find('a', class_='DY5T1d').get_text()
                      })
        else:
           break
    return last_news
    
        
    

def parse():
    html = get_html(URL)
    if html.status_code==200:
        get_content(html.text)

@Bot.event
async def on_ready():
    print("bot is online")

@Bot.command(pass_context=True)  
async def help(ctx):
    await ctx.send("Список команд:")
    await ctx.send("!play - пингует пользователей которые смогут пойти с вами играть в выбранные игры. Игры выбираются подкомандами (сокращенное название игр r6 или R6 означает Rainbow Six: Siege, и т.д.)")
    await ctx.send("!info - последние новости, обновляются при вызове команды")


@Bot.command(pass_context=True)  
async def hello(ctx):
   
    await ctx.send(f"Здорово пидоры <@here>")
    

@Bot.command(pass_context=True)  
async def play(ctx, arg=None):
    await ctx.send(format(ctx.message.author))
    if arg=='r6' or arg=='R6':  
        await ctx.send("Зовёт играть в Rainbow Six: Siege <@411072243565592576> <@360698875574616065> <@286827348983283712> <@419195935676170240> <@360003712300613632>")
    elif arg=='apex' or arg=='арех' or arg=='Apex' or arg=='Арех':
        await ctx.send("Зовёт играть в Apex Legends <@411072243565592576> <@286827348983283712> <@419195935676170240> <@360003712300613632>")
    elif arg=='cs' or arg=='кс' or arg=='Cs' or arg=='Кс' or arg=='CS' or arg=='КС':
        await ctx.send("Зовёт играть в Counter-Strike: Global Offensive, малоли сколько у нас отчаянных <@here>")
    elif arg=='циву' or arg=="цивку" or arg=='Циву' or arg=="Цивку":
        await ctx.send("Зовёт играть в Sid Meier’s Civilization VI или Sid Meier’s Civilization V <@411072243565592576> <@286827348983283712> <@419195935676170240> <@360698875574616065>")
    elif arg=='wow' or arg=='вов':
        await ctx.send("Зовёт играть в World of Warcraft <@411072243565592576> <@360698875574616065> <@360003712300613632>")
    elif arg==None:
        await ctx.send("Зовёт почилить <@here>")

@Bot.command(pass_context=True)
async def info(ctx):
    html = requests.get(URL)
    if html.status_code==200:
        print(html)
        mes=get_content(html.text)
        await ctx.send(mes)
    

Bot.run(TOKEN)
