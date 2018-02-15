import discord
import asyncio
import logging

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    # Bot only logs chats it has perms to read.
    # Prints output of chat to console bot is running in.
    print('{}, sent by: {}, @ {}, in {} | #{}\n'.format(message.content, message.author, message.timestamp, message.server, message.channel))

    # Logs output of chats exposed to Bot in flatfile DB.
    if message.content.startswith('!ping'):
       await client.send_message(message.channel, 'Pong!')




    # looks for !test command
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have sent {} messages when ive been online, @{}'.format(counter, message.author))
        print(message.author, 'told me to count messages in', message.channel, 'chat, on ', message.server)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        print(message.author, 'in', message.channel, 'chat, on ', message.server, ', told me to sleep')

    # does nothing right now
    if message.content.startswith('!find'):
        member = find(lambda m: m.name == '', channel.server.members)


async def on_error():
    print('Fatal Error')
client.run('Mzk3NTU4OTUwNjcwNzYxOTg0.DSyFeA.V8CdO3o69Be8XUcFhAvhLddGYzQ')