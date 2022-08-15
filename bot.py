import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import reader

load_dotenv()

intents = discord.Intents.default()
# intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def duut(ctx, arg):
    if arg:
        result = reader.read(f"./images/{arg}")
    else:
        result = reader.read("./test.png")

    await ctx.send('\n'.join(result))

@bot.command()
async def duutxl(ctx, arg):
    if arg:
        result = reader.read(f"./images/{arg}")
    else:
        result = reader.read("./test.png")

    for str in result:
        await ctx.send(str)

bot.run(os.getenv('TOKEN'))
