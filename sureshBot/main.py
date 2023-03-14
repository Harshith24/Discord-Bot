import discord
from discord.ext import commands
from suresh import Suresh

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command = None)
important_test = 947636842801541121

important = 830272182977953792
carpooling = 900201162609934366
secret_siblings = 948485530490900561

Varsity_match_recaps = 830271872963969065
JV_match_recaps = 948068096793522206

general = 830260998858211400
varsity_general = 939617416693039124
JV_general = 939615948313333761

carpool_lineups = 900201052207452170

badminton_emoji = "🏸"
car_emoji = "🚙"
important_emoji = "‼️"

@bot.event
async def on_ready():
    print(f"{bot.user.name} is ready")

@bot.event
async def on_message(message):
    msg = message.content
    sg = message.content
    foul_lang = ["shit", "fuck", "idiot", "stupid", "ass", "bitch", "wtf", "wth"]

    if(message.channel.id == important):
        await message.add_reaction(important_emoji)
    elif (message.channel.id == carpooling):
        await message.add_reaction(car_emoji)
    
        # if any(word in msg for word in foul_lang):
        # f"{message.author.mention}"
        # for word in foul_lang:
        #     if word in msg:
        #         await message.channel.send("Foul Language! ", reference=message)

    elif(message.channel.id == Varsity_match_recaps or message.channel.id == JV_match_recaps):
        await message.add_reaction(badminton_emoji)
    
    
    await bot.process_commands(message)

async def setup():
    await bot.wait_until_ready()
    bot.add_cog(Suresh(bot))

# async def create_db_pool():
#     bot.pg_con = await asyncpg.create_pool(database="badminton", user="postgres", password="Zaq1xsw@")

bot.loop.create_task(setup())
# bot.loop.run_until_complete(create_db_pool())

with open("token.0", "r", encoding="utf-8") as f:
    TOKEN = f.read()
    bot.run(TOKEN)
