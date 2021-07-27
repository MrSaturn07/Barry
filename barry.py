import discord
from discord.abc import Messageable
from discord.embeds import Embed
from discord.ext import commands
bot = discord.Client()
bot = commands.Bot(command_prefix='~')
import random
from PIL import Image
from io import BytesIO
import asyncio
import os
from youtube_dl import YoutubeDL
from Music import Music, Music
import aiofiles
import requests, json
from geopy.geocoders import Nominatim
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
bot.add_cog(Music(bot))

@bot.event
async def on_ready():
 game = discord.Game('You like jazz? | ~help')
 await bot.change_presence(status=discord.Status.online, activity=game)
 print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def badaim(ctx):
 """1990 mouse usin ass"""
 godquotes = discord.Embed(title='Aids Aim',description='*Ha ha stupid n word. I would say your aim is cancer, but I fucked your mom*',color=0xFFFF00)
 await ctx.reply(embed=godquotes)
 
@bot.command()
async def Mazywifey(ctx):
 """You say shit, instaban"""
 mazywife = discord.Embed(title='The future wifey',description='<@798022873960415262> luv',color=0xFFFF00)
 await ctx.reply(embed=mazywife)

@bot.command()
async def sex(ctx):
 """Hot"""
 sex = discord.Embed(title="I'm gonna cum",description="⠄⠄⢀⣀⣀⣤⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⣴⣿⡿⠛⠛⠻⢿⣿⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠄⣿⣿⣇⣀⠄⠄⠄⠛⠛⠄⠄⢠⣴⣾⣿⣿⣶⣄⠄⠄⢶⣶⣦⠄⢠⣶⣶⠂⠄ ⠄⠈⠛⠿⠿⣿⣿⣿⣶⣦⡀⢠⣿⣿⣁⣀⣀⣹⣿⣧⠄⠄⠹⣿⣷⣿⡿⠁⠄⠄ ⠠⣤⣤⡀⠄⠄⠄⠈⢻⣿⡇⢸⣿⣿⠛⠛⠛⠛⠛⠛⠄⠄⢠⣾⣿⣿⣆⠄⠄⠄ ⠄⠻⣿⣷⣶⣤⣴⣶⣿⡿⠁⠄⠻⣿⣶⣤⣤⣾⡿⠋⠄⣰⣿⡿⠁⠻⣿⣷⡀⠄ ⠄⠄⠄⠉⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠉⠉⠉⠉⠄⠄⠈⠉⠉⠁⠄⠄⠉⠉⠉⠄",color=0xFFFF00)
 await ctx.reply(embed=sex)

@bot.command()
async def pepe(ctx):
 """Beautiful beautiful boi"""
 pepe = discord.Embed(color=0xFFFF00)
 pepe.set_image(url = 'https://static01.nyt.com/images/2016/09/28/us/17xp-pepethefrog_web1/28xp-pepefrog-articleLarge.jpg?quality=75&auto=webp&disable=upscale')
 await ctx.reply(embed=pepe)

@bot.command()
async def merica(ctx):
 """SUCK ON MY BALLZ"""
 await ctx.reply('Merica FUCK YEAH!!!!')
 await ctx.reply('https://www.youtube.com/watch?v=U1mlCPMYtPk&ab_channel=BadfishKoo')
 
@bot.command()
async def trash(ctx):
 """DISGUSTANG"""
 trash = discord.Embed(title='Fords are trashy :nauseated_face:', color=0xFFFF00)
 trash.set_image(url='https://i.redd.it/lzohorzdgrn21.jpg')
 await ctx.reply(embed=trash)

@bot.command()
async def quality(ctx):
 """The most quailty truck"""
 quality = discord.Embed(title='Now thats one fine truck :pickup_truck:', color=0xFFFF00)
 quality.set_image(url='https://www.motorbiscuit.com/wp-content/uploads/2021/01/Auto-Show-Chevy-Silverado-Display-1024x682.jpg')
 await ctx.reply(embed=quality)

@bot.command()
async def die(ctx):
 """Die painfully"""
 await ctx.reply(ctx.author.mention + ' was hit by a bus full of fortnite players. After they left a few tire marks on the body they got out and dabbed on them. How embarrassing :man_facepalming:')

@bot.command()
async def rick(ctx):
 """Rick em and roll em"""
 await ctx.reply('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')

