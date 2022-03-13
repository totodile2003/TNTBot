import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
client = discord.Client()
from discord.ext.commands import Bot as BotBase
intents = discord.Intents.default()
intents.reactions = True
client = commands.Bot(command_prefix = '!' , intents = intents)
client.remove_command('help')
OWNER_IDS = [308710079325011970]
SERVER_ID = [837662074611040267]
class Bot(BotBase):
  def __init__(self):
    self.Guild = SERVER_ID

    super().__init__(owner_ids=OWNER_IDS)

  def run(self):
    pass

  async def on_connect(self):
    print("Bot Connected to server")

  async def on_ready(self):
    pass




@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="!help"))
    print("TNTBot is Online and Running")

#This posts a message in the server that tells users how to use the bot and what the commands do, This is a bot I set up for my freinds stream discord so that is why it links to all of his socials
@client.command()
async def help(ctx):
  await ctx.send("A user has requested help, this Bots Prefix is '!'\nCommands Available in TNTBot:\n1. ping - shows your latency to the server\n2. twitch - Puts a link to Patric's Twitch in the chat\n3. tiktok - Puts a link to Patric's TikTok in the chat\n4. instagram - Puts a link to Patric's Instagram in the chat\n5. twitter - Puts a link to Patric's Twitter in the chat\n6. youtube - Puts a link to Patric's YouTube in the chat\n7. smp - gives details on how to apply for the SMP")

  print("Setup Complete")

def run(self, version):
  self.version = version

#This command tells the user their current ping

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency * 1000)
    ))

#SMP Applicants
  #This sends a message to the user that typed the command and asks them to fill out the application form that is in the discord channel linked.

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def smp(ctx):
    await ctx.send("If you would like to join The Bomber SMP then fill out the google form in this channel: <#878751905503936533>.\n If you have already done this, then TNTBomb1164 will get round to looking at your application soon and he will message you telling you if you made it in.\n Good Luck!")


#Social Media Commands

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def youtube(ctx):
    await ctx.send("You can find Patric on youtube at TNTbomb1164 click this link to go to his page  https://www.youtube.com/channel/UC7WbdXeCzkTHW4We6qdraHw ")

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def twitch(ctx):
    await ctx.send("You can find Patric on twitch at TNTbomb1164 click this link to go to his page  https://www.twitch.tv/tntbomb1164 ")

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def tiktok(ctx):
    await ctx.send("Patric's tiktok is patricshipley_ click this link to go to his account  https://vm.tiktok.com/ZMdnwtB8Q/ ")

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def instagram(ctx):
    await ctx.send("Patric's instagram is patricshipley\_ here you can vote for what game will be played on the next stream on his stories, click this link to go to his page  https://www.instagram.com/patricshipley_")

@client.command()
@commands.cooldown(1,15,commands.BucketType.user)
async def twitter(ctx):
    await ctx.send("Patric's twitter is patricshipley\_ click this link to go to his account  https://twitter.com/patricshipley_ ")

#This commmand allows a moderator to delete a specified number of messages

@client.command()
@commands.has_role('Moderator',)
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount+1)

keep_alive()
client.run(os.environ['TOKEN'])
