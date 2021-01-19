import discord, os
from discord.ext import commands
from gameFunctions import *

client = discord.Client() #connection to discord

@client.event #register an event
async def on_ready():
    print("Gamble Bot is online!")
    await client.change_presence(activity=discord.Game(name="Made by Hemzyy. '$help'"))


@client.event #second event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('$help'):
        await message.channel.send("Type '$balance' to check your balance\nType '$bet [amount] [h or t]' to bet\ntype '$rewards' to see rewards available to redeem")

    if message.content == ('$rewards'):
        with open('rewards.txt') as f:
            file = f.read()
        await message.channel.send(file)

    if message.content.startswith('$bet'): #Basically the whole point of this bot
        msg = message.content.split(' ', 2)
        arg = msg[1]
        prediction = msg[2]
        sender = message.author

        if isNewPlayer(str(sender)):
            addPlayer(str(sender))
            await message.channel.send('You have been added to the players list with a balance of 50 points.')
        else:
            if (enoughBalance(str(sender), int(arg))):
                removePoints(str(sender), int(arg))
                if isEqual(str(prediction)):
                    addPoints(str(sender), int(arg)*2)
                    await message.channel.send('Congrats, you won double your bet!')
                else:
                    await message.channel.send('You lost.')
            else:
                await message.channel.send('You don\'t have enough points.')
                
    if message.content == ('$balance'):
        sender = message.author
        if isNewPlayer(str(sender)):
            addPlayer(str(sender))
            await message.channel.send('You have been added to the players list with a balance of 50 points.')
        await message.channel.send('<@'+ str(message.author.id)+'>, '+ checkBalance(str(sender)))
                    


        
    '''
    if message.content == ("nik mok"):
        await message.channel.send("ou yemak")

    if message.content == "n7abek ghiles":
        await message.channel.send("ok")
    '''


client.run(TOKEN)
