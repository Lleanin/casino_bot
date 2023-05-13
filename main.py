import nextcord
from nextcord.ext import commands
import redis
import json
import os
from dotenv import load_dotenv
from time import time

#Задание для Zeazy
'''
1) Разобраться с баллами в бд
'''

intents = nextcord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!",intents=intents)

@bot.slash_command(description="Show your profile!")
async def profile(interaction: nextcord.Interaction):
    await interaction.send(file=nextcord.File('picture.png'))


def encode_data(payload):
    return f"{payload}".encode()


def decode_data(payload):
    return json.load(payload)


@bot.event
async def on_message(message):
    if not message.author.bot:
        user_id = message.author.id
        r.hset(user_id,'balance', 0
               #'time': 0
              )


@bot.slash_command(description="Show your balance!")
async def my_balance(interaction: nextcord.Interaction):
    if not interaction.user.bot:
        user_id = interaction.user.id
    await interaction.send("Ваш баланс составляет:{}".format(r.hget(user_id))['balance'])


@bot.command()
async def bonus(interaction: nextcord.Interaction):
    if not interaction.user.bot:
        user_id = interaction.user.id
    user_data = r.hgetall(user_id)['balance']
    balance = user_data['balance']
    balance += 600
    user_data['balance'] = balance
    r.hset(user_id,'balance', balance)
    await interaction.send("На ваш баланс зачислено 600 коинов!")


if __name__ == '__main__':
    r = redis.Redis(
    host='redis-16728.c266.us-east-1-3.ec2.cloud.redislabs.com',
    port=16728,
    password='purple_love0816',
    charset="utf-8",
    decode_responses=True
    )
    load_dotenv()
    token = os.environ['DS_TOKEN']
    bot.run(token)