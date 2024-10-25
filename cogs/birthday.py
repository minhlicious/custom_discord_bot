from discord.ext import commands
import discord


class BirthdayReminders(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="birthday",
    )
    async def BirthdayAddUpdate(self, ctx, *, member: discord.Member = None):
        pass