@bot.command()
async def anime(ctx):
 """The best anime's"""
 anime = discord.Embed(title='My Favorite Animes', description='The Bee Movie \n\n Demon Slayer \n\n hunter x hunter \n\n One Punch Man \n\n My Hero Academia \n\n Blue Exorcist \n\n The Seven Deadly Sins \n\n Naruto', color=0xFFFF00)
 anime.set_thumbnail(url='https://cdn.vox-cdn.com/thumbor/J2XSqgAqREtpkGAWa6rMhkHA1Y0=/0x0:1600x900/1400x933/filters:focal(672x322:928x578):no_upscale()/cdn.vox-cdn.com/uploads/chorus_image/image/66320060/Tanjiro__Demon_Slayer_.0.png')
 await ctx.reply(embed=anime)
  
@bot.command()
async def god(ctx):
 """The true god"""
 god = discord.Embed(color=0xFFFF00)
 god.set_image(url='https://static.wikia.nocookie.net/supermarioglitchy4/images/1/1a/Barry_B._Benson.jpg/revision/latest?cb=20180325023605')
 await ctx.reply(embed=god)
  
@bot.command()
async def daddy(ctx):
 """UwU"""
 daddy = discord.Embed(title='I am your daddy', color=0xFFFF00)
 daddy.set_image(url = 'https://i1.sndcdn.com/avatars-v3dqrzWvuGVwgSvo-u5wDAA-t500x500.jpg')
 await ctx.reply(embed=daddy)

@bot.command()
async def sexybarry(ctx):
 """UGHHHHHHHH si papi"""
 sexy = discord.Embed(title="Why, heya honey", color=0xFFFF00)
 sexy.set_image(url='https://spng.pngfind.com/pngs/s/631-6319286_barry-bee-benson-png-barry-bee-benson-sans.png')
 await ctx.reply(embed=sexy)

@bot.command()
async def update(ctx):
 """Update schedule"""
 update = discord.Embed(title='Update schedule', description='This gets updated essenitally whenever @Mazy is bored or has a funny idea', color=0xFFFF00)
 update.set_thumbnail(url = 'https://www.iquanti.com/wp-content/uploads/2018/03/google-update.jpg')
 await ctx.reply(embed=update)

@bot.command()
async def fuckoff(ctx):
 """Take a hint"""
 fuckoff = discord.Embed(title='Fuck Off', color=0xFFFF00)
 fuckoff.set_image(url='https://www.wired.com/wp-content/uploads/2016/05/11xHTywJSoZIMTgyfgFLBJQ-1.gif')
 await ctx.reply(embed=fuckoff)

@bot.command()
async def whois_Jim(ctx):
 """A bitch"""
 jim = discord.Embed(title='Jim',description='A bitch that likes dirtbikes too much\n\nJk, mans name is Pierson, very cool dud',color=0xFFFF00)
 jim.set_thumbnail(url='https://cdn.discordapp.com/avatars/537808758932504581/a6bd5107a08b6dfa4e3405f01e9d1afa.webp?size=1024')
 await ctx.reply(embed=jim)

@bot.command()
async def whois_Jerky(ctx):
 """Also a bitch"""
 jerky = discord.Embed(title='Jerkey',description='Kind of a bitch, and a retard (likes fords)',color=0xFFFF00)
 await ctx.reply(embed=jerky)

@bot.command()
async def simonsays(ctx, *, arg):
 """Classic"""
 await ctx.reply(arg)

@bot.command()
async def image(ctx, *, arg):
 """reply it"""
 simon = discord.Embed(title='uwu',color=0xFFFF00)
 simon.set_image(url=arg)
 await ctx.reply(embed=simon)

@image.error
async def image_error(ctx, error):
 if isinstance(error, commands.BadArgument):
  await ctx.reply('`You failed, what an idiot`')

#Commands area
@bot.command()
async def info(ctx, user:discord.Member = (None)):
 rando_insults = [
  "They are a registered sex offender!",
  "They hate babies!",
  "They have 27 children locked in their basement.",
  "They hate kittens.",
 ]
 if user==None:
  user=ctx.author
 fmt = '{0} joined on {0.joined_at} and has {1} roles.'
 upfp = user.avatar_url
 profem = discord.Embed(title=user,description=fmt.format(user, len(user.roles)),color=0xFFFF00)
 profem.set_thumbnail(url=upfp)
 profem.add_field(name='Fun fact',value=(random.choice(rando_insults)),inline=True)
 await ctx.reply(embed=profem)

@bot.command()
async def shutupretard(ctx):
 shutret = discord.Embed(title="Shut up retard",description ="You really should you pathetic piece of shit",color = (0xFFFF00))
 await ctx.reply(embed=shutret)

