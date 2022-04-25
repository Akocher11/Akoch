import discord
from discord.ext import commands
class Otletsay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Otlet : ✅')
        print('Say : ✅')

    @commands.command()
    async def otlet(self, ctx, *, saymsg=None):
        if saymsg == None:
            return await ctx.send("Írj valami ötletet a ?otlet után és úgy jó lesz!")
        await ctx.message.delete()
        sayEmbed = discord.Embed(title=f"{ctx.author.name} ötlete :", color=discord.Color.blue(),
                                 description=f"{saymsg}")
        sayEmbed.timestamp = ctx.message.created_at

        Embed = await ctx.send(embed=sayEmbed)
        await Embed.add_reaction(emoji="✅")
        await Embed.add_reaction(emoji="❌")

    @commands.command()
    @commands.has_role('►│🔧 Bot+')
    async def say(self, ctx, *, saymsg=None):
        if saymsg == None:
            return await ctx.send("Írj valami szöveget a ?say után és úgy jó lesz!")
        await ctx.message.delete()
        sayEmbed = discord.Embed(title=f"{ctx.author.name} Mondta :", color=discord.Color.red(),
                                 description=f"{saymsg}")
        sayEmbed.timestamp = ctx.message.created_at

        await ctx.send(embed=sayEmbed)

def setup(bot):
    bot.add_cog(Otletsay(bot))