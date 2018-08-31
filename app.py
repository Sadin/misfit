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
    await client.change_presence(game=discord.Game(name='with dodgeballs'))

"""
def log_to_discord():
    message_author = str(message.author)
    message_channel = '#' + str(message.channel)
    await client.send_message(client.get_channel('413799927622139937'), f'{message.timestamp} in {message_channel} | { message_author.strip("@")}: {str(message.content)}')



    # Bot only logs chats it has perms to read.
    # Prints output of chat to console botis running in.
    print('{}, sent by: {}, @ {}, in {} | #{}\n'.format(message.content, message.author, message.timestamp, message.server, message.channel))
    print(message.type)
    # Duplicated all messages to the #Logs Channel
"""

# welcomes new user
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    #Help menu for those new to the bot.abs
    if message.content.startswith('!help'):
        await client.send_typing(message.channel)
        await client.send_message(message.author, 'https://github.com/Sadin/misfit/wiki/Help')
        await client.send_message(message.channel, 'I sent you a DM.')

    # Simple Ping Command.
    if message.content.startswith('!ping'):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, 'Pong!')

    if message.content.startswith('!announce'):
        await asyncio.sleep(1)

    if message.content.startswith('!gg'):

        # Show bot is doing something
        await client.send_typing(message.channel)

        member = message.author
        member_name = str(member).split('#')[0].capitalize() 
        
        await client.send_message(message.channel, f'Oh! { member_name } do you want to join the ganggang? ( type "yes" to confirm )')

        msg = await client.wait_for_message(author=message.author, content='yes')

        if msg:
            await client.send_typing(message.channel)
            role = discord.utils.get(message.author.server.roles, name="ganggang")

        await client.add_roles(member, role)
        await asyncio.sleep(1)
        await client.send_message(message.channel, f'{ member_name }, you\'re now subscribed to ganggang BOIIIIII!' )

async def on_error():
    print('Fatal Error')
client.run('Mzk3NTU4OTUwNjcwNzYxOTg0.DSyFeA.V8CdO3o69Be8XUcFhAvhLddGYzQ')

