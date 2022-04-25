import discord
from discord.ext import commands
class Nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Nuke : ✅')

    @commands.command()  # törli a szobának az üzenet előzményeit
    @commands.has_role('►│🔧 Bot+')
    async def nuke(self, cty, *, amount=10000):
        await cty.channel.purge(limit=amount)
        embed = discord.Embed(title='', Color=0xff087f)
        embed.add_field(name=f'Nuked by {cty.author.name}#{cty.author.discriminator}',
                        value='ennek a szobának az üzenetei törölve!')
        await cty.channel.send(content=None, embed=embed)

def setup(bot):
    bot.add_cog(Nuke(bot))