@bot.command()
async def degenerate_scum(ctx):
 degenerate = discord.Embed(title='Absalute Degenerate',desciption='***Degenerates like you belong on a cross***',color=0xFFFF00)
 await ctx.reply(embed=degenerate)
 
@bot.command()
async def whois_urmom(ctx):
 yourmom = discord.Embed(title="Your mom is fuckin ugly",description="I won't sugarcoat it because she'll eat that too",color=0xFFFF00)
 yourmom.set_image(url='http://taggmagazine.com/wp-content/uploads/2013/07/fortune1.jpg')
 await ctx.reply(embed=yourmom)

@bot.command()
async def whois_Mazy(ctx):
 mazy = discord.Embed(title='Mazy',description='Never leaves his pc, likes linux a little too much \n\n **Youtube:** https://www.youtube.com/channel/UCTU12OQOJq55jgqM88P8q0w \n\n **Twitch:** https://twitch.tv/izzmazy \n\n **Twitter:** https://twitter.com/mazylol \n\n **Instagram:** https://www.instagram.com/izzmazy/ \n\n **Steam Profile:** https://steamcommunity.com/id/izzmazy/ \n\n **Reddit:** https://www.reddit.com/user/inmemumscar06 \n\n ',color=0xFFFF00)
 mazy.set_thumbnail(url='https://i.pinimg.com/564x/88/fa/b7/88fab7fd12ecd9c4b165922feac2b354.jpg')
 await ctx.reply(embed=mazy)

@bot.command()
async def Mazyquotes(ctx):
 mazquotes = discord.Embed(title='Mazy Quotes',description="***I'm gonna give blowies at the orphanage*** -Mazy\n\n***Mazy, they're toddlers*** -BT\n\n***And?*** -Mazy",color=0xFFFF00)
 await ctx.reply(embed=mazquotes)

@bot.command()
async def wholoveshim(ctx):
 wholove = discord.Embed(description='***NO ONE***',color=0xFFFF00)
 await ctx.reply(embed=wholove)
 
@bot.command()
async def War(ctx):
 war = discord.Embed(title='War',description="***Just spend youth commiting war crimes*** -BT3025",color=0xFFFF00)
 await ctx.reply(embed=war)
 
@bot.command()
async def sewerslide(ctx):
 sewerslide = discord.Embed(title='Sewerslide',description='***Haha you depressed bitch haha do it no balls***',color=0xFFFF00)
 await ctx.reply(embed=sewerslide)
 
@bot.command()
async def stfu(ctx):
 stfu = discord.Embed(title='STFU',description="https://www.youtube.com/watch?v=KRB-iHGHSqk or https://www.youtube.com/watch?v=OLpeX4RRo28",color=0xFFFF00)
 await ctx.reply(embed=stfu)
 
@bot.command()
async def littlegirls(ctx):
 littlegirl = discord.Embed(title='Little Girls',description="https://www.youtube.com/watch?v=6ltAVRyeqHk",color=0xFFFF00)
 await ctx.reply(embed=littlegirl)
 
@bot.command()
async def YeeYeeHaircut(ctx):
 yeeyeehc = discord.Embed(title='Yee Yee Haircut',description="***Ah, nigga, don't hate me 'cause I'm beautiful, nigga. Maybe if you got rid of that old yee-yee ass haircut you got you'd get some bitches on your dick. Oh, better yet, maybe Tanisha'll call your dog-ass if she ever stop fuckin' with that brain surgeon or lawyer she fucking with. Niggaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa***",color=0xFFFF00)
 await ctx.reply(embed=yeeyeehc)
 
@bot.command()
async def TheTruth(ctx):
 truth = discord.Embed(title='Truthbomb',description="***Maybe Khans kill people without looking them in the face, but I ain't a fink, dig? You've made your last delivery, kid. Sorry you got twisted up in this scene. From where you're kneeling it must seem like an 18-carat run of bad luck. But, truth is... the game was rigged from the start.***",color=0xFFFF00)
 await ctx.reply(embed=truth)
 
