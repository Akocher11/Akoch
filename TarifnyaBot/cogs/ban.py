import discord
from discord.ext import commands

class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Ban : ✅')

    @commands.command()  # bannol egy embert
    @commands.has_role('►│🔧 Bot+')
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if member == None:
            await ctx.send("Írj embert indokkal együtt. ?ban @ember csúnyán beszélt")
        elif reason == None:
            await ctx.send("Írj indokot is. ?ban @ember csúnyán beszélt")
        else:
            await member.ban(reason=reason)
            await ctx.send(f'{ctx.author.mention} kibannolta {member.mention}-t')


def setup(bot):
    bot.add_cog(Ban(bot))