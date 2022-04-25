import discord
from discord.ext import commands
class Unmute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Unmute : ✅\n\n--------------------------------------------\n')

    @commands.command()
    @commands.has_role('►│🔧 Bot+')
    async def unmute(self, ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name='Muted')
        tagRole = discord.utils.get(ctx.guild.roles, name='►│👤 Tag')

        await member.remove_roles(mutedRole)
        await member.add_roles(tagRole)
        await ctx.send(f'Unmuted {member.mention}')
        await member.send('Unmuteolva lettél Tarifnya szerverén Irány chatelni')


def setup(bot):
    bot.add_cog(Unmute(bot))