@bot.command()
async def instantweebdepression(ctx):
 instaweebdep = discord.Embed(title='Instant Weeb Depression',description="***Ash, I am very worried because I haven’t seen you and I don’t know if you are okay. You said to me before, “we live in different worlds,” but I am not sure if that is true. We are from different countries, and our skin and eyes are different colours. But so what? We are friends. Isn’t that enough? What else do we need? I am very happy I came to America. I made many friends here. Above all… I met you, Ash. You asked me many times if you scare me. But I never felt scared of you, not even once, From the first time I met you. Actually, I always felt that you are hurt, much more than me - that your spirit is wounded. I know you are much smarter than me, and bigger, and stronger - but even so.. I always wanted to protect you. Funny, isn’t it? But what did I want to protect you from? I think I wanted to protect you from your future. Because your fate was sweeping you away, like a flood. Do you remember telling me about the leopard in the Hemingway book? He died at the top of the mountain, and you said he knew he will never go back down. But I said you are not a leopard, and that you can change your future. It’s true, Ash. You can change your fate. You are not alone, Ash. I am with you. My soul is always with you. Sayonara, New York… Sayonara, America. … Ash, but I’m not saying “sayonara” to you.. because this isn’t goodbye. I know we’ll see each other again someday.. You are my best friend, Ash.***",color=0xFFFF00)
 await ctx.reply(embed=instaweebdep)
 
@bot.command()
async def caveman(ctx):
 caveman = discord.Embed(title='OOGABOOGA',color=0xFFFF00)
 caveman.set_image(url="https://media.discordapp.net/attachments/814345735226785812/814682754079260712/image0.gif")
 await ctx.reply(embed=caveman)
 
@bot.command()
async def Loser(ctx):
 loser = discord.Embed(title='What a loser',color=0xFFFF00)
 loser.set_image(url="https://media.discordapp.net/attachments/814345735226785812/814684633530499113/image0.png?width=420&height=401")
 await ctx.reply(embed=loser)

@bot.command()
async def BigTiddiesAndTrauma(ctx):
 bigtittiesandtruama = discord.Embed(title='Big Tiddies *and trauma*',color=0xFFFF00)
 bigtittiesandtruama.set_image(url='https://i.redd.it/19erqlus9rr21.jpg')
 await ctx.reply(embed=bigtittiesandtruama)

@bot.command()
async def BigAnimeTiddies(ctx):
 embed = discord.Embed(title = "Random Nhentai Number", description = (random.randint(111111,999999)), color = (0xFFFF00))
 await ctx.reply(embed = embed)

@bot.command()
async def LightningMcqueen(ctx):
 lightningmcfuck = discord.Embed(title='KACHOW',color=0xFFFF00)
 lightningmcfuck.set_image(url="https://i.ytimg.com/vi/3S6uNw-D6RA/maxresdefault.jpg")
 await ctx.reply(embed=lightningmcfuck)

@bot.command()
async def DoinYaMom(ctx):
 doinyamum = discord.Embed(title="Doin ya mom",description="Doin ya mom",color=0xFFFF00)
 await ctx.reply(embed=doinyamum)

@bot.command()
async def Nukes(ctx):
 nukes = discord.Embed(title='Nukes',description="***I am become death, destroyer of worlds***",color=0xFFFF00)
 await ctx.reply(embed=nukes)

@bot.command()
async def Oath(ctx):
 oath = discord.Embed(title='The Oath',description="***I, Barry B. Benson swear on my worthless bot life to say nothing but the truth***",color=0xFFFF00)
 await ctx.reply(embed=oath)

@bot.command()
async def BestGameEver(ctx):
 bestgamever = discord.Embed(title='ALL BAD',description="***EVERY GAME EVER PLAYED IS A PIECE OF SHIT***",color=0xFFFF00)
 await ctx.reply(embed=bestgamever)
  
@bot.command()
async def retard(ctx):
 retard = discord.Embed(title="I found one!!!" ,color=0xFFFF00)
 retardimg = ctx.author.avatar_url
 retard.set_image(url=retardimg)
 await ctx.reply(embed=retard)

@bot.command()
async def pooper(ctx):
 poopie = discord.Embed(title="That's one big stink",color=0xFFFF00)
 poopie.set_image(url='https://i.cbc.ca/1.4956283.1545425483!/fileImage/httpImage/image.JPG_gen/derivatives/16x9_780/trump-poo.JPG')
 await ctx.reply(embed=poopie)

@bot.command()
async def tractor(ctx):
 tractor = discord.Embed(title='She likes my tractor',color=0xFFFF00)
 tractor.set_image(url='https://i.ytimg.com/vi/gaiOisHQSlQ/maxresdefault.jpg')
 await ctx.reply(embed=tractor)

