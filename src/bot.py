import discord
import random

import thanks_handler

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


def show_empty_error(author):
  possible = ["Not sure what you're trying to show " + author.mention,
              "Make sure to specify what you want to show " + author.mention,
              "Show you what, " + author.mention + "?"] 
  return random.choice(possible)

def play_empty_error(author):
  possible = ["Not sure what you're trying to play " + author.mention,
              "Make sure to specify what you want to play " + author.mention,
              "What does " + author.mention + " want to play?"] 
  return random.choice(possible)

def rand_empty_error(author):
  possible = ["I'm going to need a non-empty list to choose from, " + author.mention,
              "Sorry " + author.mention + ", picking from an empty list is pretty non-trivial",
              "At least one element is needed " + author.mention] 
  return random.choice(possible)

def num_error(author):
  possible = ["Whoops! I was expecting a number " + author.mention,
              "Make sure to use numbers in your command " + author.mention,
              "Looks like I'm going to need a number instead " + author.mention] 
  return random.choice(possible)

def unknown_error(author):
  possible = ["Not sure I understood that keyword " + author.mention,
              "That doesn't seem to be part of my lexicon " + author.mention,
              "Sorry " + author.mention + ", I'm not sure what that means"]
  return random.choice(possible)

def unimplemented_error(author):
  possible = ["Sorry " + author.mention + ", that feature doesn't seem to be implemented yet",
              "Unfortunately, I haven't been taught how to do that " + author.mention,
              "Whoops, looks like you found a command I don't know how to process yet " + author.mention]
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
      if (await self.check_thanks(author, msg_lst, message.channel, message.mentions) or
          await self.check_show(author, msg_lst, message.channel, message.mentions) or
          await self.check_play(author, msg_lst, message.channel, message.mentions) or
          await self.check_coin(author, msg_lst, message.channel, message.mentions) or
          await self.check_roll(author, msg_lst, message.channel, message.mentions) or
          await self.check_rand(author, msg_lst, message.channel, message.mentions)):
        return
      await message.channel.send(unknown_error(author))

  async def check_thanks(self, author, message, channel, mentions):
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

  async def check_show(self, author, message, channel, mentions):
    if message[0] != '!show':
      return False 
    if len(message) == 1:
      await channel.send(show_empty_error(author)) 
      return True
    if ((not await self.show_thanks(author, message[1:], channel, mentions))):
      await channel.send(unknown_error(author))
    return True

  async def show_thanks(self, author, message, channel, mentions):
    if message[0] != 'thanks':
      return False
    if len(message) == 1:
      # TODO show your thanks
      await channel.send(unimplemented_error(author))
      return True

  async def check_play(self, author, message, channel, mentions):
    if message[0] != '!play':
      return False
    if len(message) == 1:
      await channel.send(play_empty_error(author)) 
      return True
    # TODO see check_show
    await channel.send(unimplemented_error(author))
    return True

  async def check_coin(self, author, message, channel, mentions):
    if message[0] != '!coin':
      return False
    await channel.send(random.choice(["Heads", "Tails"]) + " " + author.mention)
    return True

  async def check_roll(self, author, message, channel, mentions):
    if message[0] != '!roll':
      return False
    if len(message) == 1:
      sides = 6 
    else:
      try:
        sides = int(message[1]) 
      except:
        await channel.send(num_error(author))
        return True
    await channel.send(str(random.randint(1, sides)) + " " + author.mention)
    return True

  async def check_rand(self, author, message, channel, mentions):
    if message[0] != '!rand':
      return False
    if len(message) == 1:
      await channel.send(rand_empty_error(author))
      return True
    await channel.send(random.choice(message[1:]) + " " + author.mention)
    return True

TOKEN = open("../secret/SECRET_TOKEN").read()
client = MyClient()
client.run(TOKEN)
