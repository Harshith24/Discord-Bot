import datetime
import discord

class UsersReminders:
    def __init__(self, messageauthor): #username
        # dates = {
        #     0 : monhours[], #monday
        #     1 : tuehours[], #tuesday
        #     2 : wedhours[], #wednesday
        #     3 : thuhours[], #thursday
        #     4 : frihours[], #friday
        #     5 : sathours[], #saturday
        #     6 : sunhours[] #sunday
        # }
        self.dates = dict.fromkeys(range(7), [])
        self.message = ""
        self.messageauthor = messageauthor
        print(self.dates)

    def add(self, day, hour, minute, message):
        self.dates[day].append(datetime.time(hour, minute))
        self.message = message
        self.day = day
        # print("Reminders class: " + message)





# import datetime
# import discord

# class UsersReminders:
#     def __init__(self, messageauthor): #username
#         # dates = {
#         #     0 : monhours[], #monday
#         #     1 : tuehours[], #tuesday
#         #     2 : wedhours[], #wednesday
#         #     3 : thuhours[], #thursday
#         #     4 : frihours[], #friday
#         #     5 : sathours[], #saturday
#         #     6 : sunhours[] #sunday
#         # }
#         self.dates = dict.fromkeys(range(7), [])
#         self.message = ""
#         self.messageauthor = messageauthor
#         print(self.dates)

#     def add(self, day, hour, minute, message):
#         self.dates[day].append(datetime.time(hour, minute))
#         self.message = message