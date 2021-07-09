import discord, time
from discord.ext.commands import Bot
from src.verif import code_verify, delete
import asyncio
token = "token"


botOpt={"logo": "https://orig00.deviantart.net/5c2f/f/2013/337/6/9/69d144a62410c5b34c8ad53b39804e7d-d6r7x9f.gif",
        "BotName": "Keter",
        "welcomeMsg":"!verify to be verified",
        "role":"verified",
        "blank":"https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1124px-Blank_button.svg.png",
        "prefix":"!",
        "channelid":862805487666069514}

intents = discord.Intents.default()
intents.members = True


keter = Bot(command_prefix = "keter", description = "keter", intents=intents)

verified = {}
prefix = botOpt["prefix"]

@keter.event
async def on_ready():
    await keter.change_presence(activity=discord.Game(name=f'{prefix}help'))
    print("Ready!")



@keter.listen()
async def on_message(message):

    content = message.content.split(" ")
    
    author = message.author
    channel = message.channel

    if channel.id != botOpt["channelid"]:
        return
    if author.id in verified and verified[author.id][0] == False:
        if message.content == verified[author.id][1]:
            
            embeded = discord.Embed(title=botOpt["BotName"], description='you have been verified', color=0xEE8700)
            embeded.set_thumbnail(url="https://media.giphy.com/media/sq3SxQclLXzRC/giphy.gif")
            msg = await channel.send(embed=embeded)
            role = discord.utils.get(author.guild.roles, name=botOpt["role"])
            await author.add_roles(role)
            del verified[author.id]
            await asyncio.sleep(10)
            await msg.delete()
            await delete()
        else:
            msg = await channel.send(content="Code invalide!")
            await asyncio.sleep(5)
            await msg.delete()
    if message.content == f"{prefix}help":
        embeded = discord.Embed(title=botOpt["BotName"], description='Help', color=0xEE8700)
        embeded.set_thumbnail(url=botOpt["logo"])
        embeded.add_field(name="** *verify **", value="Verify your account", inline=True)
        embeded.add_field(name="** *welcome **", value="Send the message for new person", inline=True)
        await channel.send(embed=embeded)
    if message.content == f"{prefix}welcome":
        await message.delete()
        embeded = discord.Embed(title=botOpt["welcomeMsg"], description='', color=0xEE8700)
        embeded.set_author(name=botOpt["BotName"],icon_url=botOpt["blank"])
        embeded.set_thumbnail(url=botOpt["logo"])
        embeded.set_footer(text="wait 30s befor send the code") 
        await channel.send(embed=embeded)
    if message.content == f"{prefix}verify":
        await message.delete()
        code = await code_verify(channel)
        verified[author.id] = [False, code]
    try:
        if author.id != keter.user.id:
            await message.delete()
    except:
        pass
keter.run(token)
