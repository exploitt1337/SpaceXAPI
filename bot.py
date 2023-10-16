import discord
from discord.ext import commands
from spacex.spacex import SpaceXAPI
import json, sellix, os, requests
from threading import Thread
spacex = SpaceXAPI()

with open('config.json', 'r') as file:
    config_data = json.load(file)
    bot_token = config_data.get('bot_token')
client = commands.Bot(command_prefix='-', intents=discord.Intents.all())

@client.event
async def on_ready():
    ip = requests.get('https://api.ipify.org').text
    os.system("cls || clear")
    print("Connected; ", client.user)
    print("Offline Webhook: http://" + ip + ":1010/offline")
    print("Online Webhook: http://" + ip + ":1010/online")

@client.command()
async def generate(ctx, request_type, amount):
    response = spacex.generate(request_type, float(amount))
    if not response.get('error'):
        key, url = response['key'], response['url']
        await ctx.send(f'Key: {key}\nURL: {url}')
    else:
        await ctx.send(f'Error: {response["message"]}')

@client.command()
async def balance(ctx):
    balance = spacex.balance()
    await ctx.send(balance['balance'] + "$")

Thread(target=sellix.run).start()
client.run(bot_token, reconnect=True)
