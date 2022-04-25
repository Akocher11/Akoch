import discord
from discord.ext import commands

class Unlock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Unlock : ✅')

    @commands.command()
    @commands.has_role('►│🔧 Bot+')
    async def unlock(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title=f"🔓 Unlocked by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Unlock(bot))