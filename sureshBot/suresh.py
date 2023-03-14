from cgitb import reset
from pydoc import describe
from re import L
import discord
import asyncio
import youtube_dl
from UsersReminders import UsersReminders
from pytz import timezone, utc
import random
from discord.ext.commands import has_permissions
from discord.ext import commands, tasks
from discord.utils import get
import datetime
from datetime import timedelta 
from googleapiclient.discovery import build
from google.oauth2 import service_account

numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
test = []
matches = []

general_test = 945435626734518325
important_test = 947636842801541121

important = 830272182977953792
carpooling = 900201162609934366
secret_siblings = 948485530490900561

Varsity_match_recaps = 830271872963969065
JV_match_recaps = 948068096793522206

general = 830260998858211400
varsity_general = 939617416693039124
jv_general = 939615948313333761

newark_26th = 948831954646757416
irvington_19th = 948831611326201906

carpool_lineups = 900201052207452170
jv = 900201761862713385
bot_commands = 953030205038022656
cpts = 830291934714265600
coaches = 936134261952614450

badminton_emoji = "🏸"
car_emoji = "🚙"
important_emoji = "‼️"


class Suresh(commands.Cog):
    client = None
    def __init__(self, bot):
        self.bot = bot
        client = bot
        client.loop.create_task(self.time_check())
        self.song_queue = {}
        self.setup()


        self.SERVICE_ACCOUNT_FILE = 'keys.json'

        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.credentials = None
        self.credentials = service_account.Credentials.from_service_account_file(
                self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)


        # The ID and range of a sample spreadsheet.
        self.spreadsheetID = '1UOOxF2GZFDZNJh56ggyPGrZDiqoR4AZHErOCV0dvatA'


        self.service = build('sheets', 'v4', credentials=self.credentials)

        # Call the Sheets API
        self.sheet = self.service.spreadsheets()
       

    def setup(self):
        for guild in self.bot.guilds:
            self.song_queue[guild.id] = []

    @commands.command()
    async def checkStatus(self, ctx):
        if(ctx.message.channel.id == bot_commands):
            await ctx.send("remote: -----> Installing requirements with pip \n" + 
                            "remote: -----> Discovering process types \n" +
                            "remote:        Procfile declares types -> worker \n" +
                            "remote: \n" +
                            "remote: -----> Compressing... \n" +
                            "remote:        Done: 71.5M \n" +
                            "remote: -----> Launching... \n" +
                            "remote:        Released v28 \n" +
                            "remote:        https://suresh-bot.herokuapp.com/ deployed to Heroku \n" +
                            "remote: \n" +
                            "remote: Verifying deploy... done. \n" +
                            "To https://git.heroku.com/suresh-bot.git \n" +
                            "d843865..ac76e3d  HEAD -> master \n" 
                            )
        

    @commands.command()
    async def sureshIntro(self, ctx):
        if(ctx.message.channel.id == bot_commands):
            await ctx.send("{} Hi! I can keep track of reminders for you and conduct polls.".format(ctx.author.mention))
       
    @commands.command()
    async def help(self, ctx):
        if(ctx.message.channel.id == bot_commands):
            await ctx.send("!addReminder 'channel' 'date' 'time' 'message' \n"
                            "!showReminders will show current reminders \n"
                            "!removeReminder 'index' *first use !showReminders to see the indexes of each reminder \n"
                            "!poll 'channel' 'how long will poll last for?' 'Question' list of options(if an option is 2 words, seperate with hyphen NOT SPACE) ")

    @commands.command()
    async def motivate(self, ctx):
        # response = requests.get('https://zenquotes.io/api/random')
        # json_data = json.loads(response.text)
        # quote = json_data[0]['q'] + " -" + json_data[0]['a']
        quote_dict = {
            "The only one who can tell you that you can't win is you and you don't have to listen" : "    -Jessica Ennis-Hill",
            "Never say never because limits, like fears, are often just illusions" : "    -Michael Jordan", 
            "Hard work beats talent when talent doesnt work hard" : "    -Tim Notke",
            "If my mind can concieve it and my heart can believe it - then I can achieve it" : "    -Muhammad Ali"
        }
        quote = random.choice(list(quote_dict))
        author = quote_dict.get(quote)
        await ctx.send(quote + author)
    
    @commands.command()
    async def testPing(self, ctx):
        await self.bot.get_channel(important_test).send(self.bot.get_channel(important_test).mention)

    @commands.command()
    async def poll(self, ctx, chn, time, question, *options):
        if (len(options)>10):
            await ctx.send("you can only have 9 options")
        else:
            channel = carpool_lineups
            if (chn == "important"):
                channel = important
            elif (chn == "general"):
                channel = general
            elif (chn == "Varsity-match-recaps"):
                channel = Varsity_match_recaps
            elif (chn == "secret-siblings"):
                channel = secret_siblings
            elif (chn == "JV-match-recaps"):
                channel = JV_match_recaps
            elif (chn == "varsity-general"):
                channel = varsity_general
            elif (chn == "jv-general"):
                channel = jv_general
            elif (chn == "carpooling"):
                channel = carpooling
            elif (chn == "bot-commands"):
                channel = bot_commands
            elif (chn == "jv"):
                channel = jv
            elif (chn == "cpts"):
                channel = cpts
            elif (chn == "newark-26th"):
                channel = newark_26th
            elif (chn == "irvington-19th"):
                channel = irvington_19th
            elif (chn == "coaches"):
                channel = coaches
            
            embed = discord.Embed(title="Poll", description=question, color=discord.Color.blue(), timestamp = datetime.datetime.utcnow())
            if(int(time)<61):
                fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False), ("instructions", "React to cast a vote! Voting ends in " + str(time) + " minutes", False)]
            elif (int(time)>60):
                t = int(time)/60
                fields = [("Options", "\n".join([f"{numbers[idx]} {option}" for idx, option in enumerate(options)]), False), ("instructions", "React to cast a vote! Voting ends in " + str(t) + " hours", False)]

            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)

            # message = await ctx.send(embed=embed)
            message = await self.bot.get_channel(channel).send(embed=embed)
            poll_id = message.id

            for emoji in numbers[:len(options)]:
                await message.add_reaction(emoji)
            
            await asyncio.sleep(int(time)*60)

            poll_msg = await self.bot.get_channel(channel).fetch_message(poll_id)
            
            numbers_votes = {"1️⃣":0,"2️⃣":0,"3️⃣":0,"4️⃣":0,"5️⃣":0,"6️⃣":0,"7️⃣":0,"8️⃣":0,"9️⃣":0}
            
            for reaction in poll_msg.reactions:
                if reaction.emoji in numbers:
                    async for user in reaction.users():
                        # if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        numbers_votes[reaction.emoji] += 1

                        # reacted.append(user.id)
            
            largest = 1
            tie = False
            tieIndexes = []
            idx = -1
            for r in range(len(options)):
                # print(r)
                if(largest < list(numbers_votes.values())[r]):
                    tie = False
                    largest = list(numbers_votes.values())[r]
                    idx = r
                    tieIndexes.clear()
                    tieIndexes.append(idx)
                    # print("largest: " + str(largest))
                    # print("idx: " + str(idx))
                    # if(len(tieIndexes)>1):
                    #     tieIndexes.clear()
                    #     tie = False
                elif (largest == list(numbers_votes.values())[r]):
                    tieIndexes.append(r)
                    tie = True
            if(idx != -1 and tie == False):
                # await ctx.send("Most votes for: " + options[idx])  
                embed = discord.Embed(title="Most votes for: " + options[idx] + " (" + str(list(numbers_votes.values())[idx]) + ")", description=question + ". Voting has ended!", color=discord.Color.blue())
                # await poll_msg.clear_reactions()
                await poll_msg.edit(embed=embed)
                # await self.bot.get_channel(channel).send("hiiiii")
            elif(idx != -1 and tie == True):
                tieVals = ""
                for i in range(len(tieIndexes)):
                    if(i == len(tieIndexes)-1):
                        tieVals += str(options[tieIndexes[i]])
                    else:
                        tieVals += str(options[tieIndexes[i]]) + ", "
                embed = discord.Embed(title="There will be a re-vote. Tie for: " + tieVals + " (" + str(list(numbers_votes.values())[tieIndexes[0]]) + ")", description=question, color=discord.Color.blue())
                # await self.bot.get_channel(channel).send(embed=embed)
                await poll_msg.edit(embed=embed)
            else:
                embed = discord.Embed(title="Voting Ended", description = question, color=discord.Color.blue())
                await self.bot.get_channel(channel).send(embed = embed)   

    @commands.command()
    async def showReminders(self, ctx):
        rems = ""
        ix = 1
        reminders = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_reminders!A2:D").execute()
        reminders = reminders.get('values', [])
        test = reminders
        # print(test)
        if(len(test[0]) == 0):
            await ctx.send("No reminders in list")
        else:
            for x in test:
            #    for i in x.dates[datetime.datetime.today().weekday()]:
            #        rems += str(numDay(x.day)) + ' ' + str(i.hour) + ":" + str(i.minute) + " " + x.message + "\n"
                rems += str(ix) + ". Date: " + str(x[1]) + ', Time: ' + str(x[2]) + ", channel: " + str(x[0]) + ', Message: ' + str(x[3]) +'\n'
                ix += 1

            await ctx.send(rems)
    
    @commands.command()
    async def removeReminder(self, ctx, i): 
        try:   
            reminders = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_reminders!A2:D").execute()
            reminders = reminders.get('values', [])
            test = reminders
            index = int(i) -1
            msg = test[index][3]
            d = test[index][1]
            t = test[index][2]
            chn = test[index][0]
            delete = self.service.spreadsheets().values().clear(spreadsheetId=self.spreadsheetID, range="bot_reminders!A{}:D{}".format(index+2,index+2), body={}).execute()
            # test.pop(index)
            await ctx.send("Removed reminder: " + str(d) + " " + str(t) + " " + str(msg) + " " + str(chn))
        except(IndexError):
            await ctx.send("no such index")

    @commands.command()
    async def addReminder(self, ctx, channel, date, time, message): 
        if (":" not in date):
            # test.append(UsersReminders(ctx.message.author))
            # test[len(test)-1].addRem(channel, date, time, message)
            nextRow = 2
            vals = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_reminders!A2:A").execute()
            # print(vals)
            nextRow = len(vals.get('values',[])) + 2
            # print(nextRow)
            request = self.sheet.values().update(spreadsheetId=self.spreadsheetID, range="bot_reminders!A{}".format(nextRow), valueInputOption="USER_ENTERED", body={"values":[[channel, date, time, message]]}).execute()

            await ctx.send("{} Reminder Added".format(ctx.author.mention))
        else:
            await ctx.send("Incorrect Format")
        # elif contains(test, message.author):

        #     test[len(test) - 1].add(day(message.content), hour(message.content), minute(message.content), mesg(message.content))
        #     await message.channel.send("{} reminder added".format(message.author.mention))
    
    async def time_check(self):
        await self.bot.wait_until_ready()
        print("working")
        away_game_reminder = "Those who are giving a ride pls make a gc and give them info about what time and place to meet up. Reminder that you have to be there around 3:30, so please plan accordingly. Everyone else who is getting a carpool with someone else, please look out for discord friend requests so you can be added into a gc with that information!"
        weekly_active = False
        # practiceDays = []
        # weeklyPracticeReminders = []
        while True:
            reminders = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_reminders!A2:D").execute()
            reminders = reminders.get('values', [])
            test = reminders

            result = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_matches!A2:F30").execute()
            values = result.get('values', [])
            matches = values
           
            # practices = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!A2:G6").execute()
            # practices = practices.get('values',[])
            # for i in practices:
            #     practiceDays.append(str(i[0]).replace(" ", "").upper())

            weekPractices = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!A2:G2").execute()
            weekPractices = weekPractices.get('values',[])
            weeklyPracticeReminderDay = weekPractices[0][0]
            # for i in weekPractices:
            #     weeklyPracticeReminders.append(str(i[0]).replace(" ", "").upper())

            # varsity_start_time = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!B2").execute()
            # varsity_start_time = varsity_start_time.get('values',[])[0][0]
            # varsity_end_time = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!B3").execute()
            # varsity_end_time = varsity_end_time.get('values',[])[0][0]
            # JV_start_time = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!C2").execute()
            # JV_start_time = JV_start_time.get('values',[])[0][0]
            # JV_end_time = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!C3").execute()
            # JV_end_time = JV_end_time.get('values',[])[0][0]
            varsity_start_time = weekPractices[0][1]
            varsity_end_time = weekPractices[0][2]
            JV_start_time = weekPractices[0][3]
            JV_end_time = weekPractices[0][4]
            
            weeklyReminderTimeSend = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!F2").execute().get('values', [])[0][0]
            weekly_active_status = self.sheet.values().get(spreadsheetId=self.spreadsheetID, range="bot_practices!G2").execute()
            weekly_active_status = weekly_active_status.get('values', [])[0][0]
            if(weekly_active_status == 'TRUE'):
                weekly_active = True
            elif(weekly_active_status == 'FALSE'):
                # print("practice reminders not active")
                weekly_active = False

            # print("working in while loop")
            dates = {
                "0" : "monday",
                "1" : "tuesday",
                "2" : "wednesday",
                "3" : "thursday",
                "4" : "friday",
                "5" : "saturday",
                "6" : "sunday"
            }
            utc_time = datetime.datetime.utcnow()

            pst_tz = timezone('US/Pacific')
            pst_time = utc_time.replace(tzinfo=utc).astimezone(pst_tz)
            now = datetime.datetime.now(tz = pst_tz)
            day = str(timedelta(days=now.weekday()))[0:1]

            allowed_mentions = discord.AllowedMentions(everyone = True)

            PT = str(pst_time)
            # print("TIME:" + PT)
            time = PT[PT.find(" ")+1 : PT.find(" ")+6]
            date = PT[0:PT.find(" ")]
            # print("Hour: " + PT[PT.find(" ")+1 : PT.find(" ")+3])
            # print("Minute: " + PT[PT.find(" ")+4 : PT.find(" ")+6])
            # print("Time: " +time)
            # print("Date: " +date)

            for x in test:
                if(date == x[1] and time == x[2]):
                    # print("TIMEE")
                    channel = bot_commands
                    if (x[0] == "important"):
                        channel = important
                    elif (x[0] == "general"):
                        channel = general
                    elif (x[0] == "Varsity-match-recaps"):
                        channel = Varsity_match_recaps
                    elif (x[0] == "secret-siblings"):
                        channel = secret_siblings
                    elif (x[0] == "JV-match-recaps"):
                        channel = JV_match_recaps
                    elif (x[0] == "varsity-general"):
                        channel = varsity_general
                    elif (x[0] == "jv-general"):
                        channel = jv_general
                    elif (x[0] == "carpooling"):
                        channel = carpooling
                    elif (x[0] == "jv"):
                        channel = jv
                    elif (x[0] == "cpts"):
                        channel = cpts
                    elif (x[0] == "newark-26th"):
                        channel = newark_26th
                    elif (x[0] == "irvington-19th"):
                        channel = irvington_19th
                    elif (x[0] == "bot-commands"):
                        channel = bot_commands
                    elif (x[0] == "coaches"):
                        channel = coaches
                    elif (x[0] == "general-test"):
                        channel = general_test

                    # print(x.channel)
                    await self.bot.get_channel(channel).send(content = "@everyone" + " " +x[3], allowed_mentions = allowed_mentions)
                    test.remove(x)

            if(weekly_active):
                for i in range(len(list(dates.keys()))):
                    # print("1. " + str(day).upper() + " " + list(dates.keys())[i].upper())
                    if str(day).upper() == list(dates.keys())[i].upper():
                        days = list(dates.values())
                        # print(str(days[i].upper()))
                        # print("practice dyas: "+practiceDays[0])
                        if(str(days[i].upper()) == str(weeklyPracticeReminderDay).upper()):
                            if(str(time) == weeklyReminderTimeSend):
                                print("TIME Confirmed Practice")
                                await self.bot.get_channel(varsity_general).send(content = "@everyone" + " Reminder Varsity practice today from " + str(varsity_start_time) + " to " + str(varsity_end_time), allowed_mentions = allowed_mentions)
                                await self.bot.get_channel(jv_general).send(content = "@everyone" + " Reminder JV practice today from " + str(JV_start_time) + " to " + str(JV_end_time), allowed_mentions = allowed_mentions)
                                # saturday = True
                                # await asyncio.sleep(30)

            for x in matches:
                if(date == x[2]):
                    # print("date: " + date + "\n sheet data: " + x[2])
                    rd = 0
                    if(str(time) == x[4]):
                        if(x[5] != "NONE"): 
                            rd = x[5]
                        if(x[1] == "TRUE"):
                            if(rd == 0):
                                rd = away_game_reminder
                            await self.bot.get_channel(carpooling).send(content = "@everyone" + " " + "Reminder: away game today against " + x[0] + ". Early Dismissal is at " + x[3] + "PM. " + rd, allowed_mentions = allowed_mentions)
                        elif(x[1] == 'FALSE'):
                            if rd == 0:
                                rd = "Please be at the field house by 3:10 to help set up and sweep the courts. Good luck!"
                            await self.bot.get_channel(important).send(content = "@everyone" + " " + "Reminder: home game today against " + x[0] + ". Early dismissal is at " + x[3] + "PM. " + rd, allowed_mentions = allowed_mentions)
                        # await asyncio.sleep(30)

            # if(str(time) == "17:59"):
            # print("timeee: " + str(time))
            await asyncio.sleep(60)

        #NEXT STEP SHOULD BE TO TRY TO GET ROLES
       
            