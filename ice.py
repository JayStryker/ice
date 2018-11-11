import discord
from discord.ext import commands

TOKEN = 'NTEwMDU5OTEzMjA5MTg0MjY2.DsW2lg.1Sf0iHnRYIGlmjpgbiYH2yuGXxo'
client = commands.Bot(command_prefix = 'p?')


@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name='p?help'))
	print('Bot online')
	print('ID')
	print('I am alive finally')
	
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.server.roles, name='Member')
	await client.add_roles(member, role)
	
@client.event
async def on_member_join(member):
	print("Recognised that a member called " + member.name + "joined")
	await client.send_message(member, "Welcome to the server!")
	print("Sent message to " + member.name)
	
@client.command(pass_context=True)
async def clear(ctx, amount=100):
	channel = ctx.message.channel
	messages = [ ]
	async for message in client.logs_from(channel, limit=int(amount) +1):
		message.append(message)
	await client.delete_messages(messages)
	await client.say('Messages deleted.')
	
#command - Help	
@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
	           colour = discord.Colour.orange()
	)
	
	embed.set_author(name='                                      Commands')
	embed.add_field(name='support', value='Shows this message', inline=True)
	embed.add_field(name='clear', value='Clears chat', inline=True)
	embed.add_field(name='kick', value='Kicks member', inline=True)
	embed.afd_field(name='join', value='invites member to my discord', inline=True)
	
	await client.send_message(author, embed=embed)
	await client.say('sent commands in your dms')
	
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(description=":error: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.kick(user)
            embed = discord.Embed(description=f":check: Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)
        
@client.command(pass_context=True)
async def join(ctx):
	await client.say('Sorry the link has been used by other discords so no invite link :(')
     
client.run(TOKEN)
