import discord

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'{self.user} has connected to Discord!')

  async def on_message(self, message):
    if message.author == self.user:
      return
    
    if message.content == 'ping':
      await message.channel.send('pong')
  
TOKEN = open("../secret/SECRET_TOKEN").read()
client = MyClient()
client.run(TOKEN)