@bot.command()
async def whois_urdad(ctx):
 urdaddy = discord.Embed(title='Fuckin weird redneck lookin ass',color=0xFFFF00)
 urdaddy.set_image(url='https://static8.depositphotos.com/1386061/896/i/600/depositphotos_8963619-stock-photo-southern-hick-with-a-rifle.jpg') 
 await ctx.reply(embed=urdaddy)

@bot.command()
async def yeetusthatfetus(ctx):
 fetus = discord.Embed(title='An ultra speedy abortion',color=0xFFFF00)
 fetus.set_image(url='https://i.pinimg.com/originals/cb/ce/fa/cbcefafdc787c75b12ddce68e47c753c.jpg')
 await ctx.reply(embed=fetus)

@bot.command()
async def im14andthisisdeep(ctx):
 deep = discord.Embed(title='14 Year Old Girls Be Like:',color=0xFFFF00)
 deep.set_image(url='https://i.ytimg.com/vi/_Nu6_A6PXEY/maxresdefault.jpg')
 await ctx.reply(embed=deep)

@bot.command()
async def wanted(ctx, user:discord.Member = (None)):
 if user is None:
  user = ctx.author
 wanted = Image.open("wanted.jpg")
 asset = user.avatar_url_as(size=128)
 data = BytesIO(await asset.read())
 pfp = Image.open(data)
 pfp = pfp.resize((284,284))
 wanted.paste(pfp, (88,229))
 wanted.save("profile.jpg")
 await ctx.send(file=discord.File("profile.jpg"))

@bot.command()
async def gay(ctx, user:discord.Member = (None)):
 if user is None:
  user = ctx.author
 gay = Image.open("gaepic.jpg")
 asset = user.avatar_url_as(size=128)
 data = BytesIO(await asset.read())
 pfp = Image.open(data)
 pfp = pfp.resize((131,131))
 gay.paste(pfp, (455,63))
 gay.save("biggae.jpg")
 await ctx.send(file=discord.File("biggae.jpg"))

@bot.command()
async def getpfp(ctx, user:discord.Member = (None)):
 if user is None:
  user=ctx.author
 pfp = user.avatar_url
 pfpembed = discord.Embed(title="Ew that's an ugly profile pic",color=0xFFFF00)
 pfpembed.set_image(url=pfp)
 await ctx.reply(embed=pfpembed)

@bot.command()
async def search(ctx, *, arg):
 try:
	 from googlesearch import search
 except ImportError:
  await ctx.reply("No module named 'google' found")
 for j in search(arg, tld="co.in", num=1, stop=1, pause=2):
	 await ctx.reply(j)

@bot.command()
async def rape(ctx, user:discord.Member = (None)):
 if user is None:
  await ctx.reply('`Error: Needs a target`')
  return
 else:
  gay = Image.open("rape.jpg")
  author = ctx.author.avatar_url_as(size=128)
  authdata = BytesIO(await author.read())
  authpfp = Image.open(authdata)
  authpfp = authpfp.resize((131,131))
  gay.paste(authpfp, (293,37))
  gay.save("lego.jpg")
  target = user.avatar_url_as(size=128)
  userdata = BytesIO(await target.read())
  userpfp = Image.open(userdata)
  userpfp = userpfp.resize((131,131))
  gay.paste(userpfp, (76,320))
  gay.save("lego.jpg")
  await ctx.reply(file=discord.File("lego.jpg"))

@bot.command()
async def hack(ctx,user:discord.Member = (None)):
 homeworkfolder = [
  'Mom',
  'Dad',
  'Grandma',
  'Grandpa',
  'School',
 ]
 homeworkran = random.choice(homeworkfolder)
 if user is None:
  await ctx.reply('`Error: Needs a target to hack stupid`')
  return
 else:
  hackmsg = await ctx.reply("<a:redsiren:867615081084223529>**Starting the hack on {}.**<a:bluesiren:867615267386818570>".format(user))
  await asyncio.sleep(1)
  await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}..**<a:bluesiren:867615267386818570>".format(user))
  await asyncio.sleep(1)
  await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}...**<a:bluesiren:867615267386818570>".format(user))
  await asyncio.sleep(1)
  await hackmsg.edit(content="<a:redsiren:867615081084223529>**Starting the hack on {}.**<a:bluesiren:867615267386818570>".format(user))
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Finding info.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Finding info..**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Finding info...**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Finding info.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Email:** `{}@lemenmail.seggs`\n\n**Phone:** `(420) 690-6969`\n\n**Job:** `Verified Pornhub Actor`".format(user))
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Injecting malware.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Injecting malware..**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Injecting malware...**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Injecting malware.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="<:Nigeriancat:849547273339142154>**Access obtained**<:Nigeriancat:849547273339142154>")
  await asyncio.sleep(2)
  await hackmsg.edit(content="**Navigating to `C:\Homework`**")
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Planting gay furry porn.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Planting gay furry porn..**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Planting gay furry porn...**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Planting gay furry porn.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Planted**")
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Sharing the folder to {}**".format(homeworkran))
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Family successfully torn apart**")
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Looking through search history.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Looking through search history..**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Looking through search history...**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Looking through search history.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Most recent search:** `Pornhub.com: Glory Hole get used by them all`")
  await asyncio.sleep(3)
  await hackmsg.edit(content="**Destroying evidence.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Destroying evidence..**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Destroying evidence...**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**Destroying evidence.**")
  await asyncio.sleep(1)
  await hackmsg.edit(content="**The FBI is definately on your ass now so good luck**")
  await asyncio.sleep(3)
  await hackmsg.edit(content="**The hack is complete**")

