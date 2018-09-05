import discord, asyncio, logging
from datetime import datetime

client = discord.Client()
stack = []

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

# welcomes new user
@client.event
async def on_member_join(member):
    server = member.server

    # log member join to stack
    stack.append(f'{ member } joined the server')

    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message(message):
    stack.append(f'{ message.author }: { message.content }')
    print( str( message.author ).split('#')[0] + ': ' + str(message.content))
    # Help menu for those new to the bot
    if message.content.startswith('!help'):
        await client.send_typing(message.channel)
        await client.send_message(message.author, 'https://github.com/Sadin/misfit/wiki/Help')
        await client.send_message(message.channel, 'I sent you a DM.')

    # Simple Ping Command.
    if message.content.startswith('!ping'):
        await client.send_typing(message.channel)
        await client.send_message(message.channel, 'Pong!')

    # 

    # @everyone the server from whatever channel ( sent to #announcements )
    if message.content.startswith('!announce'):
        await asyncio.sleep(1)

    # ganggang related commands
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
        print(f'Added { member_name } | { message.author } to @ganggang')
        await client.send_message(message.channel, f'{ member_name }, you\'re now subscribed to ganggang BOIIIIII!' )

    # give user the stack
    if message.content.startswith('!traceback'):
        print('Logging message stack to discord... ( last 10 items )')
        await client.send_typing(message.channel)
        temp_stack = stack
        temp_stack.reverse()
        for item in range(9):
            await client.send_message(message.channel, str(temp_stack[item]))
        print('Stack dump complete')
        temp_stack = None

async def on_error():
    print('Fatal Error')
client.run('Mzk3NTU4OTUwNjcwNzYxOTg0.DSyFeA.V8CdO3o69Be8XUcFhAvhLddGYzQ')

# takes a string, breaks it into parts and formats it for actions/logging.
def parse_text(message):
    
    formatted = message.rsplit(message)

    return formatted

def log_event(eventData):
    event = parse_text(eventData)

    stack.append(event)


