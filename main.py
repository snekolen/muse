import discord
from discord import voice_client
from discord.ext import commands
from finder import findSong, findUrl
from countries import allCountries, countryExists
import ffmpeg
import youtube_dl
import os

client = commands.Bot(command_prefix = "+")
playing = False

#Make a help page

@client.event
async def on_ready():
    print("Bot is ready") #Message prints out to the console when using an IDE

@client.event
async def on_command_error(ctx, error): #Add for CommandNotFound
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing argument")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Unable to convert between data types")

    
@client.command(name = "list") #Pulls up list of countries for each decade
async def _list(ctx, year: int): 
    try:
        if year < 1900 or year > 2020:
            raise Exception("Year must be between 1900 and 2020")
        elif year % 10 != 0:
            raise Exception("Year must end in 0")
    except Exception as e: #Other exceptions include MissingRequiredArgument and BadArgument
        await ctx.send(e)
    else:
        clist = allCountries(year)
    
        page1 = discord.Embed(
            title = str(year) + "s Countries (1/" + str(len(clist)) + ")",
            description = clist[0],
            color = discord.Color.blue()
        )
        page2 = discord.Embed(
            title = str(year) + "s Countries (2/" + str(len(clist)) + ")",
            description = clist[1],
            color = discord.Color.blue()
        )
        page3 = discord.Embed(
            title = str(year) + "s Countries (3/" + str(len(clist)) + ")",
            description = clist[2],
            color = discord.Color.blue()
        )
        pages = [page1, page2, page3]
        
        if len(clist) == 4:
            page4 = discord.Embed(
                title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                description = clist[3],
                color = discord.Color.blue()
            )
            pages.append(page4)
        elif len(clist) == 5:
            page4 = discord.Embed(
                title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                description = clist[3],
                color = discord.Color.blue()
            )
            pages.append(page4)
            page5 = discord.Embed(
                title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                description = clist[4],
                color = discord.Color.blue()
            )
            pages.append(page5)
        elif len(clist) == 6:
            page4 = discord.Embed(
                title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                description = clist[3],
                color = discord.Color.blue()
            )
            pages.append(page4)
            page5 = discord.Embed(
                title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                description = clist[4],
                color = discord.Color.blue()
            )
            pages.append(page5)
            page6 = discord.Embed(
                title = str(year) + "s Countries (6/" + str(len(clist)) + ")",
                description = clist[5],
                color = discord.Color.blue()
            )
            pages.append(page6)
        elif len(clist) == 7:
            page4 = discord.Embed(
                title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                description = clist[3],
                color = discord.Color.blue()
            )
            pages.append(page4)
            page5 = discord.Embed(
                title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                description = clist[4],
                color = discord.Color.blue()
            )
            pages.append(page5)
            page6 = discord.Embed(
                title = str(year) + "s Countries (6/" + str(len(clist)) + ")",
                description = clist[5],
                color = discord.Color.blue()
            )
            pages.append(page6)
            page7 = discord.Embed(
                title = str(year) + "s Countries (7/" + str(len(clist)) + ")",
                description = clist[6],
                color = discord.Color.blue()
            )
            pages.append(page7)
            
        
        message = await ctx.send(embed = page1)
        await message.add_reaction('⏮')
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('⏭')
    
        def check(reaction, user):
            return user == ctx.author
    
        i = 0
        reaction = None
    
        while True:
            if str(reaction) == '⏮':
                i = 0
                await message.edit(embed = pages[i])
            elif str(reaction) == '◀':
                if i > 0:
                    i -= 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '▶':
                if i < len(clist) - 1:
                    i += 1
                    await message.edit(embed = pages[i])
            elif str(reaction) == '⏭':
                i = len(clist) - 1
                await message.edit(embed = pages[i])
            
            try:
                reaction, user = await client.wait_for('reaction_add', timeout = 50.0, check = check)
                await message.remove_reaction(reaction, user)
            except:
                break
    
        await message.clear_reactions()


@client.command(name = "join") #Makes bot join VC
async def join(ctx):
    userConnected = ctx.author.voice 
    try:
        if userConnected:
            await userConnected.channel.connect()
        else:
            raise Exception("Please connect to the voice channel")
    except Exception as e:
        await ctx.send(e)
        

@client.command(name = "play", pass_context = True) #Plays music based on command
async def _play(ctx, *args): #Args include word(s) in the country's name and year
    country = " ".join(args[0:len(args) - 1])
    year = args[len(args) - 1]
    '''
    if not ctx.voice_client:
        userConnected = ctx.author.voice 
        await userConnected.channel.connect()
    '''
              
    try:
        if len(args) == 1 or args[len(args) - 1].isnumeric() == False: 
            raise Exception("Please re-enter your command in the format '+play [country] [year]'")
        elif int(year) < 1900 or int(year) > 2020:
            raise Exception("Year must be between 1900 and 2020")
        elif int(year) % 10 != 0:
            raise Exception("Year must end in 0")
        elif countryExists(country, int(year)) == False:
            raise Exception(country + " did not exist in the " + str(year)+ "s")
    except Exception as e:
        await ctx.send(e)
    await ctx.send("Loading song from " + country + " in the " + year + "s...")

    #Finding and playing songs
    songDict = findSong(country, int(year))
    songDict = findUrl(songDict)
    await ctx.send(songDict["Song"] + " by " + songDict["Artist"] + ", released " + songDict["Year"]) #Info about song
    await ctx.send(songDict["URL"]) #Line 2
    
    song_there = os.path.isfile("song.mp3")

    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        return
    
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name = "General") #Change name part to name of voice channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    url = songDict["URL"]
    ydl_opts = {
        "format" : "bestaudio/best", 
        "postprocessors" : [{
            "key" : "FFmpegExtractAudio", 
            "preferredcodec" : "mp3",
            "preferredquality": "192",
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))  
    #include error handling for whether the message author is connected

            
#Include skip, resume, and pause commands
@client.command(name = "resume")
async def resume(ctx):
    pass

@client.command(name = "pause")
async def pause(ctx):
    pass

@client.command(name = "skip")
async def skip(ctx):
    pass
        
@client.command(name = "leave") #Makes bot leave voice channel
async def leave(ctx):
    try:
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
        else:
            raise Exception("Bot is already disconnected from voice channel")
    except Exception as e:
        await ctx.send(e)

    
#Create a class to keep track of top countries, decades, and songs
@client.command(name = "top") #Pulls up list of top countries, decades, and songs
async def top(ctx, category):
    if category == "countries":
        pass
    elif category == "decades":
        pass
    elif category == "songs":
        pass
    else:
        try:
            raise Exception("Plase re-enter your command in the format '+top [category]', where the only valid terms for [category] are 'countries', 'decades', and 'songs'")
        except Exception as e:
            await ctx.send(e)


client.run('ODQ0Nzc1NTk3NDk4ODI2ODMy.YKXUlQ.sNQPt6p-yt0fvqoSvFtCs7rrBu0') 
