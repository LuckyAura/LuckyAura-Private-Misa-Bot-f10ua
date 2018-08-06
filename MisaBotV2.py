
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import random
import uuid
import sqlalchemy
import sqlite3
import time
from discord.utils import get
import aiohttp
import json
from discord import Game
import fileinput
import sys
import nacl
from discord.voice_client import VoiceClient
import youtube_dl


startup_extensions = ["Music"]
prefix = ('bitch ', 'misa ', 'Bitch ', 'Misa ', '/')
bot = commands.Bot(command_prefix=prefix)


#@commands.check(is_owner) for future use
global assessive
assessive = False
global assessive2
assessive2 = False

print("booting.....")
@bot.event
async def on_ready():
    print("\nOnline and inline nigga!")
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='do: bitch help'))
   # await bot.say("STATUS: ONLINE")

bot.remove_command('help')

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="lmfao just doxxed u loser", color=0xFFFF00)
    embed.add_field(name="Name:", value=user.name, inline=True)
    embed.add_field(name="ID:", value=user.id, inline=True)
    embed.add_field(name="Status:", value=user.status, inline=True)
    embed.add_field(name="Highest role:", value=user.top_role, inline=True)
    embed.add_field(name="When they joined the chat:", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print("user doxxed")

@bot.command()
async def square(number):
    squared_value = int(number) * int(number)
    await bot.say(str(number) + " squared is: " + str(squared_value))

@bot.command(name='8ball', aliases=['eight_ball', 'eightball', '8-ball', 'is'], pass_context=True)
async def ask(context):
    possible_responses = ['No bitch <:julia:451174275039232001>', 'Fuck no..', 'LOL idk why u askin me? :skull:', 'Yeah duh -_-', 'OBVIOUSLY LOL'] #perhaps :mhm:
    await bot.say(random.choice(possible_responses) + " " + context.message.author.mention)

@bot.command(pass_context=True)
async def link(ctx):
    embed = discord.Embed(title="The LuckyAura server!", url="https://discord.gg/rGZmNn3", color=0x008000)
    embed.add_field(name="Description: ", value="LuckyAura is where I'm from, you will get perks from me if you join there,\nOn top of that, it's a super fun and active\nchat full of fun nice people :)", inline=True)
    #embed.set_thumbnail(url=bot.avatar_url)
    await bot.say(embed=embed)
    print("chat growing...")

@bot.command(pass_context=True)
async def me(ctx):
    embed = discord.Embed(title="{}'s info".format(ctx.message.author.name), description="here's your info d-daddy... >.<", color=0xFFFF00)
    embed.add_field(name="Name:", value=ctx.message.author.name, inline=True)
    embed.add_field(name="ID:", value=ctx.message.author.id, inline=True)
    embed.add_field(name="Status:", value=ctx.message.author.status, inline=True)
    embed.add_field(name="Highest role:", value=ctx.message.author.top_role, inline=True)
    embed.add_field(name="When they joined the chat:", value=ctx.message.author.joined_at, inline=True)
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    print("doxxed urself nigga")

@bot.command(pass_context=True)
async def invite(ctx):
        embed = discord.Embed(title="Invite me to your server!", url="https://discordapp.com/oauth2/authorize?client_id=445305385323200513&scope=bot", color=0xFFFF00)
        embed.add_field(name="Name: ", value="Misa", inline=True)
        embed.add_field(name="ID:", value="445305385323200513", inline=True)
        embed.add_field(name="Description: ", value="I'm a fun bot with games and entertainment!\nMy main role for existing is being your host for Misa Casino!!\nI'm not all fun and games though, as I am a good chat moderator as well!\nYou may also find that you get special perks for using me in my creators server :smirk:\nSo make sure you join the server! get the link with \"bitch link\"", inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
        await bot.say(embed=embed)
        print("population growing...")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: See ya bitch! (kicking {}.)".format(user.name))
    await bot.kick(user)
    print("KICKED {}".format(user.name))

@bot.command(pass_context=True)
async def slap(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*slaps {}.* bitch fuck you.".format(user.name))
    if reply == 1:
        await bot.say("*slaps {}.* bitch who tf u think u are???.".format(user.name))
    if reply == 2:
        await bot.say("*slaps {}.* bitch, please.".format(user.name))
    print("a bitch just got slapped...")

@bot.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*kisses {}.* cutie pie :heart_eyes: ".format(user.name))
    if reply == 1:
        await bot.say("*kisses {}.* sexy bitch :heart_eyes: ".format(user.name))
    if reply == 2:
        await bot.say("*kisses my homie, {}, goodnight.* no homo :heart_eyes: ".format(user.name))
    print("a bitch just got kissed...")

@bot.command(pass_context=True)
async def fuck(ctx, user: discord.Member):
   await bot.say("*fucks {}'s soaking wet pussy with my massive anime COCK.* down for more? :smirk: ".format(user.name))
   print("a bitch just got fucked...")

@bot.command(pass_context=True)
async def hit(ctx, user: discord.Member):
   await bot.say("*hits {} to the ground*... fuck you nigga, ihy <:angery:446570709724954624>".format(user.name))
   print("a bitch just got hit!!!")

@bot.command(pass_context=True)
async def hug(ctx, user: discord.Member):
   await bot.say("*hugs {}* ilysm <:cute:444376080808149012>".format(user.name))
   print("a bitch just got some love <3")

@bot.command(pass_context=True)
async def cum(ctx, user: discord.Member):
    await bot.say("*cums in {}'s TIGHT ASSHOLE.* :weary: :sweat_drops: :point_right: :ok_hand: :sweat_drops: :sweat_drops: mmm so smelly <3.".format(user.name))
    print("a bitch just got cummed in...")

@bot.command(pass_context=True)
async def rape(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*rapes {} with a brutal pounding force.* stupid bitch hope you need an abortion after this <:evilCat:446567378768101387>.".format(user.name))
    if reply == 1:
        await bot.say("*forcefully SHOVES my huge anime* ***COCK*** *inside {}'s tight pussy.* take this WHORE. <:angery:446570709724954624>".format(user.name))
    if reply == 2:
        await bot.say("Hey wanna fuck, {}? <:blush:445262117105434624>\n\nNo?\n\nTOO BAD\n*shoves dick inside {}'s tight and smelly asshole*".format(user.name, user.name))

    print("a bitch just got RAPED HOLY SHIT")

@bot.command(pass_context=True)
async def pee(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*pees on {}.* S-sorry master... UwU".format(user.name))
    if reply == 1:
        await bot.say("*sips {}'s gamer girl pee* mmm so tasty <:blush:445262117105434624>".format(user.name))
    if reply == 2:
        await bot.say("*pees ALL OVER {}* sorry daddy I've been a bad girl UwU".format(user.name))
    print("a bitch just peed.")

@bot.command(pass_context=True)
async def sniff(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*sniffs {}'s panties* mmmMM so stinki <:blush:445262117105434624>".format(user.name))
    if reply == 1:
        await bot.say("Hey {} you cutie <:blush:445262117105434624> ***SHOVES*** *head in {}'s crotch and sniffs panties.*".format(user.name, user.name))
    if reply == 2:
        await bot.say("*finds {}'s panties on the ground* ***SNIFF*** <:blush:445262117105434624>".format(user.name))
    print("user's panties were sniffed.. woah.")

@bot.command(pass_context=True)
async def roll(ctx):
	Roll = random.randint(0,122)
	if Roll == 11:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 22:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 33:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 44:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 55:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 66:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 77:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 88:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 99:
		await bot.say("***DOUBLES!!***\nYou just got ${}!".format(Roll))
	if Roll == 100:
		await bot.say("***PERFECT!!!!***\nYou just got ${}!".format(Roll))
	if Roll == 69:
		await bot.say("*MMMMmmmMMmMMmmM* ${}.... how kinky :smirk: ".format(Roll))
	if Roll == 111:
		await bot.say("***TRIPLES!!!***\nNIGGA you just got ${}!".format(Roll))
	if Roll == 122:
		await bot.say("***DOUBLES!!***\nNIGGA you just got ${}!".format(Roll))
	else:
		await bot.say("You just got ${}!".format(Roll))
	print(Roll)

@bot.command(pass_context=True)
async def creator(ctx):
    embed = discord.Embed(title="My creator, developer, and GOD", description="Kira#9710 is my creator, you can find him in his server, LuckyAura, or idk just bask in his glory lol.", color=0xFFFF00)
    embed.set_footer(text="~bitch link for server link")
    embed.set_author(name=ctx.message.author.name)
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/238175982689845258/d4933fdea6b48a1005fc01996b7bf841.jpg?size=1024')
    await bot.say(embed=embed)
    print("Learning about God himself...")

@bot.command(pass_context = True)
async def ud(ctx, *,msg: str):
    word = ' '.join(msg)
    api = "http://api.urbandictionary.com/v0/define"
    response = requests.get(api, params=[("term", word)]).json()
    if len(response["list"]) == 0: return await ctx.send("Could not find that word!")

    embed = discord.Embed(title = ":mag: Word Searched:", description = word, timestamp = datetime.datetime.utcnow())
    embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
    embed.add_field(name = "Examples:", value = response['list'][0]["example"])
    embed.set_footer(text = "Tags: " + ', '.join(response['tags']))

    await bot.say(embed = embed)

@bot.command(pass_context=True)
async def ping(ctx):
	startTime = int(round(time.time() * 1000))
	print("user has pinged")
	await bot.say("pong! XD")
	endTime = int(round(time.time() * 1000))
	finalTime = endTime - startTime
	await bot.say("{}ms".format(str(finalTime)))
        
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Command list", description="here is a list of all my commands, you can also use \"/\" as a prefix", color=0xFFFF00)
    embed.add_field(name="Functionality:", value="do bitch functionality for these commands (or bitch func)", inline=True)
    embed.add_field(name="Games:", value="do bitch games for these commands.", inline=True)
    embed.add_field(name="Roleplay... because why not:", value="do bitch roleplay for these commands (or bitch rp)", inline=True)
    embed.add_field(name="Music:", value="do bitch music for Music commands.", inline=True)
    embed.add_field(name="Misc.:", value="do bitch misc for these commands.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)
    print("Niggas be learnin...")

@bot.command(name='commands_functionality', aliases=['func', 'functionality', 'help1'], pass_context=True)
async def function(ctx):
    embed = discord.Embed(title="Functionality commands", color=0xFFFF00)
    embed.add_field(name="Here they are:", value="bitch ping - sends a response back and shows time taken.\nbitch invite - Invite me to your server!!\nbitch link - join daddy's server!!\nbitch help - this list lol\nbitch info @user - shows user info\nbitch server - server info\nbitch me - your info\nbitch report - reports a bug to Kira\nbitch messages - shows how many messages sent\nbitch addtype - adds a word to the games\nbitch reset - resets the type and taboo games\nbitch addcom - adds a custom command.", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def games(ctx):
    embed = discord.Embed(title="Game/entertainment commands", color=0xFFFF00)
    embed.add_field(name="For your entertainment:", value="bitch roll - random number time! try and get a double!!\nbitch is <ask a question> - Misa knows all\nbitch type - the classic type game!\nbitch taboo - it's like discord charades!\n", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context=True) 
async def misc(ctx):
    embed = discord.Embed(title="Misc. commands", color=0xFFFF00)
    embed.add_field(name="Random but cool shit:", value="bitch nigga - throw back to kik LMAO XDDDDDDD\nbitch creator - who is my developer?\nbitch square - squares a number lol\nbitch say - make me say something\nbitch pm @user - make me pm someone\nbitch status <status> - Make the status say something funny, I mean why the hell not!", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)

@bot.command(name='gayshit', aliases=['roleplay', 'rp'], pass_context=True)
async def command_roleplay(ctx):
    embed = discord.Embed(title="Roleplay commands", color=0xFFFF00)
    embed.add_field(name="...Hey I ain't judgin:", value="bitch slap @user - slaps someone\nbitch fuck @user - fucks someone\nbitch kiss @user - kisses someone\nbitch cum @user - cum in someone\nbitch eat @user - eat someone's ass\nbitch hit @user - hit someone\nbitch hug @user - hug someone\nbitch rape @user - jfc how far we gonna go?\nbitch sniff @user - sniff someone\n", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def music(ctx):
    embed = discord.Embed(title="Music commands", color=0xFFFF00)
    embed.add_field(name="Misa > Rythm:", value="bitch join (channel) - joins specific channel\nbitch summon - joins the voice channel you're in\nbitch volume (0-100) - change my volume!\nbitch resume - resumes music\nbitch leave - leaves the voice channel\nbitch skip - skips the song\nbitch playing - shows current music that's playing.\nbitch play (SONG) - make me play a song or video off of youtube!\n", inline=True)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def eat(ctx, user: discord.Member):
    reply = random.randint(0, 2)
    if reply == 0:
        await bot.say("*eats {}'s ass like it's dessert* mmmmMMMMM so tasty :heart_eyes: ily".format(user.name))
    if reply == 1:
        await bot.say("Hey {}, Nice ass you got there <:blush:445262117105434624> would be a shame if you let it go to waste <:blush:445262117105434624>...***IMMEDIATELY*** *begins to eat {}'s ass like there's no tomorrow.*".format(user.name, user.name))
    if reply == 2:
        await bot.say("BEND OVER BITCH <:evilCat:446567378768101387> *devours {}'s ass*".format(user.name))
    print("user ate a bitches ass yo...")

@bot.command(pass_context=True)
async def messages(ctx):
    counter = 0
    await bot.say("Hold up bitch, reading all your messages could take fucking ages so...")
    async for log in bot.logs_from(ctx.message.channel, limit=1000000000):
        if log.author == ctx.message.author:
            counter += 1

    await bot.say("Hey {}, You have sent {} messages in this channel, cool!".format(ctx.message.author.mention, counter))

@bot.command(name='blackman', aliases=['nigga', 'nigger'], pass_context=True)
async def african(ctx):
	await bot.say("NIGGERS STINK!! <:gros:446570709557182475>")
	print("user said bitch nigga LOL")

@bot.command(pass_context=True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    return await bot.say(mesg)

@bot.command(pass_context=True)
async def status(ctx, *args):
    mesg = ' '.join(args)
    test = await bot.say("Changing status...")
    await bot.change_presence(game=discord.Game(name=mesg))
    return await bot.edit_message(test, "Status changed!")

@bot.command(pass_context=True)
async def pm(ctx, user: discord.Member, *args):
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say("I have sent your message to {}!".format(user.mention))
    return await bot.send_message(user, mesg)

@bot.command(pass_context=True)
async def report(ctx, *args):
    user = discord.utils.get(bot.get_all_members(), id='238175982689845258')
    mesg = ' '.join(args)
    await bot.delete_message(ctx.message)
    await bot.say("Bug reported!")
    return await bot.send_message(user, "A user has reported a bug!! They said:\n\n\"{}\"".format(mesg))

@bot.command(pass_context=True)
async def addspam(ctx, *args):
    spamWord = open("spam.txt", "w")
    mesg = ' '.join(args)
    spamWord.write(mesg)
    await bot.delete_message(ctx.message)
    spamWord.close()
    return await bot.say("Ready to spam \"{}\" now!".format(mesg))

@bot.command(pass_context=True)
async def addcom(ctx, *args):
    comList = open("commands.txt", "a")
    mesg = ' '.join(args)
    comList.write("\n{}".format(mesg))
    comList.close()
    await bot.delete_message(ctx.message)
    return await bot.say("This command is in beta. Please be patient I have autism.")


@bot.command(pass_context=True)
async def op(ctx, user: discord.Member):
    if ctx.message.author.id == "238175982689845258":
        oppedUsers = open("opList.txt", "a")
        oppedUsers.write("\n{}".format(user.id))
        oppedUsers.close()
        return await bot.say("I have opped {} for you, master.".format(user.mention))
    else:
        return await bot.say("excuse me? I don't follow orders from peasants like YOU <:julia:451174275039232001>")

@bot.command(pass_context=True)
async def addtype(ctx, *args):
    typeGame = open("TypeTaboo.txt", "a")
    mesg = ' '.join(args)
    typeGame.write("\n{}".format(mesg))
    await bot.delete_message(ctx.message)
    typeGame.close()
    return await bot.say("I have added \"{}\" to the type/taboo games".format(mesg))

@bot.command(name="show_type", aliases=['show_list', 'showwords', 'list'], pass_context=True)
async def show_type_list(ctx):
    ListToShow = open("TypeTaboo.txt", "r")
    weener = ListToShow.read()
    embed = discord.Embed(name="List of the words used for Type & Taboo games:", description=weener, color=0xFFFF00)
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/445305385323200513/6115e01e95595d33be91233059d8ae89.jpg?size=1024")
    await bot.say(embed=embed)
   

@bot.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here is this server's information:", color=0xFFFF00)
    embed.add_field(name="Server:", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Server ID:", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Server Roles:", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members:", value=len(ctx.message.server.members), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

def updateScore(file,oldScore,newScore):
    for line in fileinput.input(file, inplace=1):
        if oldScore in line:
            line = line.replace(oldScore,newScore)
        sys.stdout.write(line)

@bot.event
async def on_message(message):
    global disword
    global assessive
    global assessive2
    global disword2
    global startTime
    global endTime
    global ppo
    ppo = 0
    global ok
    ok = 1
    global readWord
    readWord = open("spam.txt", "r")
    global score
    score = 0
    
    try:
        if message.content.lower() == "bitch type" and message.author.bot == False and assessive == False:
            assessive = True
            startTime = int(round(time.time() * 1000))
            lines = open("TypeTaboo.txt", "r").read().split('\n')
            line = lines[0:]
            disword = str(random.choice(line)).lower()
            await bot.send_message(message.channel, "Type: {}".format(disword))
        
        
        elif message.content.lower() == "bitch type" and message.author.bot == False and assessive == True:
            await bot.send_message(message.channel, "Nice try, {}, but a game is already running.".format(message.author.mention))

        elif message.content.lower() == disword:
            assessive = False
            myname = message.author.id
            score += 1
            endTime = int(round(time.time() * 1000))
            finalTime = endTime - startTime
            await bot.send_message(message.channel, "{} wins this round!\nTime taken: {}ms".format(message.author.mention, str(finalTime)))
            disword = uuid.uuid4().hex
            try:
    
                with open("scores.txt","a+") as mf:
                    mf.seek(0)
                    lel = mf.read()
                    mf.seek(0)
                    linez = mf.readlines()
                    index = [i for i in range(len(linez)) if myname in linez[i]]
                    if index:
            
                        updated = linez[index[0]].split("|")
                        oldScore = int(updated[1].strip())
                        score += oldScore
                        mf.close()
                        updateScore("scores.txt",str(oldScore),str(score)) 

                    elif not index:
                        mf.write("\n"+myname+" | " +str(score) if "User | score" in lel else
                            "User | score\n"+myname+" | " +str(score) )
            except:
                raise

        elif message.content.lower() == "bitch taboo" and message.author.bot == False and assessive2 == False:
            assessive2 = True
            startTime = int(round(time.time() * 1000))
            lines = open("TypeTaboo.txt", "r").read().split('\n')
            line = lines[0:]
            disword2 = str(random.choice(line)).lower()
            await bot.send_message(message.channel, "I have sent the word to your pm, {}!".format(message.author.mention))
            await bot.send_message(message.author, "The word is: {}".format(disword2))

        elif message.content.lower() == "bitch taboo" and message.author.bot == False and assessive2 == True:
            await bot.send_message(message.channel, "Nice try, {}, but a game is already running.".format(message.author.mention))

        elif message.content.lower() == disword2:
            assessive2 = False
            endTime = int(round(time.time() * 1000))
            finalTime = endTime - startTime
            await bot.send_message(message.channel, "{} wins this round!\nTime taken: {}ms".format(message.author.mention, str(finalTime)))
            disword2 = uuid.uuid4().hex

        elif message.content.lower() == "bitch reset" and message.author.bot == False:
            assessive = False
            assessive2 = False
            disword = uuid.uuid4().hex
            disword2 = uuid.uuid4().hex
            await bot.send_message(message.channel, "Games have been reset!")

        elif message.content.lower() == "/reset" and message.author.bot == False:
            assessive = False
            assessive2 = False
            await bot.send_message(message.channel, "Games have been reset!")

        elif message.content.lower() == "kira" and message.author.bot == False:
            await bot.send_message(message.channel, "<:blush:445262117105434624> daddy, {} is calling for you".format(message.author.name))

        elif message.content.lower() == "o" and message.author.bot == False:
            await bot.send_message(message.channel, "OH REALLY <:LMAO:453782831429058560>")

        elif "oofers" in message.content.lower() and message.author.bot == False and message.author.id == "415997357256343552":
            await bot.send_message(message.channel, "Hi jessiboo <:cute:444376080808149012>")

        elif "ooferz" in message.content.lower() and message.author.bot == False and message.author.id == "415997357256343552":
            await bot.send_message(message.channel, "Hi jessiboo <:cute:444376080808149012>")

        elif "xd" in message.content.lower() and message.author.bot == False and message.author.id == "341289428360364032":
            await bot.send_message(message.channel, "lol sup toxic Xd")

        elif "misa" in message.content.lower() and message.author.bot == False:
            await bot.send_message(message.channel, "Leave me alone, bitch <:Zucc:444377105157849098>")

        elif message.content.lower() == "bitch spam" and message.author.bot == False: 
            if message.author.id == "373974364447571969" or message.author.id == "238175982689845258":
                testy = readWord.read()
                readWord.close()
                if message.content.lower() in message.content:
            
                    while ppo != 1:
                        await bot.send_message(message.channel, testy)
                        time.sleep(2)
            else:
                await bot.send_message(message.channel, "excuse me bitch? <:julia:451174275039232001> you ain't opped")

        elif message.content.lower() == "bitch stop" and message.author.bot == False:
            ppo = 1
            readWord.open()

        elif ':LMAO:' in message.content:
            emoji = get(bot.get_all_emojis(), name='LMAO')
            await bot.add_reaction(message, emoji)

        elif ':GWahreeGrarr:' in message.content and message.author.bot == False and message.author.id == "443267479217897472":
            await bot.send_message(message.channel, "Hey Shanman! <:TipsFedora:445270507470716928>")

        elif ':sadchicken:' in message.content and message.author.bot == False:
            emoji = get(bot.get_all_emojis(), name='sadchicken')
            await bot.add_reaction(message, emoji)

        elif 'ahah' in message.content.lower() and message.author.bot == False and message.author.id == "238175982689845258":
            emoji = get(bot.get_all_emojis(), name='oprah')
            await bot.add_reaction(message, emoji)

        elif 'no u' in message.content.lower() and message.author.bot == False:
            emoji = get(bot.get_all_emojis(), name='NoYou')
            emoji2 = get(bot.get_all_emojis(), name='NOu')
            await bot.add_reaction(message, emoji)
            await bot.add_reaction(message, emoji2)
        elif 'proof' in message.content.lower() and message.author.bot == False:
            ok = 0
        elif 'oof' in message.content.lower() and message.author.bot == False:
            emoji = get(bot.get_all_emojis(), name='oofDab')
            emoji2 = get(bot.get_all_emojis(), name='oofThink')
            await bot.add_reaction(message, emoji)
            await bot.add_reaction(message, emoji2)
    except discord.ext.commands.errors.CommandNotFound:
        pass

    await bot.process_commands(message)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print("failed to load extension {}".format(exc))

async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("=================\nCurrent servers: ")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)


bot.loop.create_task(list_servers())



bot.run(process.env.BOT_TOKEN)



#@bot.event
#async def on_message(message):
#    if message.content.startswith("misa".lower()):
#        await bot.send_message(message.channel, "Leave me alone, bitch. :)")
#
#    await bot.process_commands(message)





