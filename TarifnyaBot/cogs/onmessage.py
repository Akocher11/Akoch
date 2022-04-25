import discord
from discord.ext import commands
class Onmessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print("Onmessage : ✅")

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if "hello" in ctx.content.lower():
            await ctx.reply(f"Szia {ctx.author.mention}! Hogy telt a napod?")

        if "jól" in ctx.content.lower():
            await ctx.reply(f"Az király.")



def setup(bot):
    bot.add_cog(Onmessage(bot))
