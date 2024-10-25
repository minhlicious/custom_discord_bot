import discord
from discord.ext import commands
from models import UserBirthday
from config import GetConfig

config = GetConfig()

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)


@bot.command(
    name="birthday",
    description="Enter your birthday in YYYY/MM/DD to register!",
)
async def birthday(ctx, arg):

    print(f"bday woohoo {arg}")
    await ctx.channel.send_message("Thanks!")
    pass


@bot.command()
async def removebirthday(ctx, arg):
    print(f"no bday")
    pass


bot_token = config["discord"]["token"]
bot.run(token=bot_token)