@bot.command()
async def weather(ctx, *, args):
 api_key = "f7acdab230c0a3c9a66d2557419c2955"
 base_url = "http://api.openweathermap.org/data/2.5/weather?"
 locator = Nominatim(user_agent="myGeocoder")
 location = locator.geocode(str(args))
 lat = str(location.latitude)
 lon = str(location.longitude)
 complete_url = base_url + "appid=" + api_key + "&lat=" + lat + "&lon=" + lon + "&units=imperial"
 response = requests.get(complete_url)
 x = response.json()
 if x["cod"] != "404":
  y = x["main"]
  current_temperature=str(y["temp"])
  current_pressure=str(y["pressure"])
  current_humidity=str(y["humidity"])
  temp_min=str(y["temp_min"])
  temp_max=str(y["temp_max"])
  z = x["weather"]
  weather_description = str(z[0]["description"])
  wethr = discord.Embed(title='Weather',color=0xFFFF00)
  wethr.add_field(name='Current Temperature',value=current_temperature + " Ferenheit",inline=False)
  wethr.add_field(name='Low',value=temp_min + " Ferenheit",inline=False)
  wethr.add_field(name='High',value=temp_max + " Ferenheit",inline=False)
  wethr.add_field(name='Atmospheric Pressure (in hPa)',value=current_pressure,inline=False)
  wethr.add_field(name='Humidity',value=current_humidity + "%",inline=False)
  wethr.add_field(name='Weather Description',value=weather_description,inline=False)
  await ctx.reply(embed=wethr)

@bot.command()
async def emoji(ctx, *, args):
 if args == ':wumpbongo:':
  await ctx.send('<a:wumpbongo:799111582130110515>')
 if args == ':vibez:':
  await ctx.send('<a:vibez:799108578920497172>')
 if args == ':rgblob:':
  await ctx.send('<a:rgblob:798608769897463858>')
 if args == ':redsiren:':
  await ctx.send('<a:redsiren:867615081084223529>')
 if args == ':popcat:':
  await ctx.send('<a:popcat:799111068168224808>')
 if args == ':peacebruh:':
  await ctx.send('<a:peacebruh:799108579051175936>')
 if args == ':knowledge:':
  await ctx.send('<a:knowledge:801824327053737994>')
 if args == ':itwasme:':
  await ctx.send('<a:itwasme:799111032575885342>')
 if args == ':hydrate:':
  await ctx.send('<a:hydrate:818297802081435648>')
 if args == ':hornycord:':
  await ctx.send('<a:hornycord:799111581900341270>')
 if args == ':Fsmash:':
  await ctx.send('<a:Fsmash:799108579151708182>')
 if args == ':dino:':
  await ctx.send('<a:dino:802596004938776646>')
 if args == ':danceblob:':
  await ctx.send('<a:danceblob:799108578882486283>')
 if args == ':comeatme:':
  await ctx.send('<a:comeatme:799112392264908810>')
 if args == ':bluesiren:':
  await ctx.send('<a:bluesiren:867615267386818570>')
 if args ==':applecat:':
  await ctx.send('<a:applecat:799111032705384498>')
 if args == ':animeroll:':
  await ctx.send('<a:animeroll:799106437942345728>')
 

bot.run('ODE1NDU1Njk5MTE0MjYyNTY4.YDsqTQ.RPIxl0rf-HhuFVWl-Ot106B3pAA')