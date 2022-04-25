import discord
from discord.ext import commands
class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Mute : ✅')

    @commands.command()
    @commands.has_role('►│🔧 Bot+')
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name='Muted')
        tagRole = discord.utils.get(ctx.guild.roles, name='►│👤 Tag')

        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=False,
                                              read_messages=False)

            await member.add_roles(mutedRole, reason=reason)
            await member.remove_roles(tagRole)
            await ctx.send(f'Muted {member.mention} azért mert {reason}')
            await member.send(f'Le lettél némítva Tarifnya szerverén mert {reason}')
        else:
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=True)
            await member.add_roles(mutedRole, reason=reason)
            await ctx.send(f'Muted {member.mention} azért mert {reason}')
            await member.send(f'Le lettél némítva a Tarifnya szerverén mert {reason}')


def setup(bot):
    bot.add_cog(Mute(bot))
