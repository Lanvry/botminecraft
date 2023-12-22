from discord.ext import commands
from myserver import server_on

TOKEN = "MTAyMTM4Mjc0MjcwNzAxOTgzNg.GFZYTS.gckLy51rY3UPyWuw-r4TCTVh5FANPbjgJvsiqQ" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(TOKEN)