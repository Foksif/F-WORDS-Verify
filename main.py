# MIT License
#
# Copyright (c) 2024 Foks_f
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import disnake
from disnake.ext import commands, tasks

import os

intents = disnake.Intents.all()



activities = [
    disnake.Activity(type=disnake.ActivityType.watching, name="By Foks_f"),
    disnake.Activity(type=disnake.ActivityType.watching, name="Version 0.2 [Beta]")
]

bot = commands.Bot(command_prefix="!", intents=intents, test_guilds=[1157195772115292252])

@bot.event
async def on_ready():
    change_status.start()
    print(f'{bot.user} is ready!')

for file in os.listdir("./cogs"):
  if file.endswith(".py"):
    bot.load_extension(f"cogs.{file[:-3]}")

@tasks.loop(seconds=30)
async def change_status():
    if bot.is_ready():
        activity = activities[change_status.current_loop % len(activities)]
        await bot.change_presence(activity=activity)


bot.run("")