#Finds music from musicbrainz based on what the user entered (Maybe move it to countries.py)

import os
import musicbrainzngs
import random
import re
import urllib.request
from unidecode import unidecode


musicbrainzngs.set_useragent(os, "0.7.1") #Creates useragent

abbreviations = {"Afghanistan": "AF", "Albania": "AL", "Algeria": "DZ", "Angola": "AO", "Argentina": "AR", 
"Armenia": "AM", "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ", "Bahamas": "BS", 
"Bahrain": "BH", "Bangladesh": "BD", "Barbados": "BB", "Belarus": "BY", "Belgium": "BE", 
"Belize": "BZ", "Benin": "BJ", "Bhutan": "BT", "Bolivia": "BO", "Bosnia": "BA", "Brazil": "BR", 
"Bulgaria": "BG", "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA","Chad": "TD", 
"Chile": "CL", "China": "CN", "Colombia": "CO", "Congo": "CG", "Costa Rica": "CR", 
"Croatia": "HR", "Cuba": "CU", "Czech Republic": "CZ", "Czechoslovakia": "XC", "Denmark": "DK",  
"Dominican Republic": "DO", "Ecuador": "EC", "Egypt": "EG", "El Salvador": "SV", 
"Equatorial Guinea": "GQ", "Estonia": "EE", "Ethiopia": "ET", "Finland": "FI", "France": "FR", 
"Gabon": "GA", "Gambia": "GM", "Georgia": "GE", "Germany": "DE", "West Germany": "DE", 
"East Germany": "XG", "Ghana": "GH", "Greece": "GR", "Guatemala": "GT", "Guyana": "GY", 
"Haiti": "HT", "Honduras": "HN", "Hungary": "HU", "Iceland": "IS", "India": "IN", 
"Indonesia": "ID", "Iran": "IR", "Iraq": "IQ", "Ireland": "IE", "Israel": "IL", "Italy": "IT",
"Ivory Coast": "CI", "Jamaica": "JM", "Japan": "JP", "Jordan": "JO", "North Korea":"KP", "Lithuania": "LT", 
"South Korea":"KR","Madagascar": "MG", "Malaysia": "MY", "Malta": "MT", "Mexico": "MX", "Moldova": "MD", 
"Mongolia": "MN", "Morocco": "MA", "Myanmar": "MM", "Nepal": "NP", "Netherlands": "NL", 
"New Zealand": "NZ", "Nicaragua": "NI", "Niger": "NE", "Nigeria": "NG", "Norway": "NO", 
"Pakistan": "PK", "Panama": "PA", "Paraguay": "PY", "Peru": "PE", "Philippines": "PH", 
"Poland": "PL", "Portugal": "PT", "Romania": "RO", "Russia": "RU", "Rwanda": "RW", 
"Saudi Arabia": "SA", "Senegal": "SN", "Serbia": "RS", "Singapore": "SG", "Slovakia": "SK", 
"Slovenia": "SI", "Somalia": "SO", "South Africa": "ZA", "Soviet Union": "SU", "Spain": "ES",  
"Sri Lanka": "LK", "Sudan": "SD", "Suriname": "SR", "Swaziland": "SZ", "Sweden": "SE", 
"Switzerland": "CH", "Syria": "SY", "Taiwan": "TW", "Tajikistan": "TJ", "Tanzania": "TZ", 
"Thailand": "TH", "Trinidad and Tobago": "TT", "Tunisia": "TN", "Turkey": "TR", 
"Turkmenistan": "TM", "Uganda": "UG", "Ukraine": "UA", "UAE": "AE", "United Kingdom": "GB", 
"United States": "US", "Uruguay": "UY", "Uzbekistan": "UZ", "Venezuela": "VE", "Vietnam": "VN", 
"Yugoslavia": "YU", "Zimbabwe": "ZW", "Laos": "LA", "Kazakhstan": "KZ", "Lebanon": "LB"}

searchLink = "https://www.youtube.com/results?search_query="
watchLink = "https://www.youtube.com/" #Includes watch? after


def findSong(country, year): #Finds songs on musicbrainz and returns them
    lastYear = year
    if year == 2020: #Use random function to generate no.
        lastYear += 2
    else: 
        lastYear += 9
    yearVal = random.randint(year, lastYear)
    songsArr = musicbrainzngs.search_releases(country = abbreviations[country], date = yearVal, type = "Single")
    indexVal = random.randint(0, len(songsArr["release-list"]) - 1)
    songInfo = songsArr["release-list"][indexVal]
    
    songName = songInfo["title"]
    artistName = songInfo["artist-credit"][0]["name"]
    yearReleased = songInfo["date"][0:4]
    songDict = {"Song": songName, "Artist": artistName, "Year": yearReleased}
    return songDict


def findUrl(songDict): #Passes in a dictionary
    searchLink = "https://www.youtube.com/results?search_query="
    watchLink = "https://www.youtube.com/watch?v=" #Includes watch? after
    
    #Romanize and convert to ascii
    searchTerm = unidecode(songDict["Song"]) + " " + unidecode(songDict["Artist"])
    searchTerm = "+".join(searchTerm.split(" "))
    searchLink += searchTerm
    
    html = urllib.request.urlopen(searchLink)
    vidIDs = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    watchLink += vidIDs[0]
    songDict["URL"] = watchLink
    songDict["ID"] = vidIDs[0]
    return songDict




