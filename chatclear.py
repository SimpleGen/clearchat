import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = "NTgxODA5ODU1OTU0NjgxODc2.XOmTnA.PRpqxPuMCQzHT-SqJES7lsZhMcQ"
client = commands.Bot(command_prefix="-")

Client = discord.client
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    print ("I am running on")
    await client.change_presence(activity=discord.Game(name="-gen | 7sek"))

#MINECRAFT
#MINECRAFT
#MINECRAFT
#MINECRAFT

@client.command()
@commands.has_permissions(send_messages=True)
async def minecraft(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -minecraft @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Minecraft account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "jeason3bb@gmail.com:baba6635",
        "monterojalysa@yahoo.com:jalysa23",
        "nickpilotte7@live.com:ilygussyyes7",
        "jeason3bb@gmail.com:baba6635",
        "monterojalysa@yahoo.com:jalysa23",
        "sennabravenboer@gmail.com:braaf206",
        "thebadster@hotmail.com:Clippers11",
        "stefanpaccaud@gmail.com:Stefan0122",
        "monterojalysa@yahoo.com:jalysa23",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)

@minecraft.error
async def minecraft_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#SPOTIFY
#SPOTIFY
#SPOTIFY
#SPOTIFY

@client.command()
@commands.has_permissions(send_messages=True)
async def spotify(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -spotify @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a Spotify account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "dmcghee1@hotmail.com:Cunn1ngham",
        "maira_giggles@hotmail.com:homerito12",
        "kyanoffutt@gmail.com:CCommerce1",
        "elikay111@yahoo.com:qwertyuiop",
        "itsamandalindsey@yahoo.com:Tobasco8 | US",
        "apatino52@gmail.com:denise88 | US",
        "briannemccauliffe@gmail.com:yerface1 | US",
        "sekyeredelores@yahoo.com:sincity1 | US",
        "mollyrothaus@gmail.com:shinshin | US",
        "proudmommy1748@gmail.com:Alessa07 | US",
        "thewimberleyfam@gmail.com:Landon03 | US",
        "kybrighteyes@gmail.com:jlm72986 | US",
        "sm_moreno_@hotmail.com:goblue11 | US",
        "angulo306@hotmail.com:18beto06 | US",
        "defiprophetic@gmail.com:122459122459 | US",
        "oax4y@hotmail.com:tonito04 | US",
        "callieburris@gmail.com:mariah29 | US",
        "teeplesst@gmail.com:batgirl8886 | US",
        "ramirez15alexandra@gmail.com:zoeybear | US",
        "rachelwaraksa@gmail.com:beatles88 | US",
        "puckett.madeline@gmail.com:puckett3 | US",
        "zachnorris7@yahoo.com:sophie117 | US",
        "pranny.1012@gmail.com:batista123 | US",
        "sailorsonic02@gmail.com:flatwalk81 | US",
        "michellekorp@gmail.com:Sweets22 | US",
        "potenza448@gmail.com:Turkeybird1 | US",
        "cduell144@roadrunner.com:spencer144 | US",
        "homesbyeagle@aol.com:Eagle1997 | US",
        "rhonda_ludbrook@yahoo.com:Utarlg01 | US",
        "thecoffeeMailbox@gmail.com:Mongoose12 | US",
        "Tjcalmon@gmail.com:eagles11 | US",
        "stewart85@gmail.com:Paddock4034 | US",
        "acsjcs@hotmail.com:jcsacg00 | US",
        "mrg8585@yahoo.com:feisty2007 | US",
        "zcesg@yahoo.com:zephyr | US",
        "manifest61@yahoo.com:1018obama | US",
        "manchild606184@yahoo.com:05nikki85 | US",
        "opatlamo@gmail.com:phucyoua | US",
        "polega@chapman.com:rocky247 | US",
        "chris_duncil@yahoo.com:aquarium | US",
        "cd_crystal@yahoo.com:harvest1 | US",
        "nickrangnekar@gmail.com:niditi7870 | US",
        "jenibackhaus@gmail.com:isaac247 | US",
        "andrewskolette@gmail.com:bearlake8 | US",
        "kaydeee23@aol.com:mytaylre25 | US",
        "gregorymoran@mac.com:rqhf8a | US",
        "javiervila1171@gmail.com:Dragons17 | US",
        "dewster420bagel@yahoo.com:beatit963 | US",
        "insideoutfitter@yahoo.com:rush2112 | US",
        "gera.saenz@live.com:chabela | US",
        "nancy.o.ewing@gmail.com:sputnik | US",
        "matthewneuhaus17@gmail.com:Green!5653 | US",
        "soccerlucas1@gmail.com:weis0171 | US",
        "granpa0405@gmail.com:tashagirl | US",
        "iivomac@gmail.com:Little13 | US",
        "coleshortall28@gmail.com:Green104 | US",
        "vannibunni@rocketmail.com:svanig14 | US",
        "holaruthann@gmail.com:polly7anna | US",
        "mnstrduc@yahoo.com:ducati996 | US",
        "tymogar@gmail.com:imreallybored1 | US",
        "emily_steffensen@hotmail.com:bluegreenpoco | US",
        "david.owens.012@gmail.com:Cobras12 | US",
        "john231lee@aim.com:Lasko123 | US",
        "kylelambeth101@gmail.com:Rockband2 | US",
        "Jacob_houzenga@yahoo.com:Turtle123123 | US",
        "laudi2016@hotmail.com:rogue2000 | US",
        "sebastian.waterman@gmail.com:Swatter27 | US",
        "pumpkinking51@gmail.com:pizza2002 | US",
        "zanemoseley@hotmail.com:511361 | US",
        "bjscullion@gmail.com:yearight | US",
        "gauth113@yahoo.com:mt101198 | US",
        "JSpadesM@aim.com:ars123 | US",
        "loganelectro@gmail.com:halofan1 | US",
        "taycurrie@gmail.com:ptlightnning | US",
        "notserp007@gmail.com:52j=VUhu | US",
        "jnorton5491@gmail.com:hoover98 | US",
        "cjax531@prodigy.net:100Bottles | US",
        "thenneghan@gmail.com:diewulu74 | US",
        "sacha@bluebirdboutique.com:banana | US",
        "trishalyn_76@yahoo.com:chadwick23 | US",
        "adjustis@yahoo.com:maple1 | US",
        "jeannebeanie_57@hotmail.com:jmwsneak1 | US",
        "alisonkwoods@gmail.com:eirgil | US",
        "dandamico6454@msn.com:puggerman | US",
        "twintime@yahoo.com:twin1957 | US",
        "williamburell@gmail.com:Jeep9099 | US",
        "dwolfz720@gmail.com:wolf7star | US",
        "sarah.chambliss@gmail.com:lamat3774 | US",
        "aldavis72@comcast.net:Chevy_2001 | US",
        "lunsfordmichael@comcast.net:shenand0 | US",
        "daytripper62@comcast.net:bb031427 | US",
        "jmblokdijk@gmail.com:A10lakers | US",
        "cdenton041793@gmail.com:leapyear1 | US",
        "projectelitestebbins@yahoo.com:gunner13 | US",
        "independentman19@aim.com:monster1 | US",
        "mckenziestahmer@gmail.com:ms961501 | US",
        "jonasall@msn.com:Earthsea1 | US",
        "m.shemeley@verizon.net:ironshem1 | US",
        "blakecolquitt@gmail.com:12343214 | US",
        "rjwatts45@gmail.com:gixxer05 | US",
        "morganmccray31@yahoo.com:gorillajoe88 | US",
        "Singerar1@att.net:042498pt | US",
        "stephaniejudd@me.com:11pass11 | US",
        "stephenk81@yahoo.com:ashton05 | US",
        "steve.ooo@mac.com:trbrocks1 | US",
        "justinpease822@gmail.com:v240z18a1 | US",
        "brianaspangler44@gmail.com:44porkypines | US",
        "hayatcamellia@yahoo.com:skank1294 | US",
        "wilfredo20200@yahoo.com:Janet318 | US",
        "crystal.lauran@gmail.com:M1cha3lsux | US",
        "wrigleybear1@gmail.com:12346107j | US",
        "jonathan_ackley91@yahoo.com:j199110231 | US",
        "blast3r321@hotmail.com:a00510457 | US",
        "vness29@yahoo.com:diego611 | US",
        "workwoman@hotmail.com:jojo7788 | US",
        "averydarcher725@yahoo.com:avery2000 | US",
        "nikatkins@gmail.com:nearma81 | US",
        "kmuzamali11@yahoo.com:Hasek139 | US",
        "keaunawalt@aol.com:Dutchess123 | US",
        "mentzer.20@osu.edu:noodles | US",
        "kelseyunland@gmail.com:horses123 | US",
        "suzywickham@yahoo.com:Bubbles1 | US",
        "yang.931@gmail.com:ianhan0106 | US",
        "info@cassandcompanysalon.com:cass2001 | US",
        "sportystuff16@gmail.com:Ksmyace16 | US",
        "lynneann1@hotmail.com:5996011 | US",
        "gilkeylaquann@gmail.com:gilkey12 | US",
        "justindoty97@hotmail.com:Greenmachine101 | US",
        "scmipa@gmail.com:Amberwan1 | US",
        "ppajkos_85@hotmail.com:sticks2b | US",
        "shafner1@yahoo.com:4freedom | US",
        "kimm199@yahoo.com:waterr | US",
        "MYFIDDY6@aol.com:SNOOPY1 | US",
        "marclouw@gmail.com:m101sail | US",
        "annakcampbell@aol.com:Ob1kenobi | US",
        "alfonsotapia18@yahoo.com:toofast12 | US",
        "ba.parnian10@gmail.com:Pari1234 | US",
        "bambamups@yahoo.com:chapell1965 | US",
        "stewy12006@yahoo.com:Racecar1 | US",
        "bratmana85@yahoo.com:Dannylover85 | US",
        "cassidy_little@yahoo.com:Jesus911 | US",
        "j.shehorn@gmail.com:falcon16 | US",
        "Joe00144@gmail.com:Jojo0918 | US",
        "jrgenz1102@yahoo.com:baseball31 | US",
        "kacie.snellings@gmail.com:Tarheels1 | US",
        "kckay21@gmail.com:Kowboyk1 | US",
        "devsaj@hotmail.com:sdevitt1 | US",
        "kpmorris07@yahoo.com:Glasg0w1972 | US",
        "l_bastress@yahoo.com:hawaii94 | US",
        "laurie@lacreativeonline.com:shawnbacker19 | US",
        "matso01@live.com:saints25 | US",
        "mebrunner0591@gmail.com:Rolltide1991 | US",
        "melissablain47@yahoo.com:Trey1219 | US",
        "merrittbuck@gmail.com:130Ngevertdr | US",
        "sarahrpannell@yahoo.com:srp8764mtp | US",
        "Snoslash88@gmail.com:woodis11 | US",
        "krickens21@hotmail.com:rocker17 | US",
        "milind_gokhale@yahoo.com:madjayraj | US",
        "patti.cole@gmail.com:lifeisgr8 | US",
        "posterworksgallery@gmail.com:pepper1 | US",
        "aerosmith722@yahoo.com:susieq01 | US",
        "ericadiles@yahoo.com:jeeeed25 | US",
        "phil@philbransom.com:uofo1980 | US",
        "tothgjoshua@gmail.com:Cosmic0384 | US",
        "dregenius98@gmail.com:ford1000 | US",
        "djnorap@gmail.com:adrlyda12 | US",
        "maanhilal@gmail.com:tri601521 | US",
        "happywithlife@gmail.com:Freedom100 | US",
        "barrybrooksoneill@gmail.com:Dollarbills | US",
        "johnoo70@hotmail.com:a3zeva123 | US",
        "j.jess2001@yahoo.com:Poptart1234 | US",
        "brian.newman84@gmail.com:mejo2102 | US",
        "kellb73@yahoo.com:jager123 | US",
        "darkcriii@yahoo.com:joey2636 | US",
        "Coleriggs13@yahoo.com:marie1 | US",
        "nshenkle@yahoo.com:maggylucy | US",
        "leahfremouw@yahoo.com:marley1fr | US",
        "sniclong@yahoo.com:samavamandy | US",
        "karen_keeter@yahoo.com:karen1963 | US",
        "charisma.edmisten@yahoo.com:Baton321 | US",
        "ninjamanex23@gmail.com:pikachu23 | US",
        "n.lascelles@yahoo.com:river1 | US",
        "heavenstar83@yahoo.com:elijahmichael | US",
        "eraserhead2287@yahoo.com:RATMx523 | US",
        "rachhany@yahoo.com:fresno | US",
        "southernbelle777@hotmail.com:philojl77 | US",
        "prettypaintg@yahoo.com:eagles36 | US",
        "carmendes2001@yahoo.com:games4us | US",
        "thekosals@yahoo.com:jack1234 | US",
        "brennen.w.brown@gmail.com:Panthers15 | US",
        "mitchell.conrad@gmail.com:Mitchmom10 | US",
        "ayad.richard@gmail.com:Likeawhore7 | US",
        "zibbus26@msn.com:quinn3561 | US",
        "steve@ibizsystems.net:hello123 | US",
        "sm103@att.net:melvin | US",
        "waitfortheword@gmail.com:juice1980 | US",
        "ctholden93@gmail.com:relaxed1 | US",
        "amata029@gmail.com:Blowme12 | US",
        "ambrose20000@gmail.com:richard11 | US",
        "katnipgangsta@gmail.com:bruins13 | US",
        "rachel.dickinson154@gmail.com:soonok32 | US",
        "joseph.ruiz@cox.net:Tigger77 | US",
        "alan.zhu.yu@gmail.com:alan72mike | US",
        "alistewart@gmail.com:6thSister | US",
        "swhit94@gmail.com:Skyhigh123 | US",
        "moser.grant@gmail.com:3l3phant | US",
        "bartondvm@gmail.com:Blue1pic | US",
        "brendafowler@comcast.net:january18 | US",
        "brianheisler@comcast.net:luke0511 | US",
        "cander49@utk.edu:titan529 | US",
        "breeagainstcity@yahoo.com:alltimel0w | US",
        "yohance518@gmail.com:yohance1 | US",
        "colbert.xandria7@gmail.com:Mtutt112 | US",
        "m_dahne@yahoo.com:pinnacle | US",
        "ejoliva@comcast.net:Plugpark91 | US",
        "norcalracer88@msn.com:Enochs88 | US",
        "boone.nichols@gmail.com:Colton1234 | US",
        "ryansmithers@cox.net:Pali2012 | US",
        "ter0814@yahoo.com:skulls13 | US",
        "rodriguez.adrian81@yahoo.com:1251628a | US",
        "susangiaco@gmail.com:buzzy1 | US",
        "lisamosquera4@yahoo.com:mom061065 | US",
        "swain.kim.d@gmail.com:jomamma | US",
        "salj2876@yahoo.com:2876dora | US",
        "deborah@bjorkly.com:Figaro2012 | US",
        "grob556@gmail.com:Th$6uhHum | US",
        "irenemark@comcast.net:andrew99 | US",
        "tenishadandridge@yahoo.com:bd24955460 | US",
        "thavle1@gmail.com:thuydung12 | US",
        "mdgibson80@gmail.com:liberty1 | US",
        "reymundo.lozano@mssm.edu:Oxfocars072 | US",
        "rpepsin1@gmail.com:usbank01 | US",
        "swannlong@aol.com:swanner4 | US",
        "daveroggen@yahoo.com:hashomer | US",
        "parksa@net.elmhurst.edu:sodapop1 | US",
        "robertz1894@gmail.com:bubbaboy62 | US",
        "Greg.Mansell@Ohio-EmploymentLawyer.com:gm281826 | US",
        "bjmealer@hotmail.com:bj0729bj | US",
        "joy.cameron@gmail.com:joanie66 | US",
        "wifi13@Comcast.net:Brandy1358 | US",
        "karenlbailey@sbcglobal.net:kitterpuss | US",
        "kasey@oleary.net:drinzy | US",
        "stazzles@gmail.com:mememe123 | US",
        "atntpc@yahoo.com:Giantescape2 | US",
        "caesar.rangel@yahoo.com:love4boys | US",
        "emilyjeanette@gmail.com:midget44 | US",
        "kaycho1101@yahoo.com:Kailene1101 | US",
        "luisnunez318@gmail.com:Cortana117 | US",
        "toddpeixinho13@gmail.com:Abcdefg8 | US",
        "bigtbone17@gmail.com:packers4 | US",
        "seased78@gmail.com:Skyrim78 | US",
        "lilspykdogg3@gmail.com:eevee123 | US",
        "theaob@aol.com:protoman1994 | US",
        "lord_kiddian@yahoo.com:p3numbra | US",
        "lanirose30@gmail.com:34hondas | US",
        "kayleewheeler33@gmail.com:jakeroo | US",
        "cchampernowne@gmail.com:Ravenclaw1 | US",
        "tobeexzack@gmail.com:Midnight11 | US",
        "daebrieon@yahoo.com:Drillers35 | US",
        "harunbegic@yahoo.com:Rajvosa1971 | US",
        "mrbossandrew@gmail.com:Likeaboss1 | US",
        "mcgrathz@yahoo.com:newjersey | US",
        "alecsmurf9@gmail.com:alec1117 | US",
        "diarmot@aol.com:carlow40 | US",
        "nmwr@mac.com:august21 | US",
        "amyryupark@yahoo.com:mimi3momo | US",
        "Ef_sala@aol.com:fabian75 | US",
        "eggritx@msn.com:Happy2day | US",
        "john.wilson@sekologistics.com:jwilly77 | US",
        "nancycenter@me.com:Deovalenti77 | US",
        "Donaldrhaas@gmail.com:college34 | US",
        "wickedjoker806@yahoo.com:adidas666 | US",
        "laurakirchner@hotmail.com:Tatumk22 | US",
        "manofwargh@gmail.com:701669 | US",
        "bill2934@gmail.com:thirtytwo32 | US",
        "asam06@gmail.com:oranges1 | US",
        "dbressler569@aol.com:Butthead569 | US",
        "mashmallow346@gmail.com:popcorn56 | US",
        "davidweidberg@gmail.com:cowboys1175 | US",
        "corywallace90@gmail.com:Wallace45 | US",
        "dlesesne23@gmail.com:akdale16 | US",
        "colorizedd@gmail.com:1life1love | US",
        "pkennedy787@gmail.com:ilikepie11 | US",
        "penguinsw022@gmail.com:fanon022 | US",
        "sethnajay@gmail.com:W!ndmil1 | US",
        "jospre001@yahoo.com:ignite123 | US",
        "teishaearl@yahoo.com:March1994 | US",
        "samhoward05@gmail.com:soccer3 | US",
        "tjaffurs@gmail.com:TJpilot01 | US",
        "jtstrapp79@yahoo.com:casavian | US",
        "conemusic@yahoo.com:woodbed513 | US",
        "oneswtworld@gmail.com:pearljam | US",
        "ldrapermusic@gmail.com:hermano1 | US",
        "sbrown1186@hotmail.com:local420 | US",
        "vlang45@hotmail.com:mustang9 | US",
        "kabarham2011irc@gmail.com:chowflea309 | US",
        "rodmachbr@hotmail.com:adsumus010378 | US",
        "evelyncarreon56@gmail.com:Bobby022 | US",
        "jschmidt85@gmail.com:Spike2k187 | US",
        "marcus513@hotmail.com:money1977 | US",
        "seeslam426@gmail.com:5335743 | US",
        "ktlouiselerer@gmail.com:mrsscoot | US",
        "skostinsky@gmail.com:2pimlico | US",
        "briangierman@gmail.com:bg607153 | US",
        "navygirl9801@yahoo.com:annabel1 | US",
        "jeffrey.mance@gmail.com:JmFu4861 | US",
        "geralddwright@gmail.com:33Knicks | US",
        "rgoldsteincpa@yahoo.com:Mgeg38ag | US",
        "sherry.fardie@yahoo.com:orion6451 | US",
        "ranyahutchens@yahoo.com:gabriel1 | US",
        "jayfra35@gmail.com:erinma | US",
        "prado.jillian@gmail.com:mookie85 | US",
        "rsbaier@gmail.com:booby2 | US",
        "Wjanetdougherty@gmail.com:wonee0504 | US",
        "aswinkumar.saravanan@gmail.com:banana | US",
        "trochan@gmail.com:Pataluma007 | US",
        "dimitri.vermes@gmail.com:chepo98p | US",
        "mjfarley@gmail.com:farside73 | US",
        "courtneeulrich@gmail.com:hippos | US",
        "sandjkemp4585@gmail.com:badist202 | US",
        "benkocm@gmail.com:kokobe01 | US",
        "matt.isenbarger@gmail.com:Mattiso1 | US",
        "csnyder7@gmail.com:C2010Ssb | US",
        "cerullot@gmail.com:Baseball84 | US",
        "sdhomeguru@yahoo.com:ewcaky5151 | US",
        "jimsbagger@yahoo.com:jimbo58 | US",
        "mallorycaldwell@gmail.com:lilangel82 | US",
        "tiffpat@aol.com:6723401g | US",
        "h_rogers@yahoo.com:SupremeJ1 | US",
        "martin.perez456@yahoo.com:88569456 | US",
        "eliastavarez22@gmail.com:penguins11 | US",
        "imsopretty2001:Maddy2001 | US",
        "Fleuryaaron19@gmail.com:Cortland19 | US",
        "jacquelinemary1989@gmail.com:clock1234 | US",
        "dakotadeist@gmail.com:dakota96 | US",
        "m.andrews9739@gmail.com:love0812 | US",
        "Mr.nictionary@gmail.com:monkey911 | US",
        "alexroman2011@yahoo.com:bologna8 | US",
        "wmichaelshannon@aol.com:imagine0 | US",
        "elliejones248@gmail.com:Music248 | US",
        "emmamicic@yahoo.com:wgwittbmg | US",
        "erinmcglynn100@yahoo.com:pacokona | US",
        "Gregory.savanah@gmail.com:Savanah22 | US",
        "hadeel724@outlook.com:reem24 | US",
        "hmsmary8708@gmail.com:0610hms8708 | US",
        "jadaadger@yahoo.com:love7262 | US",
        "jasmine.rab4@gmail.com:Elmo1320 | US",
        "jazellerzz7913@gmail.com:MUAj7913 | US",
        "JGarvin143@gmail.com:Lynxlover143 | US",
        "jmskg5@live.com:soccer745 | US",
        "joannamorris99@gmail.com:jojobean08 | US",
        "joannakamara@ymail.com:smartjojo123 | US",
        "joehanna.allen@gmail.com:w0lfgang | US",
        "kacie_4_11_14@yahoo.com:kacielynn | US",
        "shelby0731@gmail.com:Samkoda1 | US",
        "morgmillers@yahoo.com:Brat92mm | US",
        "memeric555@gmail.com:Nur$e2019 | US",
        "sierra.gladsee.sg@gmail.com:Sg100796 | US",
        "sayraflores238@gmail.com:sayra_oxo | US",
        "mctn21@yahoo.com:austin1990 | US",
        "prathmika.jha@gmail.com:Mika123jha | US",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)


