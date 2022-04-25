import discord
from discord.ext import commands

class Lock(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lock : ✅')

    @commands.command()
    @commands.has_role('►│🔧 Bot+')
    async def lock(self, ctx):
        channel = ctx.channel
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

        embed = discord.Embed(title=f"🔒 Locked by {ctx.author.name}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Lock(bot))