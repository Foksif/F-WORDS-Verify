import disnake
from disnake.ext import commands

class VerifyModal(disnake.ui.Modal):
    def __init__(self, code):
        self.code = code

        components = [
            disnake.ui.TextInput(label="Введите код", placeholder=str(self.code), custom_id="code")
        ]

        super().__init__(title="Верификация", components=components, custom_id="verify_modal")

    async def callback(self, interaction: disnake.ModalInteraction) -> None:
        if self.code == int(interaction.text_values["code"]):
            role = interaction.guild.get_role(<Role>)
            noneGender = interaction.guild.get_role(<Role>)

            await interaction.author.remove_roles(role)
            await interaction.author.add_roles(noneGender)

            embed = disnake.Embed(title="Верефикация пройдена!", description="Введите команду: **```/gender```** В чат: <#> что-бы изменить пол.", color=0xFFB02E)

            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("Неверный код!", ephemeral=True)


class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Верификация", style=disnake.ButtonStyle.grey, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        import random
        code = random.randint(1000, 9999)
        await interaction.response.send_modal(VerifyModal(code))

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.command()
    async def verify(self, ctx):
        embed = disnake.Embed(color=0xFFB02E)
        embed.set_image(url='Baner url')
        await ctx.send(embed=embed, view=ButtonView())

    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        self.bot.add_view(view=ButtonView(), message_id=...)

def setup(bot):
    bot.add_cog(Verify(bot))