@spotify.error
async def spotify_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#FORTNITE
#FORTNITE
#FORTNITE
#FORTNITE

@client.command()
@commands.has_permissions(send_messages=True)
async def fortnite(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -fortnite @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a fortnite account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "I think you dont read our Bot infortmation, so we dont have any of fortnite accounts",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)

@fortnite.error
async def fortnite_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

#ROBLOX
#ROBLOX
#ROBLOX
#ROBLOX

@client.command()
@commands.has_permissions(send_messages=True)
async def roblox(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -roblox @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a roblox account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "I think you dont read our Bot infortmation, so we dont have any of roblox accounts",
        "",
        "",
        "",
        "",
        "",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)

@client.command()
@commands.has_permissions(send_messages=True)
async def nordvpn(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type you name! -nordvpn @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a nordvpn account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "argelio.companioni@gmail.com:Argelio1",
        "alexthegreat8994@gmail.com:Sevenhate9",
        "noahjohnson15.nj@gmail.com:redline41",
        "josh@joshprice.net:stamakA5",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)

@nordvpn.error
async def nordvpn_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
@commands.has_permissions(send_messages=True)
async def uplay(ctx, member: discord.Member = None):
    if not member:
        await ctx.send("Please type your name! -uplay @name")
        return
    channel = discord.utils.get(member.guild.channels, name="generator-log")
    emb = (discord.Embed(description="Account Generator", color=0x2DF270))
    emb.add_field(name=f"A user created a roblox account", value=member.display_name, inline=False)
    emb.add_field(name=f"and the id is {member.mention}", value="check it", inline=False)
    await channel.send(embed=emb)
    await ctx.send("I send a Account to your DMs, please wait a bit. (I do allown the accs so i cant  refill it all weekends)")
    await asyncio.sleep(3)
    choices = [
        "shelleysmith2010@yahoo.com:red123",
        "michael_t@hughes.net:star69",
        "brooksiejam@aol.com:Koncua",
        "spartan_082@yahoo.com:daemon1",
        "thgenisis@yahoo.com:annie2195",
        "davwatts@bellsouth.net:clarkent",
        "blakemostafa@yahoo.com:pebble11",
        "soonersisk@yahoo.com:meg6468",
        "mybabybek@yahoo.com:bradpitt1",
        "corneliusdarionte@yahoo.com:ayanna",
        "riaelvargos@yahoo.com:June4747",
        "savagely_wicked@yahoo.com:kristen",
        "somphs@yahoo.com:mansDievs1",
        "mitchellstepp@yahoo.com:hpcomputer11",
        "sabdar2008@yahoo.com:goten8910",
        "patrick_jason12@yahoo.com:gsenjou10",
        "buschman112@yahoo.com:heaven1",
        "greed159@yahoo.com:Shadow1",
        "frogoa@yahoo.com:lafrogo2",
        "eugen_ciocea@yahoo.com:steaua",
        "jonathancollier@ymail.com:collier",
        "tony_vu94@yahoo.com:niffer12",
        "davidesp00@yahoo.com:nicdavnicdav",
        "orvilleide@yahoo.com:orv123",
        "annmarie_truong@yahoo.com:123truong",
        "friedman.david89@yahoo.com:Mymommy01",
        "akeisaunders@yahoo.com:amoney24",
        "iyskes@yahoo.com:packers",
        "volaregear@yahoo.com:uela8bee",
        "nbastreet4@yahoo.com:r0tten",
        "nathan.krakowski@yahoo.com:brooklyn01",
        "kreposa@comcast.net:Bellaluna",
        "cristiandreig@yahoo.com:newronx",
        "daravongsimon@yahoo.com:1xg56rty3",
        "hockeygabe45@yahoo.com:lgialbye",
        "guitarherolegend@sbcglobal.net:Coblivion2011",
        "robertjbrown1996@yahoo.com:durarara",
        "farkas.eduard@yahoo.com:Eduard12",
        "a_powers14@yahoo.com:powers14",
        "alecyurchenko@yahoo.com:232523op",
        "jacob.steel@ntlworld.com:jacob2002",
        "shannonpike2003@yahoo.com:Jesuschrist1",
        "kobenlock@yahoo.com:joshua69",
        "joe_baker1331@yahoo.com:bobflower",
        "charliepena315@yahoo.com:MVP4life",
        "descendantoftheson@yahoo.com:revival",
        "guamae@yahoo.com:piesR4you",
        "ngal2478@yahoo.com:Geltado99",
        "kyogerfan@yahoo.com:ilovemom2",
        "mandywerner@earthlink.net:1baker1",
        "joelgrant_au@yahoo.com:bluesky76",
        "chase@comcast.net:chase1",
        "thiantairas@yahoo.com:br1g4ndin3",
        "medic.stat@earthlink.net:1st508th",
        "mattpurcell39@yahoo.com:bmxrox11",
        "ethan134@yahoo.com:1cedcoffee",
        "costymen1996@yahoo.com:sharian2",
        "sirross1117@yahoo.com:crowfoot",
        "rossamaxwell29@yahoo.com:925raglov",
        "stadiumpulse@yahoo.com:shannen1",
        "oguillemette@yahoo.com:legoland",
        "daelarr789@yahoo.com:dave1963",
        "da.wongman@yahoo.com:kingz250",
        "mrhigh@comcast.net:1webster",
        "ajmiller0802@yahoo.com:blueeulb02",
        "bassettpro@yahoo.com:Marijuana1",
        "nysnowduzie@aol.com:rra6rom7669",
        "loganbeck492@yahoo.com:Baseball4",
        "dextariushero@yahoo.com:dna0799",
        "lukeellerbrook@yahoo.com:green2",
        "chipnash.5777@yahoo.com:sapphire75",
        "elijah.joki@yahoo.com:jellybean1",
        "bennyroyer@yahoo.com:Br8366",
        "lleaty@yahoo.com:Mickey25",
        "djstyle64@yahoo.com:sirstyles",
        "dyurteyevroman@yahoo.com:roman483",
        "tpun423@yahoo.com:mustang3",
        "shane.perry11@yahoo.com:Murphy123",
        "ssenter@charter.net:optics1",
        "pspimptha1st@yahoo.com:daredevil1",
        "presidentcalvin2@yahoo.com:moux26",
        "cameash2009@yahoo.com:hackin",
        "alexandra.elisa@yahoo.com:mancare",
        "jmm165@yahoo.com:digger6354",
        "kirbydog01@fuse.net:agincourt1",
        "alan.hulme3@ntlworld.com:laura211",
        "aznswagga203@yahoo.com:danielm1",
        "genasbusiness@yahoo.com:cheech",
        "justin_tic@yahoo.com:522522jt",
        "stan_daniel_marian@yahoo.com:maistro1",
        "bwong247@yahoo.com:bballer23",
        "jacksontabscott@rocketmail.com:Spike123",
        "ghost_eg_man@yahoo.com:assem123",
        "flashpoint911944@yahoo.com:domi1994",
        "kevinisawesome@bellsouth.net:thermal516122",
        "bilavioleta@yahoo.com:9nepasa",
        "jaswilkins@msn.com:LoLyo123",
        "gnjprice@msn.com:karson3323",
        "justanigga530@yahoo.com:Darkman1985",
        "ionut_stavarachi@yahoo.com:0080090071io",
        "bananaideala@yahoo.com:karina",
        "droppinjbombs@yahoo.com:J3ss3wil",
        "burkhaltermax@yahoo.com:vexy14289",
        "snipekg@yahoo.com:lol0lol",
        "cyberspaceboy@frontier.com:oldfart13",
        "kylepetersen48@yahoo.com:kyle98",
        "dylan.mincks@yahoo.com:flager500",
        "chrisrodier69@yahoo.com:water1",
        "reggie_183@yahoo.com:roadrunner18",
        "towerman5445@yahoo.com:ruby12",
        "beaugarbers@yahoo.com:adidas88",
        "a9300455@yahoo.com:peekaboo",
        "cyrusconnor2109@yahoo.com:cisco2109",
        "koda_hobby@yahoo.com:pimping15",
        "big_mo3@yahoo.com:hanan6xy",
        "jamiem753@earthlink.net:67chevelle",
        "nicolaswohr@yahoo.com:nick2mlt3",
        "pmarasciulo@yahoo.com:maggio",
        "mirali56@yahoo.com:alisaif567",
        "nichitaviorel@yahoo.com:nvg1234",
        "FabHyd69@yahoo.com:violet69",
        "dtownpimpinfoever@yahoo.com:wac3310",
        "lerej1@yahoo.com:nwadis1",
        "pokemon2241@yahoo.com:kenshin1",
        "loc93loc93@yahoo.com:Locpro93",
        "arsbrocca@yahoo.com:totalninety",
        "annlall@rocketmail.com:zkp123",
        "fillyfranks@yahoo.com:keaton09",
        "jaquariuscarothers@yahoo.com:buggy1",
        "phr33rsmembership@yahoo.com:potato123",
        "saro_sharma67@yahoo.com:sharma22",
        "spencerrock80@yahoo.com:foxbody",
        "royv722@yahoo.com:Rv112385",
        "mcgown.lewis@yahoo.com:emirates380",
        "justinneireiter@yahoo.com:Daniel18",
        "robin.gjerde@mail.com:Genser123",
        "divine457@comcast.net:runescape12",
        "brandon.hayter@yahoo.com:linkrulz1",
        "mexside_maniac@yahoo.com:MasterM2",
        "nicusorsimion07@yahoo.com:cristi",
        "coltonmcghee@yahoo.com:Godrocks23",
        "sher3897@yahoo.com:cudsue",
        "mikel87@yahoo.com:berlin87",
        "florawoods@ymail.com:sparkles",
        "batulio27@yahoo.com:theone27",
        "stanescuolimpiu@yahoo.com:arsinel",
        "ernlopez2000@yahoo.com:zepole",
        "sharpay333@att.net:Wildcats33",
        "sequel74501@yahoo.com:Fuck4758",
        "jrcorriere2002@yahoo.com:jcizzle301",
        "david_estep1981@yahoo.com:allie1006",
        "descurvydog805@yahoo.com:Monkey01",
        "isaacbrown955@yahoo.com:Radiation955",
        "alex19051988@yahoo.com:ciomu19051988",
        "hunterwedell@yahoo.com:reggy22",
        "nasimmons84@yahoo.com:Coward121",
        "adi21costi@yahoo.com:daniela",
        "michael.a.roberts@me.com:starswimmer93",
        "noid732@comcast.net:myluck1",
        "inly_damien@yahoo.com:naimadpop89",
        "abdirahmanwardere@yahoo.com:123abc",
        "tibi_tokos@yahoo.com:denisa",
        "nwb23uk@yahoo.com:transport",
        "joakin.angulo@yahoo.com:parasito",
        "mikelboomhower@yahoo.com:s310sg",
        "ninjadj11@aol.com:karate10",
        "cyann21@yahoo.com:jason73",
        "rd4in98@aol.com:cancun",
        "dorothyreid@msn.com:totototo",
        "hunterp0123@yahoo.com:Number60",
        "messager0013@aol.com:bbborgne13",
        "fabian_lancea@yahoo.com:aecnal",
        "coldaqua01@yahoo.com:heward11",
        "jailyn811@yahoo.com:william20",
        "deliobaeta@gmail.com:dio050181",
        "robertitoo@aol.com:Zaq12wsx",
        "nazeembenzainal@gmail.com:nazeem1999",
        "jacob4yq1@hotmail.com:Je159418",
        "snmfarr@hotmail.com:mayatony146",
        "spevin@o2.pl:apparition",
        "will.smither@mail.com:merlin11",
        "zuzka65@inmail.sk:zuzka65",
        "xx-enzoo-xx@hotmail.fr:cacacul01",
        "minibish21@hotmail.com:madbird",
        "kamileczekd95@o2.pl:undercover95",
        "chris.harcar@yahoo.com:perfect12",
        "cigeljgoran@yahoo.com:klopkosenegal",
        "forrestmoffat@yahoo.com:Addison9",
        "jacob.daniels38@yahoo.com:buster",
        "alikhsanclub@yahoo.com:bobobo7957",
        "r_norman48@att.net:budlight1",
        "templar.jenkies@yahoo.com:m71833",
        "marinecam2@hotmail.fr:Partenaire12",
        "petarr.horvat@yahoo.com:sollozzoo",
        "naiosulmasio@yahoo.com:cv1230",
        "mbrazzeal@yahoo.com:elostar3355",
        "arturslava2008@gmail.com:123124artur",
        "javiercamarenalozano@gmail.com:3helados",
        "danidanut98@yahoo.com:sebysan23",
        "adamgrusky@msn.com:Koolanole9",
        "ps701@yahoo.com:Great1916",
        "jun1orsr@yahoo.com:Santo213",
        "janecpix@yahoo.com:Cairnan6",
        "greg.fourseff@hotmail.fr:15mars1976",
        "gregory9972@wp.pl:hummerh2",
        "mephasto@freemail.hu:ae718075",
        "dmcdilda@comcast.net:35722k",
        "revolution25@hotmail.fr:bonemouth",
        "me_z00t@yahoo.com:immortal1",
        "mirela.bucur@rocketmail.com:parola555",
        "kschanda_jr@yahoo.com:Ks1069262871",
        "sp.eminem@centrum.cz:pppooonnnyyy",
        "paparakeshreddy2014@gmail.com:7660050279p",
        "shadowblade10000@yahoo.com:blade77521",
        "brajan.krzeminski@interia.pl:lego123ooo",
        "uthaleabhi@gmail.com:kehsihba1681994",
        "baugustova@seznam.cz:cholera",
        "mikeshomework2006@earthlink.net:kenny123",
        "morhe24@onet.eu:dwarf24",
        "smileycaleb@outlook.com:Chicago1",
        "midget810@comcast.net:creeper810",
        "simax_khiyaboon@yahoo.com:akpkreno",
        "flaviusemilian@yahoo.com:matryx1",
        "zachman.117@sbcglobal.net:Swindall117",
        "castoraz@hotmail.com:orazio54",
        "trixtora@mail.com:ceNzor",
        "thomas.saxton@ntlworld.com:atl290786",
        "goldrism@aol.com:father08",
        "comprat@takas.lt:hacker",
        "gpitelen@msn.com:dover1995",
        "tyler.amy@windstream.net:emmajo721",
        "alessandro.ragnoli@alice.it:jaco1999",
    ]
    rancoin = random.choice(choices)
    await ctx.author.send(rancoin)
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker")
    await member.remove_roles(role)
    role = discord.utils.get(ctx.guild.roles, name="Cracker Lite")
    await member.remove_roles(role)
    await asyncio.sleep(3600)
    role = discord.utils.get(ctx.guild.roles, name="User")
    await member.add_roles(role)

@uplay.error
async def uplay_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@uplay.error
async def uplay_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await channel.send(f"You do not have enough permissions {member.mention}")

@client.command()
async def gen(ctx):
    emb = (discord.Embed(description="SimpleGenerator Help", color=0x2DF270))
    emb.set_author(name="7sek")
    emb.add_field(name="-spotify", value="generate a spotify account", inline=False)
    emb.add_field(name="-fortnite", value="generate a fortnite account", inline=False)
    emb.add_field(name="-roblox", value="generate a roblox account", inline=False)
    emb.add_field(name="-minecraft", value="generate a minecraft account", inline=False)
    emb.add_field(name="-uplay", value="generate a uplay account", inline=False)
    emb.set_thumbnail(url="https://media.discordapp.net/attachments/399575754012229632/579027145628844033/8sek.png?width=676&height=676")
    await ctx.send(embed=emb)

client.run("NTgzMjg1NzM1MDQ2NTEyNjYw.XO6OdQ.6wbf1XObMT7Dt82Buy1DACYDBdo")
