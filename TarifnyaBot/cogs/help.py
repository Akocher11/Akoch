import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_ready(self):
        print('Help : ✅')

    @commands.group(invoke_without_command=True)
    @commands.has_role('►│🔧 Bot+')
    async def mhelp(self, ctx):
        em = discord.Embed(title='Help',
                           description="Használd a ?help <parancs>-ot hogy tudd meg hogyan kell használni")

        em.add_field(name="__Ember moderáció__", value="kick\nban\nunban\nmute\nunmute")
        em.add_field(name="__Chat moderáció__", value="lock\nunlock\nnuke\nabw\nrbw")
        em.add_field(name="__Chat__", value="otlet\nsay")
        em.add_field(name="__Fun__", value="tictactoe\n(place)\nrandomg")
        em.add_field(name="__Button__", value="lc")
        em.add_field(name="__+__", value="gstart")

        await ctx.send(embed=em)

    @mhelp.command()
    async def kick(self,ctx):
        em = discord.Embed(title="__Kick__", description="Ki rúgja a meg pingelt embert")
        em.add_field(name="**Használata**", value="?kick @ember <indok>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def ban(self,ctx):
        em = discord.Embed(title="__Ban__", description="Ki bannolja a meg pingelt embert")
        em.add_field(name="**Használata**", value="?ban @ember <indok>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def unban(self,ctx):
        em = discord.Embed(title="__Unban__", description="Unbannolja az adott embert")
        em.add_field(name="**Használata**", value="?unban Akocher11#7376")

        await ctx.send(embed=em)

    @mhelp.command()
    async def mute(self,ctx):
        em = discord.Embed(title="__Mute__", description="Mute-olja a meg pingelt embert")
        em.add_field(name="**Használata**", value="?mute @ember <indok>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def unmute(self,ctx):
        em = discord.Embed(title="__Unmute__", description="Unmute-olja a meg pingelt embert")
        em.add_field(name="**Használata**", value="?unmute @ember")

        await ctx.send(embed=em)

    @mhelp.command()
    async def lock(self,ctx):
        em = discord.Embed(title="__Lock__", description="Lezárja azt a csatornát amelyikbe beírtad a lockot")
        em.add_field(name="**Használata**", value="?lock")

        await ctx.send(embed=em)

    @mhelp.command()
    async def unlock(self,ctx):
        em = discord.Embed(title="__Unlock__",
                           description="Lezárásból feloldja azt a csatornát amelyikbe beírtad az unlockot")
        em.add_field(name="**Használata**", value="?unlock")

        await ctx.send(embed=em)

    @mhelp.command()
    async def nuke(self,ctx):
        em = discord.Embed(title="__Nuke__",
                           description="Törli az üzenet előzményeket(Ha nem írsz be számot akkor az összeset"
                                       "törli)")
        em.add_field(name="**Használata**", value="?nuke <szám>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def abw(self,ctx):
        em = discord.Embed(title="__abw__",
                           description="(AddBannedWord), ha valaki beírja a tiltott szót akkor automatikusan törli")
        em.add_field(name="**Használata**", value="?abw <tiltó szó>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def rbw(self,ctx):
        em = discord.Embed(title="__rbw__", description="(RemoveBannedWord), törli a tiltó listáról a szót")
        em.add_field(name="**Használata**", value="?rbw <tiltott szó>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def otlet(self,ctx):
        em = discord.Embed(title="__Otlet__", description="ki írsz vele egy ötletet")
        em.add_field(name="**Használata**", value="?otlet <ötleted>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def say(self,ctx):
        em = discord.Embed(title="__Say__", description="ki íratod a bottal a amit szeretnél mondani")
        em.add_field(name="**Használata**", value="?say <Mondani valód>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def tictactoe(self,ctx):
        em = discord.Embed(title="__TicTacToe__", description="3x3-as Amőba Fun game")
        em.add_field(name="**Használata**", value="?tictactoe <@Játékos> <@Játékos2>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def place(self,ctx):
        em = discord.Embed(title="__TicTacToe__", description="Ha elindult egy tictactoe játék ezzel tudsz helyezni.")
        em.add_field(name="**Használata**", value="?place <szám>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def gstart(self,ctx):
        em = discord.Embed(title="__Giveaway__", description="indít egy giveawayt")
        em.add_field(name="**Használata**", value="?gstart (a továbbiakat ki írja)")

        await ctx.send(embed=em)

    @mhelp.command()
    async def randomg(self, ctx):
        em = discord.Embed(title="__Giveaway__", description="Generál két szám között egy random számot")
        em.add_field(name="**Használata**", value="?randomg <szám1> <szám2>")

        await ctx.send(embed=em)

    @mhelp.command()
    async def lc(self,ctx):
        em = discord.Embed(title="__LinkCreate__", description="Csinál egy gombot")
        em.add_field(name="**Használata**", value="?linkcreate <link ahova dobjon ha rányomsz> <gomb tartalma>")

        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Help(bot))