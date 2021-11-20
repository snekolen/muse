# Muse

## Description
Muse is a Discord bot that sends an embed containing information about a song's title, artist, and release country and date based the user inputted country and decade.  The idea of this bot is inspired by Radiooooo.com, which uses a similar method to determine songs to play.  In other words, it's like Radiooooo but as a music library bot.  Additionally, Muse keeps track of the most searched terms and recently liked songs among all servers.  It is built using Discord's and various other APIs that will be described in its usage in a later section of this ReadME. \
**Language(s):** Python \
**Developer:** Helen Ma


## Usage
### Inviting to Server
The invite link for Muse is in the line below:\
```https://tinyurl.com/muse-bot```
#### Intructions:
1. Click the link above to get to the invite page of Muse.
2. Select the server you would like to invite Muse to.
<img src="https://i.imgur.com/lUXrmsT.png" alt="landing" width="414" height="896" />
3. Click authorize and follow proceeding steps.
<img src="https://i.imgur.com/Cm00s2c.png" alt="authentication" width="414" height="896" />
4. The bot can now be used in the server.
<img src="https://i.imgur.com/eJxFuKo.jpg" alt="server" width="414" height="404" /> 

### Commands
#### +list
```+list [decade]``` \
Sends a list of countries in the world by decade ranging from 1900 to 2020
#### +song
```+song [country] [decade]``` \
Sends a song released from the input country during the specified decade
(ex: +song Japan 1980)
#### +top
```+top terms``` \
Shows the top 3 most searched terms
```+top songs``` \
Shows the 3 most recently liked songs in the server
#### Error Handling
The program uses try-catch blocks where it outlines if/else statements to determine whether the input is valid.  In the try block, if the input is determined to be invalid, the program throws an error, which will be caught and sent as a regular message in Discord.

## Advanced
### APIs
#### Discord py
The Discord.py API provides a general framework for 
#### Musicbrainzngs
#### Unidecode
#### URL Lib and Re
### Classes
#### Cog
#### Menu
#### Music
#### Info

## Development 
### Shift in Purpose
### Testing Methods
### Troubleshooting

## Closing
