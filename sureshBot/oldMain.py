import discord
from discord.ext import commands
from suresh import Suresh
import datetime
import asyncio
from UsersReminders import UsersReminders
from pytz import timezone, utc
import random
import os

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# test = []
# commandSymbol = '!'
# default_channel = 945435626734518325
# important_channel = 947636842801541121
# index = 0


# async def time_check():
#     await bot.wait_until_ready()
#     print("working")
#     while True:
#         await asyncio.sleep(10)
#         # print("working in while loop")
#         now = datetime.datetime.now()
#         utc_time = datetime.datetime.utcnow()

#         pst_tz = timezone('US/Pacific')
#         pst_time = utc_time.replace(tzinfo=utc).astimezone(pst_tz)
#         PT = str(pst_time)
#         # print("TIME:" + PT)
#         time = PT[PT.find(" ")+1 : PT.find(" ")+6]
#         date = PT[0:PT.find(" ")]
#         # print("Hour: " + PT[PT.find(" ")+1 : PT.find(" ")+3])
#         # print("Minute: " + PT[PT.find(" ")+4 : PT.find(" ")+6])
#         # print("Time: " +time)
#         # print("Date: " +date)
#         for x in test:
#             if(date == x.date and time == x.time):
#                 # print("TIMEE")
#                 allowed_mentions = discord.AllowedMentions(everyone = True)
#                 await bot.get_channel(default_channel).send(content = "@everyone" + " " +x.message, allowed_mentions = allowed_mentions)
#                 test.remove(x)

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

# def numDay(dayNum):
#     if dayNum == 0:
#         return "Monday"
#     if dayNum == 1:
#         return "Tuesday"
#     if dayNum == 2:
#         return 'Wednesday'
#     if dayNum == 3:
#         return "Thursday"
#     if dayNum == 4:
#         return "Friday"
#     if dayNum == 5:
#         return "Saturday"
#     if dayNum == 6:
#         return "Sunday"

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
#     minute = date[date.find(':') + 1 : date.find(':') + 3]
#     minute = int(minute)

#     if minute > 59:
#         minute = 59
    
#     if minute < 0:
#         minute = 0

#     return minute

# def mesg (date):
#     msg = date[date.find("|") + 1:]
#     # print ("whole: " + date)
#     # print("message: " + msg)
#     return msg

# def date (reminder):
#     return reminder[reminder.find("{")+1 : reminder.find("}")]

# def time (reminder):
#     return reminder[reminder.find("[")+1 : reminder.find("]")]

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    msg = message.content
    foul_lang = ["shit", "fuck", "idiot", "stupid", "ass", "bitch", "wtf", "wth"]

    if message.author == bot.user:
        return
    
    # if any(word in msg for word in foul_lang):
    # f"{message.author.mention}"
    for word in foul_lang:
        if word in msg:
            await message.channel.send("Foul Language! ", reference=message)
    
    if message.author == bot.user:
        return

    # if message.content.startswith(commandSymbol + "channelid"):
    #     default_channel = int(message.content[11: len(message.content)]) #client.get_channel()
    #     print(message.content[11: len(message.content)])
    #     await message.channel.send('Channel set to: ' + str(default_channel))
    
    # if message.content.startswith(commandSymbol + 'ping'):
    #     await message.channel.send('Pinging {}'.format(message.author.mention))
    
   
    # if message.content.startswith(commandSymbol + 'showReminders'):
    #     rems = ""
    #     ix = 1
    #     if(len(test) == 0):
    #         await message.channel.send("No reminders in list")
    #     else:
    #         for x in test:
    #         #    for i in x.dates[datetime.datetime.today().weekday()]:
    #         #        rems += str(numDay(x.day)) + ' ' + str(i.hour) + ":" + str(i.minute) + " " + x.message + "\n"
    #             rems += str(ix) + ". Date: " + str(x.date) + ', Time: ' + str(x.time) + ', Message: ' + str(x.message) +'\n'
    #             ix += 1

    #         await message.channel.send(rems)
    
    # if message.content.startswith(commandSymbol + 'rmvReminder'):
    #     index = int(message.content[message.content.find(" "):])-1
    #     msg = test[index].message
    #     d = test[index].date
    #     t = test[index].time
    #     test.pop(index)
    #     await message.channel.send("Removed reminder: " + str(d) + " " + str(t) + " " + str(msg))

    # if message.content.startswith(commandSymbol + 'rem'):
    #     # if (day(message.content) == -1):
    #     #     await message.channel.send("Invalid day, please try again\n $rem day hour(24hr):minute")
    #     # elif not contains(test, message.author):
    #     # else:  
    #     if ("{" in message.content and "}" in message.content and "[" in message.content and "]" in message.content):
    #         test.append(UsersReminders(message.author))
    #         test[len(test)-1].addRem(date(message.content), time(message.content), mesg(message.content))

    #         await message.channel.send("{} Reminder Added".format(message.author.mention))
    #     else:
    #         await message.channel.send("Incorrect Format")
    #     # elif contains(test, message.author):

    #     #     test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), mesg(message.content))
    #     #     await message.channel.send("{} reminder added".format(message.author.mention))
    
    await bot.process_commands(message)

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Suresh(bot))

bot.loop.create_task(setup())
# bot.loop.create_task(time_check())
# bot.time_check().start()

with open("token.0", "r", encoding="utf-8") as f:
    TOKEN = f.read()
    bot.run(TOKEN)
