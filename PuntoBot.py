import random
import asyncio
import aiohttp
import json
import imgurpython
from imgurpython import ImgurClient
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("¬")
TOKEN = "NDU3MTkwMDkwODQ2NzY1MDc2.DgVfAA.8GhanqDPwvrW-iKlW5jXj2bdib8"  # Get at discordapp.com/developers/applications/me

client = Bot(command_prefix=BOT_PREFIX)
#PRESET 8-BALL SHIT
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#POWER CALCULATOR
@client.command(name = "power",
                description="Calculates exponentials.",
                brief="Finds powers. Used: power [number] [power]")
async def power(number,power):
    squared_value = int(number)**int(power)
    await client.say(str(number) + " to the power of " + str(power) + " is " + str(squared_value) +".")

#IMGUR GRABBER
client_id = 'fa94b9e017ea009'
client_secret = 'aac1bc089b2dca419fbaa9d8d4135a9b7fb07aab'

imgclient = ImgurClient(client_id, client_secret)

@client.command(name = "imgrab",
                description="Grabs top image for a term from Imgur.",
                brief="Search Imgur. Used: imgrab [search]")
async def imgrab(term):
    result = imgclient.gallery_search(term, advanced=None, sort='time', window='all', page=0)    
    for item in result:
        print (item.link)
    await client.say("look in console")

#SET BOT STATE
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="gam"))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
