import discord
from discord.ext import commands
import os

def readToken():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

client = commands.Bot(command_prefix='.')

@client.event
async def on_member_join(member):
    await client.get_channel(749693397027127421).send(f"{member.name}, welcome to the server.  Please type /nick (Firstname) (Lastname)")

@client.command(aliases=['Suggest'])
async def suggest(ctx):
    file = open('suggestions.txt', 'a')
    suggestion_list = ctx.message.content.split()
    suggestion = ''
    for i in suggestion_list:
        if i.lower() != '.suggest':
            suggestion += i + ' '
    file.write(suggestion + '\n')
    file.close()
    await ctx.channel.send('Thank you for the suggestion')

TOKEN = readToken()
client.run(TOKEN)
