import discord
from discord.ext import commands
class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kick : ✅')

    @commands.command()  # kickel egy embert
    @commands.has_role('►│🔧 Bot+')
    async def kick(self, cty, member: discord.Member, *, reason=None):
        if member == None:
            await cty.send("Írj embert indokkal együtt. ?kick @ember spamelt")
        elif reason == None:
            await cty.send("Írj indokot is. ?kick @ember spamelt")
        else:
            await member.kick(reason=reason)
            await cty.send(f'Kicked {member.mention}')


def setup(bot):
    bot.add_cog(Kick(bot))