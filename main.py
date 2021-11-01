import discord
import random
import requests
import json
import os
from replit import db

client = discord.Client()


sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable', 'depressing']

starter_encouragements = [
    'Cheer up!', 'Hang in there.', 'You are a great thing.', 'Too bad, wierdo.'
]

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if 'encouragements' in db.keys():
        encouragements = db['encouragements']
        encouragements.appen(encouraging_message)
        db['encouragements'] = encouragements
    else:
        db['encouragements'] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db['encouragements']
    if len(encouragements) > index:
        del encouragements[index]
        db['encouragements'] = encouragements


@client.event
async def on_ready():
    print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if message.content.startswith('$hello'):
        await message.channel.send('Hello, I am Soviet Bot.')

    if msg.startswith('$ping'):
      await message.channel.send('ALL HAIL THE USSR')
      
    if message.content.startswith('$creator'):
        await message.channel.send('I was created by Zhong Xina!')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encouraging_message = msg.split('$new ', 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send('New encouragement added!')
    
    if msg.startswith('$cmds'):
      await message.channel.send(
        'Hello, I am Heckers Assistant! You can use the commands $help or $commands to view my commands. You can use the commands $ping or $hello, to see if I am operational, you can use the command $creator to see who I was created by, and you can use the command $inspire to have me send a random inspirational quote using https//:www.zenquotes.io. Remember, ALL HAIL THE USSR' 
      )