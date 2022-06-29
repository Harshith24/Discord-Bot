import discord
import threading
import time
import datetime
import asyncio
from UsersReminders import UsersReminders
#from discord.ext import commands

test = []
client = discord.Client()
commandSymbol = '!'
default_channel = 945435626734518325
index = 0


async def time_check():
    await client.wait_until_ready()
    #print("working")
    while True:
        await asyncio.sleep(10)
        #print("working")
        now = datetime.datetime.now()
        for x in test:
            for i in x.dates[datetime.datetime.today().weekday()]:
                # print("hour: " + str(now.hour) + " minute: " + str(now.minute))
                # print("i hour: " + str(i.hour) + " i minnute: " + str(i.minute))
                if now.hour == i.hour and now.minute == i.minute:
                    # print("TIMEEE")
                    #print(now.hour == i.hour)
                    await client.get_channel(default_channel).send(x.messageauthor.mention + " " +x.message)
                    test.remove(x)

def contains(test, messageauthor):
    for x in test:    
        if x.messageauthor == messageauthor:
            return True
    return False

def day(date): #!add monday 14
    day = date[date.find(' ') + 1: date.find(' ', 5)]
    day = day.upper()

    if day == "MONDAY":
        return 0
    if day == "TUESDAY":
        return 1
    if day == "WEDNESDAY":
        return 2
    if day == "THURSDAY":
        return 3
    if day == "FRIDAY":
        return 4
    if day == "SATURDAY":
        return 5
    if day == "SUNDAY":
        return 6
    
    return -1

def numDay(dayNum):
    if dayNum == 0:
        return "Monday"
    if dayNum == 1:
        return "Tuesday"
    if dayNum == 2:
        return 'Wednesday'
    if dayNum == 3:
        return "Thursday"
    if dayNum == 4:
        return "Friday"
    if dayNum == 5:
        return "Saturday"
    if dayNum == 6:
        return "Sunday"

def hour(date):
    print(date[date.find(' ', 5) + 1 : ])
    hour = date[date.find(' ', 5) + 1 : date.find(':')]
    hour = int(hour)
    if hour > 23:
        hour = 23
    
    if hour < 0:
        hour = 0

    return hour

def minute(date):
    minute = date[date.find(':') + 1 : date.find(':') + 3]
    minute = int(minute)

    if minute > 59:
        minute = 59
    
    if minute < 0:
        minute = 0

    return minute

def mesg (date):
    msg = date[date.find("|") + 1:]
    # print ("whole: " + date)
    # print("message: " + msg)
    return msg
    


# thread = threading.Thread(target = check_time, args = ())
# thread.start()

@client.event
async def on_ready():
    print('Bot is ready.')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(commandSymbol + "channelid"):
        default_channel = int(message.content[11: len(message.content)]) #client.get_channel()
        print(message.content[11: len(message.content)])
        await message.channel.send('Channel set to: ' + str(default_channel))
    
    if message.content.startswith(commandSymbol + 'ping'):
        await message.channel.send('Pinging {}'.format(message.author.mention))
    
    if message.content.startswith(commandSymbol + 'showReminders'):
        rems = ""
        for x in test:
           for i in x.dates[datetime.datetime.today().weekday()]:
               rems += str(numDay(x.day)) + ' ' + str(i.hour) + ":" + str(i.minute) + " " + x.message + "\n"
        
        await message.channel.send(rems)

    if message.content.startswith(commandSymbol + 'rem'):
        if (day(message.content) == -1):
            await message.channel.send("Invalid day, please try again\n $rem day hour(24hr):minute")
        # elif not contains(test, message.author):
        else:    
            test.append(UsersReminders(message.author))
            test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), mesg(message.content))

            await message.channel.send("{} Reminder Added".format(message.author.mention))
        # elif contains(test, message.author):

        #     test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), mesg(message.content))
        #     await message.channel.send("{} reminder added".format(message.author.mention))
        



    
client.loop.create_task(time_check())
client.run('OTQ1NDMzMjY2NTE5OTUzNDA4.YhQFWA.F8zOuJie4zIRK46h7xaAgjnPpdo')

# import discord
# import threading
# import time
# import datetime
# import asyncio
# from UsersReminders import UsersReminders
# #from discord.ext import commands

# test = []
# client = discord.Client()
# commandSymbol = '!'
# default_channel = 945435626734518325
# index = 0


# async def time_check():
#     await client.wait_until_ready()
#     #print("working")
#     while True:
#         await asyncio.sleep(40)
#         #print("working")
#         now = datetime.datetime.now()
#         for x in test:
#             for i in x.dates[datetime.datetime.today().weekday()]:
#                 if now.hour == i.hour and now.minute == i.minute:
#                     #print(now.hour == i.hour)
#                     await client.get_channel(default_channel).send("{} time for class".format(x.messageauthor.mention))
#                     # ("{} time for class".format(x.messageauthor.mention))

# def contains(test, messageauthor):
#     for x in test:    
#         if x.messageauthor == messageauthor:
#             return True
#     return False

# def day(date): #!add monday 14
#     day = date[date.find(' ') + 1: date.find(' ', 5)]
#     day = day.upper()

#     if day == "MONDAY":
#         return 0
#     if day == "TUESDAY":
#         return 1
#     if day == "WEDNESDAY":
#         return 2
#     if day == "THURSDAY":
#         return 3
#     if day == "FRIDAY":
#         return 4
#     if day == "SATURDAY":
#         return 5
#     if day == "SUNDAY":
#         return 6
    
#     return -1

# def hour(date):
#     print(date[date.find(' ', 5) + 1 : ])
#     hour = date[date.find(' ', 5) + 1 : date.find(':')]
#     hour = int(hour)
#     if hour > 23:
#         hour = 23
    
#     if hour < 0:
#         hour = 0

#     return hour

# def minute(date):
#     minute = date[date.find(':') + 1 : date.find(':') + 2]
#     minute = int(minute)

#     if minute > 59:
#         minute = 59
    
#     if minute < 0:
#         minute = 0

#     return minute

# def mesg (date):
#     msg = date[date.find("`") + 1:]
#     print ("whole: " + date)
#     print("message: " + msg)
#     return msg
    


# # thread = threading.Thread(target = check_time, args = ())
# # thread.start()

# @client.event
# async def on_ready():
#     print('Bot is ready.')
    

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith(commandSymbol + "channelid"):
#         default_channel = int(message.content[11: len(message.content)]) #client.get_channel()
#         print(message.content[11: len(message.content)])
#         await message.channel.send('Channel set to: ' + str(default_channel))
    
#     if message.content.startswith(commandSymbol + 'ping'):
#         await message.channel.send('Pinging {}'.format(message.author.mention))

#     if message.content.startswith(commandSymbol + 'add'):
#         if (day(message.content) == -1):
#             await message.channel.send("Invalid day, please try again\n $add day hour(24hr):minute")
#         elif not contains(test, message.author):
            
#             test.append(UsersReminders(message.author))
#             test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), "test maesage")

#             await message.channel.send("{} reminder added".format(message.author.mention))
#         elif contains(test, message.author):

#             test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), "test message")
#             await message.channel.send("{} reminder added".format(message.author.mention))
        



    
# client.loop.create_task(time_check())
# client.run('OTQ1NDMzMjY2NTE5OTUzNDA4.YhQFWA.F8zOuJie4zIRK46h7xaAgjnPpdo')