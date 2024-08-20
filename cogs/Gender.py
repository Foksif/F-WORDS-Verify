import disnake
from disnake.ext import commands

class Settings:
    Male = 00000000000
    Female = 00000000000
    NoneGender = 00000000000

class ButtonView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Муж", style=disnake.ButtonStyle.primary, custom_id="button1")
    async def button1(self, button: disnake.ui.Button, interaction: disnake.Interaction):

        roleM = interaction.guild.get_role(Settings().Male)
        roleG = interaction.guild.get_role(Settings().Female)
        roleN = interaction.guild.get_role(Settings().NoneGender)

        if not interaction.user.get_role(Settings().Male):
            if not interaction.user.get_role(Settings().Female):
                if not interaction.user.get_role(Settings().NoneGender):
                    await interaction.author.add_roles(roleM)
                    embed = disnake.Embed(title="Вам был выдан мужской пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    await interaction.author.remove_roles(roleN)
                    await interaction.author.add_roles(roleM)
                    embed = disnake.Embed(title="Вам был выдан мужской пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                if not interaction.user.get_role(Settings().NoneGender):
                    await interaction.author.remove_roles(roleG)
                    await interaction.author.add_roles(roleM)
                    embed = disnake.Embed(title="Вам был выдан мужской пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    await interaction.author.remove_roles(roleN)
                    await interaction.author.remove_roles(roleG)
                    await interaction.author.add_roles(roleM)
                    embed = disnake.Embed(title="Вам был выдан мужской пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(title="У вас уже установлен мужской пол.", color=0xFFB02E)
            await interaction.response.send_message(embed=embed, ephemeral=True)


    @disnake.ui.button(label="Жен", style=disnake.ButtonStyle.danger, custom_id="button2")
    async def button2(self, button: disnake.ui.Button, interaction: disnake.Interaction):

        roleM = interaction.guild.get_role(Settings().Male)
        roleG = interaction.guild.get_role(Settings().Female)
        roleN = interaction.guild.get_role(Settings().NoneGender)

        if not interaction.user.get_role(Settings().Female):
            if not interaction.user.get_role(Settings().Male):
                if not interaction.user.get_role(Settings().NoneGender):
                    await interaction.author.add_roles(roleG)
                    embed = disnake.Embed(title="Вам был выдан женский пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    await interaction.author.remove_roles(roleN)
                    await interaction.author.add_roles(roleG)
                    embed = disnake.Embed(title="Вам был выдан женский пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
            else:
                if not interaction.user.get_role(Settings().NoneGender):
                    await interaction.author.remove_roles(roleM)
                    await interaction.author.add_roles(roleG)
                    embed = disnake.Embed(title="Вам был выдан женский пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
                else:
                    await (interaction.author.remove_roles(roleN))
                    await (interaction.author.remove_roles(roleM))
                    await interaction.author.add_roles(roleG)
                    embed = disnake.Embed(title="Вам был выдан женский пол.", color=0xFFB02E)
                    await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed(title="У вас уже установлен женский пол.", color=0xFFB02E)
            await interaction.response.send_message(embed=embed, ephemeral=True)

class ButtonsRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.slash_command()
    async def gender(self, interaction):
        view = ButtonView()
        embed = disnake.Embed(title="Выбор пола", description="Выбери пол нажатием на кнопки ниже.", color=0xFFB02E)


        await interaction.response.send_message(embed=embed, ephemeral=True, view=view)


def setup(bot):
    bot.add_cog(ButtonsRole(bot))
