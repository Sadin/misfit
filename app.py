import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages on this server since ive joined, @{}'.format(counter, message.author))
        print(message.author, 'told me to count messages in', message.channel, 'chat, on ', message.server)
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        print(message.author, 'in', message.channel, 'chat, on ', message.server, ', told me to sleep')

    if message.content.startswith('!find'):
        member = find(lambda m: m.name == 'Mighty', channel.server.members)

client.run('Mzk3NTU4OTUwNjcwNzYxOTg0.DSxvMw.iXWfXfpLOmjIJUxr2DVJrgHtwP4')