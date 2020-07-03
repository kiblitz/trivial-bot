import discord
import random

import thanks_handler

async def check_thanks(author, message, channel, mentions):
  if message[0] != '!thanks':
    return False
  if len(message) == 2:
    message.append("")
  if (len(mentions) == 0 or 
     (message[1] != mentions[0].mention and
      message[1][:2] + message[1][3:] != mentions[0].mention)):
    await channel.send(thanks_mention_error(author))
    return True
  ty_msg = ' '.join(message[2:])
  thanks_handler.new_thanks(author.id, mentions[0].id, ty_msg)
  await channel.send(thanks_accepted(author, mentions[0]))
  return True 

def thanks_mention_error(author):
  possible = ["Make sure to include who you're thanking " + author.mention,
              "Not sure who that's directed to " + author.mention,
              "Who was that for " + author.mention + "?"] 
  return random.choice(possible)

def thanks_accepted(author, to):
  possible = ["Alright " + author.mention + ", your thanks to " + to.mention + " has been sent",
              "Thanks for thanking " + to.mention + ", " + author.mention + "!",
              "Wow " + to.mention + "! Looks like you received a thanks from " + author.mention + "!"]
  return random.choice(possible)

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')
    thanks_handler.connect()

  async def on_message(self, message):
    author = message.author
    if author.id == self.user.id:
      return

    msg_lst = message.content.split() 

    if len(msg_lst) == 0:
      return 

    if msg_lst[0][0] == '!':
      await check_thanks(author, msg_lst, message.channel, message.mentions)

TOKEN = open("../secret/SECRET_TOKEN").read()
client = MyClient()
client.run(TOKEN)
