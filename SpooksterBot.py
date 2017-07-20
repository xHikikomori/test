import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

Client = discord.Client()
bot_prefix= "/"
client = commands.Bot(command_prefix=bot_prefix)


@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))


    #Posts a greeting in general indicating the bot is online
    rnd = randint(1, 30)
    if rnd is 1:
        await client.send_message(discord.Object(id='337028246413639685'), 'k den')

    elif rnd is 2:
        await client.send_message(discord.Object(id='337028246413639685'), 'Hello')

    elif rnd is 3:
        await client.send_message(discord.Object(id='337028246413639685'), 'woh')

    elif rnd is 4:
        await client.send_message(discord.Object(id='337028246413639685'), '"I remember when I was 17" - Chris Imhoff')

    elif rnd is 5:
        await client.send_message(discord.Object(id='337028246413639685'), 'Epic!')

    elif rnd is 6:
        await client.send_message(discord.Object(id='337028246413639685'), "Jed you're still kicked out of the spooksters")

    elif rnd is 7:
        await client.send_message(discord.Object(id='337028246413639685'), 'k den')

    elif rnd is 8:
        await client.send_message(discord.Object(id='337028246413639685'), "Creamed Cabbage and Toilah are raging homosexuals, don't get too close!")

    elif rnd is 9:
        await client.send_message(discord.Object(id='337028246413639685'), '42 Maxwell St, Monavale')

    elif rnd is 10:
        await client.send_message(discord.Object(id='337028246413639685'), 'Send LEWDS!')

    elif rnd is 11:
        await client.send_message(discord.Object(id='337028246413639685'), 'xd')

    elif rnd is 12:
        await client.send_message(discord.Object(id='337028246413639685'), 'yeet')

    elif rnd is 13:
        await client.send_message(discord.Object(id='337028246413639685'), "It's 6ft at the green tides today!")

    elif rnd is 14:
        await client.send_message(discord.Object(id='337028246413639685'), 'Frantic Gecko has small man syndrome')

    elif rnd is 15:
        await client.send_message(discord.Object(id='337028246413639685'), 'Daily reminder that harlem shake videos are still being uploaded to youtube')

    elif rnd is 16:
        await client.send_message(discord.Object(id='337028246413639685'), 'rawr xd')

    elif rnd is 17:
        await client.send_message(discord.Object(id='337028246413639685'), 'I love Hayley')

    elif rnd is 18:
        await client.send_message(discord.Object(id='337028246413639685'), 'Flat is justice!')

    elif rnd is 19:
        await client.send_message(discord.Object(id='337028246413639685'), 'Illya is best loli!')

    elif rnd is 20:
        await client.send_message(discord.Object(id='337028246413639685'), 'Hikikomori was a mod+ on raidforums, be careful or he will HACK you')

    elif rnd is 21:
        await client.send_message(discord.Object(id='337028246413639685'), 'Sneaky Squid enjoys being fem dommed by his gf')

    elif rnd is 22:
        await client.send_message(discord.Object(id='337028246413639685'), 'Spacial is dating a man *bangs table*')

    elif rnd is 23:
        await client.send_message(discord.Object(id='337028246413639685'), 'James™ is da bong lord')

    elif rnd is 24:
        await client.send_message(discord.Object(id='337028246413639685'), 'haha weed!')

    elif rnd is 25:
        await client.send_message(discord.Object(id='337028246413639685'), 'Traps are not gay!')

    elif rnd is 26:
        await client.send_message(discord.Object(id='337028246413639685'), "RIP Charlie's sister!")

    elif rnd is 27:
        await client.send_message(discord.Object(id='337028246413639685'), 'Anyone at the mall?')

    elif rnd is 28:
        await client.send_message(discord.Object(id='337028246413639685'), 'Peter Griffin finds weed in black ops 2')

    elif rnd is 29:
        await client.send_message(discord.Object(id='337028246413639685'), "HELP! I'm stuck in your draw!!!")

    elif rnd is 30:
        await client.send_message(discord.Object(id='337028246413639685'), 'owo')

    
        
@client.command(pass_context=True)
async def stinker(ctx):
    print("running /stinker command...")
    await client.say("ben!")
    print("/stinker command was run")
    
        
        
@client.command(pass_context=True)
async def gay(ctx):
    print("running /gay command...")
    await client.say("Bryce!")
    print("/gay command was run")



