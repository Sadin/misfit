import discord, asyncio, logging
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("""
 /$$$$$$$             /$$               /$$                          
| $$__  $$           | $$              | $$                          
| $$  \ $$ /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$$
| $$$$$$$/|____  $$|_  $$_/   /$$_____/| $$__  $$ /$$__  $$ /$$_____/
| $$____/  /$$$$$$$  | $$    | $$      | $$  \ $$| $$$$$$$$|  $$$$$$ 
| $$      /$$__  $$  | $$ /$$| $$      | $$  | $$| $$_____/ \____  $$
| $$     |  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$ /$$$$$$$/
|__/      \_______/   \___/   \_______/|__/  |__/ \_______/|_______/`
    """)
    print(f'Login successful...\nusername:{client.user.name} | id:{client.user.id}')
    await client.change_presence(game=discord.Game(name='with unwanted toys'))

def log_to_discord()
    message_author = str(message.author)
    message_channel = '#' + str(message.channel)
    await client.send_message(client.get_channel('413799927622139937'), f'{message.timestamp} in {message_channel} | { message_author.strip("@")}: {str(message.content)}')



    # Bot only logs chats it has perms to read.
    # Prints output of chat to console botis running in.
    print('{}, sent by: {}, @ {}, in {} | #{}\n'.format(message.content, message.author, message.timestamp, message.server, message.channel))
    print(message.type)
    # Duplicated all messages to the #Logs Channel


# welcomes new user
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    # Establish Logging channel
    if not message.channel == client.get_channel('413799927622139937'):


        #Help menu for those new to the bot.abs
        if message.content.startswith('!help'):
            await client.send_message(message.author, 'https://github.com/Sadin/misfit/wiki/Help')
            await client.send_message(message.channel, 'I sent you a DM.')

        # Simple Ping Command.
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

        if message.content.startswith('!announce'):
            await asyncio.sleep(1)
    else:
        print(f'Will not log chats sent to #logs')

async def on_error():
    print('Fatal Error')
client.run('Mzk3NTU4OTUwNjcwNzYxOTg0.DSyFeA.V8CdO3o69Be8XUcFhAvhLddGYzQ')
