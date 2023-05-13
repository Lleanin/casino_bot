import nextcord
import logging
import os
from nextcord.ext import commands
import redis

r = redis.Redis(
    host='redis-16728.c266.us-east-1-3.ec2.cloud.redislabs.com',
    port=16728,
    password='purple_love0816',
    charset="utf-8",
    decode_responses=True
    )

intents = nextcord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)


# r.set('balance', '0')  # Установка значения
# user_id = r.get('index')  # Получение значения


# @bot.slash_command(description="Show your profile!"
# async def profile(interaction: nextcord.Interaction):
#     await interaction.send(file=nextcord.File('picture.png'))

@bot.event
async def on_message(message):
    if not message.author.bot:
        user_id = message.author.id
        r.set(user_id, bytes({'balance': 0}))


@bot.slash_command(description="Show your balance!")
async def my_balance(interaction: nextcord.Interaction):
    if not interaction.user.bot:
        user_id = interaction.user.id
    await interaction.send("Ваш баланс составляет:{}".format(r.get(user_id)))


@bot.command()
async def bonus(interaction: nextcord.Interaction):
    if not interaction.user.bot:
        user_id = interaction.user.id
    r.incrby(user_id, 200)
    await interaction.send("На ваш баланс зачислено 200 коинов!")


if __name__ == '__main__':
    bot.run('MTEwNTE5NzM1NDUwOTk0NjkxMA.G6KVPw.DUDQ1MVzIxw662YHS0wBCN8-ZPDJn7W0eNI6Is')