@client.command(pass_context=True)
async def sex(ctx,args):
    print("/sex command was run")
    rnd = randint(1, 10)
    if rnd is 1:
        await client.say('Your attempt too sex {} was an epic fail https://images.discordapp.net/attachments/270523219214204938/336812256866336780/18403246_1398304556931039_8835722781557344382_n.jpg'.format(args))
    elif rnd is 2:
        await client.say('Your attempt too sex {} was an epic WIN!!! https://cdn.discordapp.com/attachments/270523219214204938/336812897999126528/1827564-Overlook-Tracer-Winstonboiii.jpg '.format(args))
    
    elif rnd is 3:
        await client.say('Your attempt too sex {} was an epic fail https://images.discordapp.net/attachments/270523219214204938/336812994543616011/18275019_1712761285418928_21504952677890610_n.jpg'.format(args))

    elif rnd is 4:
        await client.say('Your attempt too sex {} was an epic WIN!!! https://images.discordapp.net/attachments/270523219214204938/336813286655918081/ngbbs4495f6d906fd9.gif'.format(args))

    elif rnd is 5:
        await client.say('Your attempt too sex {} was an epic WIN!!! https://images.discordapp.net/attachments/270523219214204938/336814181472796672/big_1473484418_image.jpg'.format(args))

    elif rnd is 6:
        await client.say('Your attempt too sex {} was an epic fail!!! https://i.ytimg.com/vi/hoETcc7HPYw/maxresdefault.jpg '.format(args))

    elif rnd is 7:
        await client.say('Your attempt too sex {} was an epic fail!!! https://images.discordapp.net/attachments/270523219214204938/336814705999872012/17362034_1834954790100000_3559162889712655566_n.jpg?width=442&height=590 '.format(args))

    elif rnd is 8:
        await client.say('Your attempt too sex {} was an epic WIN!!! http://nerdreactor.com/wp-content/uploads/2011/07/CDBABY-Dirty-Single-Cover.jpg '.format(args))

    elif rnd is 9:
        await client.say('Your attempt too sex {} was an epic fail!!! https://images.discordapp.net/attachments/283181037243072512/336815871324323840/de0ca198af75b9c6cdc891d856e33877750bf4fd19f733f4b912681a7d2a4ed1.jpg '.format(args))

    elif rnd is 8:
        await client.say('Your attempt too sex {} was an epic WIN!!! http://i1.ytimg.com/vi/X3ihcfJdAMs/hqdefault.jpg  '.format(args))

@client.command(pass_context=True)
async def illya(ctx):
    channelid = str
    channelid = ctx.message.channel
    print("/illya command was run")
    rnd = randint(1,2)
    if rnd is 1:
        await client.send_file(channelid, 'E:\Discord Bot\illya\loli1.jpg')

    elif rnd is 2:
        await client.send_file(channelid, 'E:\Discord Bot\illya\loli2.jpg')

@client.command(pass_context=True)
async def warning(ctx, args):
    rnd = randint(1, 10)
    if rnd is 1:
        await client.say('{} has been warned, reason: Being an absolute dickhead!'.format(args))

    elif rnd is 2:
        await client.say('{} has been warned, reason: Acting like a real Chris Imhoff!'.format(args))

    elif rnd is 3:
        await client.say('{} has been warned, reason: Spending a Saturday with the mrs!'.format(args))

    elif rnd is 4:
        await client.say("{} has been warned, reason: You're really just pissing me off!".format(args))

    elif rnd is 5:
        await client.say("{} has been warned, reason: Here I was just quietly enjoying my time on The Spookster discord and you just logged in and fucking ruined my day, I'm actually just so fucking pissed at you right now you should probably just leave before I decide too make my way down to your house and beat your lord farquad lookin ass".format(args))

    elif rnd is 6:
        await client.say('{} has been warned, reason: Caught them watching MLP porn!'.format(args))

    elif rnd is 7:
        await client.say("{} has been warned, reason: You think your words hurt? I'm currently on 20 medications for depression. My life is shit. You think your insults can drag me down? I've already hit rock bottom. Look at these cuts. Yeah, I cut the long way. I've been hospitalized twice for blood loss, and each time I come back, I'm cursed for bringing home another hospital bill. You think your words sting? They means nothing. You think you're the only one to insult me? My mom curses me for existing. My dad beats me every day and my older brother, the pervert he is, keeps touching me. They curse me every day for existing. I'm an annoyance. I shouldn't be alive, I wish I could just end it, but there isn't even pain anymore. No reason to end it. You think your words hurt? They mean nothing to me. I don't feel anything anymore. Now please just leave me alone before I ban you".format(args))

    elif rnd is 8:
        await client.say('{} has been warned, reason: fuckin elmo from sesame street lookin ass'.format(args))

    elif rnd is 9:
        await client.say('{} has been warned, reason: okaaaayyyyyy Robbie'.format(args))

    elif rnd is 10:
        await client.say('{} has been warned, reason: Honestly there was no real reason I just really fucking hate you'.format(args))
                         
@client.event
async def on_message(message):
    if message.content == 'owo' :
        await client.send_message(message.channel, "What's this?")
        print('owo command was run!')
    await client.process_commands(message)

@client.command(pass_context=True)
async def pubg(ctx):
    channelid = str
    channelid = ctx.message.channel
    print("/pubg command was executed...")
    # Get an example image
    import matplotlib.cbook as cbook
    image_file = cbook.get_sample_data(r'C:\Users\user\Pictures\Slideshow\map.png')
    img = plt.imread(image_file)

    # Make some example data
    x = np.random.rand(1)*img.shape[1]
    y = np.random.rand(1)*img.shape[0]

    # Create a figure. Equal aspect so circles look circular
    fig,ax = plt.subplots(1)
    ax.set_aspect('equal')

    # Show the image
    ax.imshow(img)

    # Now, loop through coord arrays, and create a circle at each x,y pair
    for xx,yy in zip(x,y):
        circ = Circle((xx,yy),25)
        ax.add_patch(circ)


    plt.savefig(r'C:\Users\user\Pictures\Slideshow\map2.png')
    await client.send_file(channelid, r'C:\Users\user\Pictures\Slideshow\map2.png')



    
client.run("MzM3MDI4MDIwODAxODk2NDU4.DFA5WQ.YttsMxqTRZM3_6yJccgGeaNSJ4Q")

