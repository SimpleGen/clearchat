import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


TOKEN = "NTQ2MDc0OTEyMTAwNzEyNDQ4.D0i7dA.VuUbr7z0IWkl_45lqOfFehwWcZU"
client = commands.Bot(command_prefix=".")

Client = discord.client
Clientdiscord = discord.Client()

testmsgid = None
testmsguser = None
botmsg = None
msg = None

chat_filter = ["CUNT", "BITCH", "FOTZE", "NIGGER", "SCHLAMPE", "HUSO", "HURENSOHN", "JUDE", "SS", "HITLER", "ADOLF", "ADOLF HITLER", "NIGGA", "SLAVE", "SKLAVE", "JEWS", "KZ"]
bypass_list = []

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="-help"))
    print ("I am running on " + client.user.name)
    print ("With the ID: " + client.user.id)

@client.event
async def on_message(message):
    contents = message.content.split(" ")  # contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    emb = (discord.Embed(description="**THIS IS NOT COOL**", color=0x2DF270))
                    emb.add_field(name="**You have be warned! When you swaer one more time you are getting muted!**", value="so stop it, and read our discord rules!", inline=True)
                    await client.send_message(message.channel, embed=emb)
                except discord.errors.NotFound:
                     return

    if "!uplay" in message.content.lower():
        if "563954418794627094" in [role.id for role in message.author.roles]:
            if (message.channel.id == "553550376595619840"):
                variable = [
                    "totalspartan58@gmail.com:kyle1230",
                    "teshone00@gmail.com:cam1152114",
                    "jacob.hagelq@hotmail.se:jahjah09",
                    "pnotching@gmail.com:renate77",
                    "kgaska9@gmail.com:orzelek987",
                    "bremenpascal@web.de:Werder1710",
                    "Nate.1.lehrke@gmail.com:Irongut1",
                ]
                await client.send_message(message.author, (random.choice(variable)))
            else:
                await client.wait_for_message(timeout=10)
                await client.delete_message(message)
                await client.send_message(message.channel, "Type **donate** in the chat to buy the Simple rank")
        else:
            await client.send_message(message.channel, "Type **donate** in the chat to buy the Simple rank")

    if "!fortnite" in message.content.lower():
        if "544185564275146813" in [role.id for role in message.author.roles]:
            if (message.channel.id == "553550376595619840"):
                variable = []
                await client.send_message(message.author, (random.choice(variable)))
            else:
                await client.wait_for_message(timeout=10)
                await client.delete_message(message)
                await client.send_message(message.channel, "Type **donate** in the chat to buy the Simple rank")
        else:
            await client.send_message(message.channel, "Type **donate** in the chat to buy the Simple rank")

    if "!minecraft" in message.content.lower():
        if "544930512209444876" in [role.id for role in message.author.roles]:
            if (message.channel.id == "553550376595619840"):
                variable = []
                await client.send_message(message.author, (random.choice(variable)))
            else:
                await client.wait_for_message(timeout=10)
                await client.delete_message(message)
                await client.send_message(message.author, "use the #❗»-generator channel")
        else:
            await client.send_message(message.channel, "Subscribe `yCode` and send Moderator or a Admin a Screen!")

if "!spotify" in message.content.lower():
    if "544930512209444876" in [role.id for role in message.author.roles]:
        if (message.channel.id == "553550376595619840"):
            variable = [
                "e_selam@yahoo.com:3600",
                "juz24_tine@yahoo.com:roxyrose",
                "Ayanalady614@yahoo.com:loverpooh",
                "virusjun2@yahoo.com:boomaui",
                "wickedson66@yahoo.com:218078",
                "danread7@yahoo.com:eee7385",
                "jljacques2@yahoo.com:1michele",
                "adunsmor1@yahoo.com:allison1",
                "synicyde@yahoo.com:intolerance",
                "gpark75@yahoo.com:gardenia",
                "farzin.tirgar@yahoo.com:123456",
                "rriley0427@yahoo.com:jordan0427",
                "heckycolazo@yahoo.com:favour",
                "twistedkornkid66@yahoo.com:qazzaq",
                "kevsoles@yahoo.com:morgus",
                "deannacaprini@yahoo.com:xena1982",
                "aynurs06@yahoo.com:121518",
                "moorebrandon33@yahoo.com:curtychew",
                "hannahbrady@yahoo.com:thailand08",
                "biancadiaz08@yahoo.com:09181989",
                "charlietaylorjr@yahoo.com:124255fbds",
                "jforey13@yahoo.com:jxj1313",
                "fa_armywife@yahoo.com:allana22",
                "judfan101@yahoo.com:sampson",
                "christophizzle4@yahoo.com:son123",
                "jpbeaudin@yahoo.com:godzilla2000",
                "hnsoares@yahoo.com:tinbird28",
                "theradicalwriter@yahoo.com:121187",
                "jmedrano76@yahoo.com:1badmex26",
                "alix3cia@yahoo.com:love2589",
                "twdsuper@yahoo.com:529707",
                "manowelborn@yahoo.com:shaniah06",
                "majah_pearl@yahoo.com:janebantoc",
                "rayc_ray@yahoo.com:ray623",
                "shaquelaboyd@yahoo.com:december13",
                "aayatullahi@yahoo.com:Adam45",
                "rlarkin_06@yahoo.com:mariah",
                "vwattsup@yahoo.com:100watts",
                "langford_1979@yahoo.com:hello27",
                "pjea090@yahoo.com:graham",
                "gphio_ximo1@yahoo.com:houston1",
                "henrycisneros89@yahoo.com:mafioso89",
                "jondaman54@yahoo.com:sidekick3",
                "kingdimmd82@yahoo.com:edgar1",
                "misz_mieyzuera86@yahoo.com:z07686",
                "gabrielvinzent@yahoo.com:nov162005",
                "dat_nigga_roy@yahoo.com:solomon",
                "suhwit_babe@yahoo.com:162889",
                "furioku69@yahoo.com:dbzdbz",
                "stonecold10189@yahoo.com:yankees31",
                "j.hauser27@yahoo.com:hockey27",
                "angelica1428@yahoo.com:poohbear87",
                "ckep1976@yahoo.com:guitar76",
                "malupit_3@yahoo.com:kamekaze",
                "chiefscottus@yahoo.com:beanie",
                "mpamaran@yahoo.com:Singap0re",
                "mylenediciembre719@yahoo.com:lemyne22",
                "joey_golamco@yahoo.com:andrea415",
                "spear0w@yahoo.com:komputer",
                "damiansully@yahoo.com:kundalini",
                "jsugail@yahoo.com:robert48",
                "jburkhart37@yahoo.com:007lurch",
                "delicia.harris@yahoo.com:dhluv4tj",
                "maryana_ha@yahoo.com:challenger",
                "jurassicpark_1999@yahoo.com:rusty1",
                "bacnberger@yahoo.com:buddy17",
                "lmcneal28@yahoo.com:dayja01",
                "rthomas08@yahoo.com:georgia08",
                "dixietruckr@yahoo.com:2001f250",
                "shelbyschanaman@yahoo.com:loveable12",
                "blastfaizu2@yahoo.com:nobuyus",
                "littletom12957@yahoo.com:shortman",
                "mgtilk@yahoo.com:lilwayne",
                "gakibapi@yahoo.com:imagineering",
                "bryancoog0719@yahoo.com:ashlynn1",
                "dyshanaerobinson@yahoo.com:vanessa",
                "whitstr09@yahoo.com:ch3rryma",
                "bbgood92@yahoo.com:brynn1",
                "yume_erysd@yahoo.com:eds459",
                "deerhuntr04@yahoo.com:stealth",
                "sarbu_192@yahoo.com:handsom",
                "charlescruz1986@yahoo.com:clapback",
                "charlescruz1986@yahoo.com:clapback",
                "addyphonasa@yahoo.com:kaitlinh1",
                "kuisma_8@yahoo.com:ginger88",
                "real.cripsz24@yahoo.com:cripside",
                "pancake.1959@yahoo.com:6959cake",
                "kcxcbb5@yahoo.com:trexit5",
                "papitchy@yahoo.com:fuckkkkk",
                "mohdyuzreen@yahoo.com:dav2065",
                "enanotomix@yahoo.com.mx:predacons",
                "jpeso43@yahoo.com:eagles",
                "body_pump69@yahoo.com:sildenafil",
                "w_donner@yahoo.com:shamokin",
                "britni4love@yahoo.com:gina9909",
                "youngmagic2@yahoo.com:123qwe",
                "tony_sumartono@yahoo.com.sg:mandar21",
                "alexwarr75@yahoo.com:bubbles75",
                "ramer_alvaran@yahoo.com:RAMRED",
                "joe_ann_louise@yahoo.com:rugtoy007",
                "ngandinh89@yahoo.com:hlhbn122",
                "angging@yahoo.com:angging",
                "cameronmaghami@yahoo.com:fuckyou12",
                "nfields43@yahoo.com:pmw4life",
                "ritchdawg24@yahoo.com:eileen66",
                "trudylou2000@yahoo.com:spriggy",
                "rafgonz43@yahoo.com:26532653",
                "oakdeja@yahoo.com:dlw143",
                "jalam007@yahoo.com:lemon722",
                "johngretch1245@yahoo.com:minnoo",
                "prakash35@yahoo.com:liverp001",
                "singleton3312@yahoo.com:sandra62",
                "roshongibson@yahoo.com:new2you",
                "smashingfalcor@yahoo.com:schumacher",
                "jhnmuso@yahoo.com.au:italian1",
                "juaniaguilera@yahoo.com.ar:humoprick",
                "jalenwilliams52@yahoo.com:blacklips9",
                "marie2989@yahoo.com:marie1",
                "morphios3@yahoo.com:landlr3",
                "cvalenzu7@yahoo.com:10548465",
                "volfan0118@yahoo.com:05210923",
                "beautifullbeatrice@yahoo.com:091503",
                "maggiebgooden@yahoo.com:maylee42",
                "ahmadnazirul@yahoo.com:kaiser19",
                "mstdk78@yahoo.com:jumper78",
                "musico@yahoo.com:musico",
                "jellybean5703@yahoo.com:polo419",
                "dilkirani678@yahoo.com:samia1989",
                "kolmisfit@yahoo.com:abc123",
                "electricdrip1488@yahoo.com:tightenup",
                "dschalow71@yahoo.com:spencer01",
                "raven_frozen15@yahoo.com:raven123",
                "msshea4@yahoo.com:celest44",
                "showguy77@yahoo.com:janjan",
                "adolph_gallegos2000@yahoo.com:sydney",
                "jjastan@yahoo.com:jologs",
                "mayfa99@yahoo.com:maya2002",
                "michael.roginski@yahoo.com:sigmund1",
                "zack_jz566@yahoo.com:blackgear",
                "mantukasz99@yahoo.com:mantas",
                "jamescgrady@yahoo.com:mopar70",
                "arshellan@yahoo.com:shaela13",
                "carlamayfieldcm@yahoo.com:ginger777",
                "jeffreyphillips1965@yahoo.com:tentflow18",
                "nimapafio70@yahoo.com:confidence2",
                "Fransthe1@Yahoo.com:gp021488",
                "mayme.neech@yahoo.com:ruthven",
                "shakitaferguson@yahoo.com:openclub05",
                "brentmeche@yahoo.com:mazda03",
                "chatwithfolykay@yahoo.com:kayode",
                "slash15gnr@yahoo.com:slash161",
                "flaca10458@yahoo.com:poti735",
                "fingersaves2000@yahoo.com:soccer21",
                "pdmather@yahoo.com:bollox",
                "wonderweed2004@yahoo.com:4100124",
                "lisaernlund1@yahoo.com:lisa8453",
                "Soraisdaking@yahoo.com:jenova",
                "leejorae@yahoo.com:movies",
                "pe_yangdalhour@yahoo.com:patlikuhl",
                "joyjoy@yahoo.com:joyjoy",
                "lhgodoy@yahoo.com:godoy123",
                "jardine51050@yahoo.com:jayden01",
                "mkescano@yahoo.com:malitbog",
                "narutoxxninja@yahoo.com:a787555",
                "josh4950@yahoo.com:iceman123",
                "Tonia_blessed@yahoo.com:Devryu09",
                "ayarci11@yahoo.com:2422519",
                "jg_4826@yahoo.com:hobbit45",
                "inara_1500@yahoo.com.ph:czx514ro",
                "florin_cipmar@yahoo.com:viorica",
                "epagnucc@yahoo.com:jordan23",
                "masterkey_gen@yahoo.com:shyrshyr",
                "mufitneftci@yahoo.com:20001900",
                "roberthayward11@yahoo.com:robert11",
                "nitwhit26@yahoo.com:spookie08",
                "blessed@yahoo.com:blessed",
                "bobcat752000@yahoo.com:Germany05",
                "flexizzel@yahoo.com:chantilly1",
                "rld1027@yahoo.com:qwerty10",
                "chowie204@yahoo.com:trident1",
                "jsp200268o@yahoo.com:sergio01",
                "destrell1@yahoo.com:baseball101",
                "rejhie_04@yahoo.com:110489",
                "princeawill@yahoo.com:sidekick3",
                "abjack12@yahoo.com:iotwc12",
                "wala_ako11@yahoo.com:hugs0226",
                "mermaid8116@yahoo.com.sg:spring81",
                "ericd.wbsd@yahoo.com:bbooc44y",
                "dormique@yahoo.com:bronzeroad48",
                "thatgooch79@yahoo.com:l06212003",
                "silencer_v@yahoo.com:reiayanami",
                "illapaco@yahoo.com:sexo00",
                "ckitts723@yahoo.com:july231988",
                "daniel_060113@yahoo.com.my:aini5524",
                "ibaloiller@yahoo.com:1qw2e3r",
                "angela26292@yahoo.com:892163b",
                "clyde_denzel@yahoo.com:hustla101",
                "quantum_org@yahoo.com:721125",
                "ogpereira2007@yahoo.com.br:ops123",
                "laurenshep06@yahoo.com:classof06",
                "Sabrinatiffa@yahoo.com:121192",
                "secret_life_of_amaranth@yahoo.com:marinda",
                "blue2flue@yahoo.com:123456",
                "chris_burdette63@yahoo.com:bananas4",
                "scmiller_144@yahoo.com:beatdadrum",
                "jeromednn@yahoo.com:121597",
                "mattman0396@yahoo.com:babylily0396",
                "j_blackwind@yahoo.com:j314159276",
                "cridgeway92@yahoo.com:cupcake92",
                "lalaw1917@yahoo.com:sydni0189",
                "generaal_jc@yahoo.com:qwerty123456",
                "rickshawbell@yahoo.com:nascar88",
                "cloverdale1477@yahoo.com:Kalista1",
                "redstoneslimited@yahoo.com:nb567574",
                "haidashamsuri@yahoo.com:100785",
                "crich892003@yahoo.com:noonie128",
                "geraldzkee2006@yahoo.com.ph:342424",
                "kary12202002@yahoo.com:yessenia1",
                "Mztrice254@yahoo.com:jalesia",
                "farhana_kamaruddin@yahoo.com:hahnenfuss",
                "haavimurflis@yahoo.com:020273",
                "gjsr216@yahoo.com:camaro",
                "laeparker@yahoo.com:diaz1141",
                "mabz_duce@yahoo.com:balderdash",
                "florin_chello2008@yahoo.com:dickhead",
                "loouuridr@yahoo.com:andrei11",
                "avysma911@yahoo.com:avery1",
                "ellanox@yahoo.com:angela",
                "tbelt26@yahoo.com:password",
                "billyk142857@yahoo.com.hk:6c08118",
                "m6r6a6@yahoo.com:19881367",
                "droc724@yahoo.com:outcold",
                "medicpm2001@yahoo.com:metro38",
                "waynesimple@yahoo.com.hk:2100841908",
                "adelinewjp@yahoo.com.sg:4oxyr0xy",
                "crapsguy58@yahoo.com:thk22758",
                "azrul_037@yahoo.com:muassyarah",
                "radogna0071v@yahoo.com:viper007",
                "aserbin13@yahoo.com:maurice13",
                "thomas_farley2008@yahoo.com:nicole09",
                "kacmom46366@yahoo.com:brighteyes",
                "dukehallmark@yahoo.com:smokes1",
                "corey_poncedeleon@yahoo.com:yeroc2490",
                "red_taurus30@yahoo.com:198080",
                "alyssalipps@yahoo.com:speedy01",
                "chucky_donta@yahoo.com:chucky123",
                "Champalex812@yahoo.com:a659186",
                "ohyeahwhammy@yahoo.com:redsox1",
                "rj_jardeleza18@yahoo.com:1810rj10",
                "cma338@yahoo.com:acorn1234",
                "v_vragovski@yahoo.com:ferari",
                "ikwan371@yahoo.com:iwan2484",
                "ozgurtureli@yahoo.com:10121012",
                "mak_642001@yahoo.com:perspolis",
                "bmcclell23@yahoo.com:fungos",
                "hotknickfan@yahoo.com:knicks",
                "teley555@yahoo.com:tyty555",
                "t_dogg2420@yahoo.com:infinity1",
                "lizzlefizzie@yahoo.com:emerger86",
                "lizzlefizzie@yahoo.com:emerger86",
                "aimee_cia@yahoo.com:04281994",
                "coolguy_usman@yahoo.com:1234qwer",
                "david_t_fenske@yahoo.com:fenske",
                "p.dbradley1@yahoo.com:3101501",
                "c_pontesor@yahoo.com:carac3",
                "mmdp86@yahoo.com:210586",
                "YJsnowman437@yahoo.com:593599",
                "kecyx_shah@yahoo.com:terminal",
                "s_carey2008@yahoo.com:tinker08",
                "pingu4liv@yahoo.com:beauty",
                "tonymianulli@yahoo.com:bigballen1",
                "kristen.smith89@yahoo.com:colgate1",
                "angiemo84@yahoo.com:pumpkin22",
                "step0007@yahoo.com:babies04",
                "latifa5781@yahoo.com:kaktan21",
                "xlizziexhooverx7@yahoo.com:nigro8",
                "einemal@yahoo.com:alex00",
                "jasmin.white@yahoo.com:jass23",
                "tarheelt107@yahoo.com:pistolpete",
                "kenpepper26@yahoo.com:derky426",
                "fearmelol48@yahoo.com:merlin211",
                "elbaskin@yahoo.com:jazz111",
                "limexxvii@yahoo.com:herrera",
                "igo2serina@yahoo.com:fwgocc1",
                "marloubarabar@yahoo.com:031576",
                "travelkeys@yahoo.com:ktogsucks",
                "dtd500@yahoo.com:beastdtd",
                "miracle014@yahoo.com:hot123",
                "rz_scorp@yahoo.com:wmf14999",
                "glacious_99@yahoo.com:iceman99",
                "jasmineflower32@yahoo.com:adrian2002",
                "hoodhoppa135@yahoo.com:1me2you3us",
                "aishahousman@yahoo.com:calvin22",
                "kentrellalexander@yahoo.com:blue94",
                "primozicsb14@yahoo.com:dzgal214",
                "sikeston1213@yahoo.com:sikeston",
                "jayc0l@yahoo.com:asshole",
                "arieskck@yahoo.com:610000",
                "angela92nguyen@yahoo.com:thethe",
                "selman_asik@yahoo.com:eminem",
                "richellesaclot@yahoo.com:vistamar",
                "whynmy@yahoo.com:invictus",
                "stsebastian00@yahoo.com:2615492",
                "olarndrafflesia@yahoo.com:akudankau7",
                "yuno_0111@yahoo.com:987540",
                "lung650417@yahoo.com.tw:kyle860512",
                "courtneyrulez501@yahoo.com:courtney",
                "paf01@yahoo.com:chhs4sc",
                "wyomarty0@yahoo.com:guinness",
                "evildoer247@yahoo.com:chromeo1",
                "opksusa@yahoo.com:13051970",
                "stephlja@yahoo.com:kandre",
                "colorblindmini@yahoo.com:flubber",
                "robin.strike@yahoo.com.br:blackon",
                "tkozlowski73@yahoo.com:freddie",
                "paysondad@yahoo.com:dodger",
                "lala1705@yahoo.com:141725",
                "muhimman@yahoo.com:muhammad",
                "boladao_28@yahoo.com.br:201194",
                "ray_jacksonjr@yahoo.com:shawn23",
                "lia_crear@yahoo.com:jesus777",
                "sizzleja2@yahoo.com:iluvajs1",
                "charmainesmiley@yahoo.com:tiffany",
                "sshah07424@yahoo.com:dell1234",
                "angieangie587@yahoo.com:25528as",
                "bobjohnson2662@yahoo.com:sugarbear",
                "jessica_medina69@yahoo.com:010591",
                "tchuppaman@yahoo.com:miezzu",
                "allinson_777@yahoo.com:ladalad123",
                "aim_cg@yahoo.com.mx:17017777",
                "murphyemma2006@yahoo.com:36622006",
                "afesguy@yahoo.com:kimchi72",
                "seli059@yahoo.com.my:130059",
                "bernadettebalan@yahoo.com:mahalko53",
                "personaljesus34@yahoo.com:batcave36",
                "mdclaire@yahoo.com:lovely",
                "katiekisel77@yahoo.com:millerlite1",
                "kaciwillis@yahoo.com:iloveyou33",
                "swordmaster_misty@yahoo.com:polkadolka",
                "omkar.london@yahoo.com:311983",
                "yairofek@yahoo.com:ofek1975",
                "los_831@yahoo.com:cenco831",
                "tanchelle75@yahoo.com:snook12",
                "demeza3@yahoo.com:tampabay3",
                "aye79876a@yahoo.com:abigail25",
                "niaoctavia12@yahoo.com:cheetahgirlz",
                "julie_dimond@yahoo.com:hokeypokey",
                "fresno22@yahoo.com:11271127",
                "krichardson0614@yahoo.com:destiney4",
                "rby987@yahoo.com:789123",
                "cowjuan@yahoo.com:garofano1",
                "car_dog_garage@yahoo.com:0toluca",
                "nj_starry@yahoo.com:starrynight",
                "jamaliah26@yahoo.com.sg:261275",
                "cigdemcokan@yahoo.com:02082007",
                "jwhit20042000@yahoo.com:jennifer",
                "keks520@yahoo.com:morrie",
                "are_jazz87boy@yahoo.com:jazz87",
                "jandymeza@yahoo.com:chris89",
                "my_agnes2k7@yahoo.com:forgot",
                "blewish_girl@yahoo.com:eika1991",
                "garrisonmp@yahoo.com:michael4",
                "redman1799@yahoo.com:baseball",
                "chalimar00@yahoo.com:shabba00",
                "darksage881905@yahoo.com:sticknija1",
                "frananjo05@yahoo.com.br:fsanti",
                "gestigoy@yahoo.com:navigators",
                "sapanu@yahoo.com:sapzal08",
                "nairda72-1@yahoo.com:webpass",
                "carlos_sl@yahoo.com:megawatt",
                "kooncetia@yahoo.com:inthecut31",
                "itslalyndsey@yahoo.com:power3",
                "ritaantonascio@yahoo.com:rita1521",
                "seadawg0831@yahoo.com:goober98",
                "shizune717@yahoo.com:supercow1",
                "penn_no1@yahoo.com:deathrow",
                "pavilionmms@yahoo.com:622622",
                "rocker4012@yahoo.com:raider56",
                "alp_uz@yahoo.com:au0144a",
                "cscreza@yahoo.com:molavi",
                "mrstray420@yahoo.com:namzug",
                "jeassyca.ngaditeja@yahoo.com:eleonora",
                "strahinjic_ds@yahoo.com:medvedja",
                "reddragon0205@yahoo.com:336699",
                "reality04@yahoo.com:sammie",
                "lucie05678@yahoo.com:hotdog",
                "tarheals56@yahoo.com:wtpbikes",
                "octavia142006@yahoo.com:octavia",
                "kimberlychavez71@yahoo.com:emma12",
                "prowess_24@yahoo.com:yenris",
                "dpikeii@yahoo.com:darts33",
                "mgyldz@yahoo.com:starbuck",
                "mandooogurlx3@yahoo.com:mandoogook",
                "yanksrul224@yahoo.com:baseba123",
                "jun_cloa@yahoo.com:cs122399",
                "kazcus@yahoo.com:Belgariad1",
                "uhollandfour@yahoo.com:Holland4",
                "jessewilson87@yahoo.com:clemson2",
                "casillasangelo@yahoo.com:4858pw",
                "chris27stout27@yahoo.com:keyboard27",
                "jaymonster13@yahoo.com:2004ram",
                "saintpauldavid@yahoo.com:matt6330",
                "djfroy@yahoo.com:froy2301",
                "averynicholas21@yahoo.com:gymdude23",
                "nitaboo14@yahoo.com:danita16",
                "hilcobroens@yahoo.com:crowbar666",
                "tonysoccerasp91@yahoo.com:tony2010",
                "ashley.joseph94@yahoo.com:desirae212",
                "mario_j0se_valdez888@yahoo.com:mariojose",
                "jkat_0219@yahoo.com:kingkong",
                "obet_ragos@yahoo.com:etong123",
                "jacobjones97@yahoo.com:drake1",
                "myashtree@yahoo.com:115691",
                "autumnbones@yahoo.com:jayden214",
                "reydownes@yahoo.com:Hudson08",
                "jeweler1977@yahoo.com:stacey76",
                "brwneyedgirlmace@yahoo.com:jazmyn07",
                "abg_designs@yahoo.com:dagwood",
                "peppermintpattie22@yahoo.com:sierra1162",
                "athirah410@yahoo.com:901004",
                "bogdancapatina@yahoo.com:aide6make",
                "cshell816@yahoo.com:Crndgg74",
                "aniceto.lorelei@yahoo.com:lorelei123",
                "lance_hghs@yahoo.com:hughdog2",
                "mgarven25@yahoo.com:garvme19",
                "kcairo56@yahoo.com:sisqo5608",
                "cj_hagii@yahoo.com:hagiii",
                "reygim_01@yahoo.com:glereyjur",
                "platv2006@yahoo.com:ScoobyDoo",
                "mahyar_he@yahoo.com:8800gt",
                "tito_b415@yahoo.com:concdid1",
                "amzver1@yahoo.com:030407",
                "aydemirtozluyurt@yahoo.com.tr:14531071",
                "rashamell2000@yahoo.com:rashamel",
                "edsname03455@yahoo.com:raiders",
                "cosmicom2000@yahoo.com:cosmin1984",
                "catridr2000@yahoo.com:george22",
                "karandinos@yahoo.com:123321mk",
                "kbrenes96@yahoo.com:number1",
                "tiplea84@yahoo.com:vasile84",
                "dnllstrong@yahoo.com:jayden",
                "neringuteee@yahoo.com:19871806",
                "ernz77@yahoo.com:abcde757",
                "sergio_gdelat@yahoo.com:222222",
                "mz.jasz@yahoo.com:1mzjasz",
                "jmurphy4677@yahoo.com:drdre666",
                "bblay4@yahoo.com:oicu812",
                "katriesh@yahoo.com:kateey1",
                "doughboypillz@yahoo.com:dough08",
                "dreli_20@yahoo.com:elias123",
                "bwiw568@yahoo.com:reklwa1",
                "dammy3000@yahoo.com:dami4u",
                "chelew27@yahoo.com:thomas1928",
                "annie111192@yahoo.com:luverne11",
                "yeraniabarrios@yahoo.com:217645",
                "neesi70@yahoo.com:joshben",
                "butch145@yahoo.com:dawgs45",
                "buttercup318043@yahoo.com:maddie9122",
                "kel0217@yahoo.com:kelann01",
                "utmel81@yahoo.com:braden04",
                "racky_john@yahoo.com:tracy1",
                "niyah92@yahoo.com:pink27",
                "hotgurl_1104@yahoo.com:iloveme4",
                "yungrad07@yahoo.com:christy1",
                "nic_ng123@yahoo.com.sg:951753",
                "jvpot@yahoo.com:090985",
                "Kings_1015@yahoo.com:jojo1015",
                "oakboi93@yahoo.com:payroll",
                "brianb130@yahoo.com:zxcvbnm1",
                "Angel86c@yahoo.com:Smiles1",
                "blstz_5264@yahoo.com.my:taa123",
                "blstz_5264@yahoo.com.my:taa123",
                "paul_tristan429@yahoo.com:sharingan",
                "nur_rasyiqah@yahoo.com:nrr220987",
                "Kauisha@yahoo.com:bigish",
                "jlevera@yahoo.com:779614",
                "b.hall07@yahoo.com:chanay6",
                "geo3232@yahoo.com:george27",
                "amiraizzat77@yahoo.com:blue77",
                "j.barnicle@yahoo.com:liverpool",
                "bluebaycanyon@yahoo.com:forklift",
                "ontha_dl2003@yahoo.com:cs60195",
                "traviskissacdc@yahoo.com:coolest91",
                "carpediemrz@yahoo.com:w18816",
                "csibi_reka@yahoo.com:kiskutya",
                "nadiakhussain@yahoo.com:sunflower",
                "beachbabechic34@yahoo.com:jessica13",
                "ciara09cece@yahoo.com:deshawna1",
                "shelbyw_1993@yahoo.com:purple",
                "massagimartinez@yahoo.com:alyssa1",
                "ttheu@yahoo.com:taylor05",
                "aznizanieyza@yahoo.com:860426",
                "asb0923@yahoo.com:bongloads",
                "ffjoec@yahoo.com:frontroom1",
                "arsyaridwan@yahoo.com:224336",
                "Latricelkb@yahoo.com:Lovely125",
                "Bmejia3522@yahoo.com:Funny13",
                "missbiggs30@yahoo.com:honeydip24",
                "mi445566@yahoo.com:june82002",
                "zhelga@yahoo.com:vida1111",
                "srmrmm@yahoo.com:mbaby2",
                "cythack@yahoo.com:spike78",
                "madjstfou@yahoo.com:Melvin91",
                "hernandez.alexiz@yahoo.com:a101010",
                "stanisha29@yahoo.com:sunsettan",
                "calisurf2008@yahoo.com:5700opal",
                "numa2329@yahoo.com:track8",
                "johnsama82@yahoo.com:sammer82",
                "kfaggiano@yahoo.com:katie210",
                "sexyduke90@yahoo.com:renelda90",
                "carvergreen@yahoo.com:tiatre",
                "rebocorny@yahoo.com.br:renata",
                "strung_out80@yahoo.com:cherubim",
                "demetrius.redding@yahoo.com:jamesr",
                "ruselgun@yahoo.com:manowar",
                "luizinhosantiago@yahoo.com:chiquilla1",
                "danhaimckenzie@yahoo.com:9938060da",
                "tiveyburks@yahoo.com:24352435",
                "danitrani7@yahoo.com:florida",
                "drekearse@yahoo.com:vikings1",
                "crispereiracps@yahoo.com.br:032203",
                "jasondplacetobe@yahoo.com:godfather",
                "jimellefson@yahoo.com:char1ie",
                "pinksrl@yahoo.com:september3",
                "pinksrl@yahoo.com:september3",
                "goodred2@yahoo.com:allpub31",
                "sampson_cott@yahoo.com:daddys82",
                "twintowers80@yahoo.com:4575",
                "jadol_12@yahoo.com:badooy",
                "darin1891@yahoo.com:fatgirl",
                "reginald_gilbert@yahoo.com:31reggie",
                "hobart_michael@yahoo.com:xxx420",
                "tbdeepcover@yahoo.com:january26",
                "sanderskg@yahoo.com:linksys23",
                "cardsbigmac25@yahoo.com:jayhawk34",
                "alisha_young0919@yahoo.com:tootsie09",
                "edithadorno@yahoo.com:sept1989",
                "ummicle@yahoo.com:spiderman",
                "trixxxie_baby@yahoo.com:trix062204",
                "morgannachuk@yahoo.com:cookie3",
                "naj_2003@yahoo.com:superman",
                "randi.dixon@yahoo.com:cupcake57",
                "akonseant@yahoo.com:114276",
                "joshchapmen@yahoo.com:konoha",
                "demsol_demsol@yahoo.com:youallknow",
                "myq425@yahoo.com:quella2001",
                "johnnycamp10@yahoo.com:redmen",
                "mgading74@yahoo.com:pussy1971",
                "crystalb21@yahoo.com:ocean76",
                "famance_13@yahoo.com:139145",
                "carmen_piglet@yahoo.com:18031980",
                "ramon_aquino69@yahoo.com:oongas",
                "mhikma@yahoo.com:mandar",
                "evboy88@yahoo.com:2007040",
                "j_roberson_972@yahoo.com:dtexas972",
                "tjcolina@yahoo.com:godsfavor",
                "cassy1238@yahoo.com:kittycass",
                "Nswingfan@yahoo.com:piper0518",
                "el_mar_y_sol@yahoo.com:kael2008",
                "krazteka13@yahoo.com:aztlan69",
                "joey.bunn@yahoo.com:toyota",
                "alex831@yahoo.com:alex",
                "the_revl954@yahoo.com:xxxxxx",
                "complicateddy@yahoo.com:diana123",
                "ersunakay@yahoo.com:5303690",
                "kelseylynn1025@yahoo.com:hood16",
                "thebighardsun@yahoo.com:213960",
                "srt4navy@yahoo.com:srt4navy",
                "certified_cutie_04@yahoo.com:ripdoc",
                "Christina_harris80@yahoo.com:tristan1",
                "wrr13@yahoo.com:dunken13",
                "tmb52377@yahoo.com:danceschool",
                "delmyvasquez34@yahoo.com:tiger123",
                "susanned5450@yahoo.com:sd1319",
                "viviandriopoulou@yahoo.com:2211",
                "ekojck@yahoo.com:238190",
                "lauroreis@yahoo.com.br:quicken",
                "trapps11@yahoo.com:rocco",
                "joshakerson28@yahoo.com:wrestling",
                "ryan.guay@yahoo.com:reg341128",
                "medi_sin_man@yahoo.com:brennan",
                "jayphil44@yahoo.com:silverio4",
                "torresh21@yahoo.com:sama1206",
                "PinkeSwear@yahoo.com:Savannah1",
                "syafique_mw@yahoo.com.my:110888",
                "bgoodson18@yahoo.com:nsyncfan",
                "ceeross7@yahoo.com:tbangers1",
                "chriscmallard@yahoo.com:ichthus",
                "rpatten@yahoo.com:onefour55",
                "tricia_1288@yahoo.com:softball",
                "djses76@yahoo.com:getmoney1",
                "anavipereira@yahoo.com.br:230296",
                "mchal_ls@yahoo.com:jesus1",
                "roch_chelle_29@yahoo.com:ellechor",
                "allexis.goodwin@yahoo.com:babygurl14",
                "allexis.goodwin@yahoo.com:babygurl14",
                "l.devoliere@yahoo.com:panthers",
                "warchol6@yahoo.com:joyof4boys",
                "s_kairn@yahoo.com:chaz1997",
                "afy_xa@yahoo.com:hafiza",
                "iamphil2008@yahoo.com:2790w00t",
                "iamphil2008@yahoo.com:2790w00t",
                "ireyesnmf@yahoo.com:nyasia418",
                "Remy85601@yahoo.com:0879Pierre",
                "gemini234@yahoo.com:gemini234",
                "tlanouette@yahoo.com:lee123",
                "c_hannula24@yahoo.com:jondas8i",
                "angelique_lewis59@yahoo.com:disneyp2",
                "ccmghana@yahoo.com:wanderer",
                "bv_minero@yahoo.com:bernard",
                "gregscorza@yahoo.com:greg07",
                "ack18@yahoo.com:goalie69",
                "ayanah228@yahoo.com:missdiva",
                "gtr1328@yahoo.com.tw:06281328",
                "bryaniseffect@yahoo.com:andrew",
                "martitacervantes1978@yahoo.com:regis1978",
                "iheartcheer320@yahoo.com:dixie320",
                "cj.nwuju@yahoo.com:gold6325",
                "czarina_diwa@yahoo.com:czarmaine",
                "ref_3105@yahoo.com:jjf111",
                "nntharp@yahoo.com:marino",
                "noaction08@yahoo.com:aksi08",
                "chea3313@yahoo.com:101879",
                "TrevinnoS@yahoo.com:onelove919",
                "alissa_reidy@yahoo.com:poppy1111",
                "mammasanford@yahoo.com:mizzer",
                "axmal11@yahoo.com:pesona77",
                "paulineappel@yahoo.com:121200",
                "blueying118@yahoo.com.hk:yingying",
                "domskie_1382@yahoo.com:011382",
                "techno_is_life@yahoo.com:2093045",
                "korykid_1@yahoo.com:love99",
                "knudko@yahoo.com:2911pm",
                "franksmith12344@yahoo.com:leeona1",
                "im_@yahoo.com:123456",
                "srseminole@yahoo.com:snickers2",
                "fatimastepps@yahoo.com:missme2",
                "smartgirl_ph@yahoo.com:apollo13",
                "cross2426@yahoo.com:xenna24",
                "x0brit0x22@yahoo.com:t00thbrush",
                "upchuck_21@yahoo.com:andyb123",
                "mcdomeng16@yahoo.com:mcdomeng16",
                "chris_englin@yahoo.com:odelay",
                "awwabl@yahoo.com:lbawwa",
                "luna.ana88@yahoo.com:202122",
                "kellog624@yahoo.com:happiness",
                "baileykim03@yahoo.com:elizabeth",
                "dougiefisher13@yahoo.com:yellowfin",
                "rts_franchise@yahoo.com:franchise",
                "nmnjordan@yahoo.com:love5083",
                "fabiorich@yahoo.com:ikthus",
                "boobi20@yahoo.com:genesis",
                "caitlinmk0108@yahoo.com:cmkb1898",
                "gracielalopez434@yahoo.com:sergrana2",
                "hboykin9515@yahoo.com:bonkers12",
                "didits_gonzales@yahoo.com:whitey",
                "zuraysf@yahoo.com.sg:inaida",
                "angelaquino@yahoo.com:angel",
                "eichman84@yahoo.com:chris7",
                "erika0506ramirez@yahoo.com:erika0506",
                "ajf4l2006@yahoo.com:km99cq",
                "nishaishere06@yahoo.com:lilsexy06",
                "josh.mccracken@yahoo.com:shanna05",
                "qrxv@yahoo.com:291279",
                "jonas_lvr247@yahoo.com:nickjonas1",
                "fireheart421@yahoo.com:superbowl39",
                "markteshenbaugh@yahoo.com:kikirara5",
                "chuckle_boo@yahoo.com:marshal4",
                "jmelowjones@yahoo.com:melow123",
                "herien07@yahoo.com:rinsie07",
                "cournykaunbaun@yahoo.com:bubbles11",
                "dennykutil@yahoo.com:lupalagi",
                "danspen13@yahoo.com:l4pt0p1",
                "jesschaser@yahoo.com:redken",
                "jsfilth13@yahoo.com:monster13",
                "chromatocrat@yahoo.com:sup512pr",
                "stephn_27@yahoo.com:korzkie",
                "trobinson1234@yahoo.com:dickhead1",
                "markhiner@yahoo.com:bigh72",
                "krova666@yahoo.com:2prhc7j",
                "eodell89@yahoo.com:pink11",
                "bigboreracing@yahoo.com:andy3300",
                "parmerholiday@yahoo.com:mrbean07",
                "izan_ainizan@yahoo.com:nike1959",
                "lenlen_gaisano@yahoo.com:len7888",
                "kymcurtis@yahoo.com:December07",
                "ray_5p1k3@yahoo.com:newraymond",
                "cfpolito@yahoo.com.br:110377",
                "ali_olcer@yahoo.com:zanaka",
                "nvoda@yahoo.com:fanta45",
                "r.provencial@yahoo.com:badco1956",
                "xkiniaczekxpl@yahoo.com:pamagda",
                "jess06_lyons@yahoo.com:jerkface",
                "dghiggy@yahoo.com:dghiggy",
                "theyankees1923@yahoo.com:mooch3",
                "deception1441@yahoo.com:dragon110",
                "cindy_shuyu@yahoo.com:aaron4life",
                "method320@yahoo.com:6244907",
                "tonytapney@yahoo.com:shebacali1",
                "my_din27@yahoo.com:774400",
                "ian_apolonio@yahoo.com.ph:tarantula",
                "kerwincruz@yahoo.com:111837",
                "beachstop@yahoo.com:sissie42",
                "kikenzi06@yahoo.com:kiarrah",
                "slickmiller28@yahoo.com:droopy",
                "struppjon@yahoo.com:packers",
                "bellaly11@yahoo.com:roxie123",
                "kimwunder@yahoo.com:jesusis",
                "marquishawkins1989@yahoo.com:lamer228",
                "gomezkev@yahoo.com:dangerous",
                "anese26@yahoo.com:grambling",
                "saenzazul@yahoo.com:130777",
                "ryda2008@yahoo.com:ilive408",
                "lauralyn06@yahoo.com.au:magic803",
                "delia_marie1@yahoo.com:delbel1",
                "kayode94@yahoo.com:Bolaji12",
                "aunler@yahoo.com:205205",
                "clevesown1@yahoo.com:washer28",
                "kd0770@yahoo.com:kyle2824",
                "cwadams03@yahoo.com:cwadams03",
                "kjoyce612@yahoo.com:joy612",
                "stateparkmomma@yahoo.com:061454",
                "jimmie81@yahoo.com:cammie07",
                "kwilliamsyes@yahoo.com:popo2580",
                "cartoony96@yahoo.com:skittles2",
                "codyodie23@yahoo.com:chicago",
                "doomdoomdoomdoomgir@yahoo.com:shitcunt28",
                "spdie7@yahoo.com:spdie7",
                "minghosie@yahoo.com:791207",
                "kianat417@yahoo.com:041795",
                "kurtdog_us@yahoo.com:einstein",
                "vash1407@yahoo.com:trigun",
                "Negm.Nemo@yahoo.com:ttttttttt",
                "tetesell@yahoo.com.br:ljo265",
                "jasminesgivens91@yahoo.com:diggy21",
                "tholt0414@yahoo.com:sophie0414",
                "lizodus@yahoo.com:jaybaby",
                "casaggi@yahoo.com.br:mar211",
                "macaulaynaomi@yahoo.com:1151997",
                "jho_angelz@yahoo.com:supergirl",
                "marius.girulis@yahoo.com:liutas08",
                "ft460@yahoo.com:mustang",
                "alishaezell@yahoo.com:mikayla123",
                "kbboys05@yahoo.com:hunting05",
                "smitty3435@yahoo.com:bandit",
                "sandi_kakugawa@yahoo.com:kaku5258",
                "ethan_ballinger08@yahoo.com:30pass",
                "nuche3135@yahoo.com:zen3135",
                "jeffersondeguzman28@yahoo.com:jeff28",
                "greg_0668@yahoo.com:ally0906",
                "fivetoasters@yahoo.com:bdt1bdt2",
                "babyjeansenya2006@yahoo.com:yasmin03",
                "seickost24@yahoo.com:russel24",
                "gloryminded@yahoo.com:kelly777",
                "jssmc@yahoo.com:1973nova",
                "wellschelsea32@yahoo.com:bowwow1",
                "kkpatel111@yahoo.com:ritu41280",
                "paymanfaraji@yahoo.com:poster",
                "spoester@yahoo.com.br:231736",
                "chrisesimpson@yahoo.com:200503",
                "lyonsmane2000@yahoo.com:amosandandy",
                "f18garcia@yahoo.com:teddy618",
                "e.nesimi00@yahoo.com:ed1976",
                "half_demonPG13@yahoo.com:iloveyou",
                "Design2182@yahoo.com:yellow123",
                "shepherd14344@yahoo.com:14344678",
                "hollywod28@yahoo.com:lakes73",
                "nemo_093@yahoo.com:1243397",
                "udshalk@yahoo.com.br:097680",
                "dewayne_richardson_michael@yahoo.com:dewayne12",
                "adrih_qt@yahoo.com:sandy2006",
                "doctor_hammood@yahoo.com:egyptian",
                "mcartwright28@yahoo.com:love11",
                "luis_tabornal2005@yahoo.com:12457800",
                "topakin@yahoo.com:topakin",
                "ezzy89_gemini@yahoo.com:yellow",
                "rcd1708@yahoo.com:hockey01",
                "elcocouy@yahoo.com:MImila08",
                "lissette44@yahoo.com:monster4",
                "shelliethomas77@yahoo.com:shel1205",
                "danamariex2@yahoo.com:august",
                "laurenchojnacki@Yahoo.com:fuckers1",
                "lrolivier@yahoo.com:tequila",
                "nomad194@yahoo.com:Nomad200",
                "kndr_tucker@yahoo.com:shatara",
                "jbiggs_apc@yahoo.com:x5687798",
                "bigsmooth_74@yahoo.com:justdoit1",
                "drdrkwan@yahoo.com.hk:gdale386",
                "tsmith2589@yahoo.com:saints08",
                "lowbrassguy1@yahoo.com:tyler12",
                "nicolespencer35@yahoo.com:janalee1",
                "aprilsimone36@yahoo.com:baruch",
                "milner142790@yahoo.com:mitchell16",
                "tgavin107@yahoo.com:dkitten22",
                "brambg@yahoo.com:bombers",
                "sgsmbo@yahoo.com:12345678",
                "tagle_k@yahoo.com:august",
                "zacktheman9@yahoo.com:wrestle1",
                "rico5_2000@yahoo.com:sosexy26",
                "jillian.perini@yahoo.com:jillpill2",
                "Teshawnfoster@yahoo.com:rico66",
                "mcewenc16@yahoo.com:cm1990",
                "mstern82@yahoo.com:1995f350",
                "lentellj@yahoo.com:1xracing",
                "gorda.1104@yahoo.com:12140401",
                "govs77@yahoo.com:vin3677",
                "cyrel1186@yahoo.com:nov1786",
                "amycleveland12@yahoo.com:01302005",
                "jentaylor_77@yahoo.com:jtaylor81",
                "allmorris@yahoo.com:jasmine7",
                "lopeztriston@yahoo.com:t441205l",
                "wsucribguy@yahoo.com:crib7944",
                "crazy_chick_4lyfe@yahoo.com:nookie1",
                "caseylw10@yahoo.com:chucky10",
                "corgi_la@yahoo.com:Donkey1",
                "mohsen_rms@yahoo.com:mufc2000",
                "tayhard@yahoo.com:villard55",
                "wewdohgy1@yahoo.com:2356777",
                "rawbury@yahoo.com:ray308128",
                "ram_ramskiez@yahoo.com:junereimar",
                "peterfsho@yahoo.com:powerr",
                "datommy@yahoo.com:freddief",
                "crisjcoen@yahoo.com:crissy",
                "jonte1293@yahoo.com:december",
                "rafraanje@yahoo.com:roalfr",
                "Giz2022@yahoo.com:202202",
                "kairos41705@yahoo.com:marmar",
                "luisdus@yahoo.com.mx:procatt",
                "shavonbouey@yahoo.com:jiselle08",
                "saurav_kakar@yahoo.com:mackintosh",
                "wkcw888@yahoo.com.hk:A821328B",
                "nightryder304@yahoo.com:e6970488",
                "supermarc_31@yahoo.com:thirtyone",
                "ookla13@yahoo.com:aug142004",
                "mogilnickikevin@yahoo.com:deadman1",
                "steph.r3711@yahoo.com:b16101",
                "Msvirgo969@yahoo.com:4ubabe",
                "prathejm@yahoo.com:socrates",
                "jlgomez90@yahoo.com:Sebastian1",
                "sarah.north@yahoo.com.au:Cooper88",
                "cheska@yahoo.com:cheska",
                "aubreagalloway@yahoo.com:october17",
                "billy_spell@yahoo.com:jump4joy",
                "lilian_b_samson@yahoo.com:charmell",
                "kai4w@yahoo.com:1816kc",
            ]
                await client.send_message(message.author, (random.choice(variable)))
            else:
                await client.wait_for_message(timeout=10)
                await client.delete_message(message)
                await client.send_message(message.author, "use the #❗»-generator channel")
        else:
            await client.send_message(message.channel, "Subscribe `yCode` and send Moderator or a Admin a Screen!")

    if message.content == "-help":
        emb = (discord.Embed(description="**COMMANDS**", color=0x3DF270))
        emb.add_field(name="!minecraft", value="for Subscriber", inline=False)
        emb.add_field(name="!spotify", value="for Subscriber", inline=False)
        emb.add_field(name="!fortnite", value="for Simple", inline=False)
        emb.add_field(name="!uplay", value="for Simple", inline=False)
        emb.add_field(name="!bot", value="see the coder of the bot", inline=False)
        emb.add_field(name="!youtube", value="get the channel link", inline=False)
        emb.add_field(name="!shop", value="get the shop link", inline=False)
        emb.add_field(name="!rules", value="get the list of rules", inline=False)
        emb.add_field(name="!simple", value="type **donate** in the chat to buy it!", inline=False)
        emb.add_field(name="!refill minecraft fortnite spotify smc sspotify uplay nordvpn hulu", value="get the channel link", inline=False)
        emb.add_field(name="donate", value="to buy the Simple rank", inline=False)
        await client.send_message(message.author, embed=emb)

    if message.content == "!rules":
        emb = (discord.Embed(description="**Rules**", color=0x3DF270))
        emb.add_field(name="1. | Swearing is strictly prohibited.", value="kick or mute", inline=False)
        emb.add_field(name="2. | Don't advertise anything (Discord servers, Roblox groups, etc). DM Advertising is not allowed.", value="24h ban", inline=False)
        emb.add_field(name="3. | Do not attempt to test or bypass the filter.", value="kick or mute", inline=False)
        emb.add_field(name="4. | Disruptive behavior and controversial topics are not allowed (religion/politics). In addition: the obvious intent to provoke another member or start arguments is prohibited.", value="kick or mute", inline=False)
        emb.add_field(name="5. | Staff impersonation is not allowed, if you change your name/profile picture, it will result in an automatic mute until things are fixed.", value="kick or mute", inline=False)
        emb.add_field(name="6. | Harassing a user, lewd jokes, etc are not tolerated. If someone is harassing someone in your DMs please send proof to a moderator.", value="kick or mute", inline=False)
        emb.add_field(name="7. | Do not ignore or argue with staff or moderators. ", value="kick or mute", inline=False)
        emb.add_field(name="8. | Don't DDoS or DOS threaten anyone.", value="perma ban", inline=False)
        emb.add_field(name="9. | Inappropriate Discord PFPs or usernames will not be tolerated. ", value="mute or kick", inline=False)
        emb.add_field(name="10. | Do not ping Owners Please. If you see that we're busy and/if you need us just DM an Supervisor, they will help you.", value="mute", inline=False)
        emb.add_field(name="11. | All staff members are to follow the same rules that all members follow, if any are seen misbehaving, it will result in an automatic demoting.", value="demoting", inline=False)
        await client.send_message(message.channel, embed=emb)

    if message.content == "-verify":
        emb = (discord.Embed(description="**Rules**", color=0x3DF270))
        emb.add_field(name="1. | Swearing is strictly prohibited.", value="kick or mute", inline=False)
        emb.add_field(name="2. | Don't advertise anything (Discord servers, Roblox groups, etc). DM Advertising is not allowed.", value="24h ban", inline=False)
        emb.add_field(name="3. | Do not attempt to test or bypass the filter.", value="kick or mute", inline=False)
        emb.add_field(name="4. | Disruptive behavior and controversial topics are not allowed (religion/politics). In addition: the obvious intent to provoke another member or start arguments is prohibited.", value="kick or mute", inline=False)
        emb.add_field(name="5. | Staff impersonation is not allowed, if you change your name/profile picture, it will result in an automatic mute until things are fixed.", value="kick or mute", inline=False)
        emb.add_field(name="6. | Harassing a user, lewd jokes, etc are not tolerated. If someone is harassing someone in your DMs please send proof to a moderator.", value="kick or mute", inline=False)
        emb.add_field(name="7. | Do not ignore or argue with staff or moderators. ", value="kick or mute", inline=False)
        emb.add_field(name="8. | Don't DDoS or DOS threaten anyone.", value="perma ban", inline=False)
        emb.add_field(name="9. | Inappropriate Discord PFPs or usernames will not be tolerated. ", value="mute or kick", inline=False)
        emb.add_field(name="10. | Do not ping Owners Please. If you see that we're busy and/if you need us just DM an Supervisor, they will help you.", value="mute", inline=False)
        emb.add_field(name="11. | All staff members are to follow the same rules that all members follow, if any are seen misbehaving, it will result in an automatic demoting.", value="demoting", inline=False)
        await client.send_message(message.channel, embed=emb)

    if "-warn" in message.content.lower():
        if "544184897674412067" in [role.id for role in message.author.roles]:
            emb = (discord.Embed(description="**Warning**", color=0x3DF270))
            emb.add_field(name="You have been warned", value="If you do this again you get a kick / ban", inline=False)
            emb.add_field(name="Read our discord rules", value="rules are hier ❗»-rules", inline=True)
            await client.send_message(message.channel, embed=emb)
        else:
            await client.send_message(message.channel, "You do not have enough permissions!")

    if "-warn" in message.content.lower():
        variable = message.content[len("-warn"):].strip()
        await client.send_message(client.get_channel("556847944750333952"), variable)

    if "-report" in message.content.lower():
        if "544184613795528705" in [role.id for role in message.author.roles]:
            emb = (discord.Embed(description="**report**", color=0x3DF270))
            emb.add_field(name="Your report was created", value="a team member will check it", inline=False)
            await client.send_message(message.channel, embed=emb)
        else:
            await client.send_message(message.channel, "You do not have enough permissions!")

    if message.content == "-report":
        variable = message.content[len("-report"):].strip()
        await client.send_message(client.get_channel("563742938685898803"), variable)

    if "-info" in message.content.lower():
        variable = message.content[len("-info"):].strip()
        await client.send_message(client.get_channel("544180648819032095"), variable)

    if "-info" in message.content.lower():
        if "544184897674412067" in [role.id for role in message.author.roles]:
            emb = (discord.Embed(description="**info**", color=0x3DF270))
            emb.add_field(name="Discord info was senden an a team member", value="Thank you", inline=False)
            await client.send_message(message.channel, embed=emb)
        else:
            await client.send_message(message.channel, "You do not have enough permissions!")

    if "https://discord.gg/" in message.content.lower():
        if "544184839318929409" in [role.id for role in message.author.roles]:
            await client.wait_for_message(timeout=1)
        else:
            await client.delete_message(message)
            emb = (discord.Embed(description="**Warning**", color=0x3DF270))
            emb.add_field(name="You have been warned", value="If you do this again you get a Mute", inline=False)
            await client.send_message(message.channel, embed=emb)

    if "@everyone" in message.content.lower():
        if "544184897674412067" in [role.id for role in message.author.roles]:
            await client.wait_for_message(timeout=1)
        else:
            await client.delete_message(message)
            emb = (discord.Embed(description="**Warning**", color=0x3DF270))
            emb.add_field(name="You have been warned", value="If you do this again you get a Mute", inline=False)
            await client.send_message(message.channel, embed=emb)

    if "-refill minecraft" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="Minecraft", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-refill smc" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="smc", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-refill fortnite" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="Fortnite", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-shop" in message.content.lower():
        emb = (discord.Embed(description="**Shop**", color=0x3DF270))
        emb.add_field(name="Accounts and more", value="https://shoppy.gg/@SimpleCrack", inline=False)
        await client.send_message(message.channel, embed=emb)

    if "-ycode" in message.content.lower():
        emb = (discord.Embed(description="**Shop yCode**", color=0x3DF270))
        emb.add_field(name="Accounts and more", value="https://shoppy.gg/@SimpleCrack", inline=False)
        await client.send_message(message.channel, embed=emb)

    if "-refill hulu" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="Hulu", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-refill spotify" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="Spotify", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-refill sspotify" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="sspotify", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if "-refill uplay" in message.content.lower():
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="Uplay", value="need refill", inline=False)
        await client.send_message(client.get_channel("557199613954621501"), embed=emb)

    if message.content == "-refill":
        emb = (discord.Embed(description="**REFILL**", color=0x3DF270))
        emb.add_field(name="False! Put an account behind it", value="-refill account", inline=False)
        await client.send_message(message.channel, embed=emb)

    if message.content == "!gen":
        await client.send_message(message.channel, "Prefix=! `spotify` `minecraft` `fortnite` `smc` `uplay` `hulu` `nordvpn` `sspotify`")

    if message.content == "!bot":
        await client.send_message(message.channel, "Bot by **@yCode.#5813**")

    if message.content == "verify":
        await client.send_message(message.channel, "[False] -> Type -verify and agree our rules")

    if message.content == "!verify":
        await client.send_message(message.channel, "[False] -> Type -verify and agree our rules")

    if message.content == "!yt":
        await client.send_message(message.author, "https://www.youtube.com/channel/UCJ72npfPcr_nyCMaevbU7cQ?view_as=subscriber")

    if message.content == "!subscriber":
        await client.send_message(message.author, "https://www.youtube.com/channel/UCJ72npfPcr_nyCMaevbU7cQ?view_as=subscriber")

    if message.content == "!instagram":
        await client.send_message(message.channel, "https://www.instagram.com/tradeandsellmarket")

    if message.content.lower().startswith("-verify"):
        if "547423541902049294" in [role.id for role in message.author.roles]:
            botmsg = await client.send_message(message.channel, "Agree or disagree")
        else:
            botmsg = await client.send_message(message.channel, "`You are Verifyed!`")

        await client.add_reaction(botmsg, "✔")
        await client.add_reaction(botmsg, "❌")

        global testmsgid
        testmsgid = botmsg.id

        global testmsguser
        testmsguser = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    chat = reaction.message.channel

    if reaction.emoji == "✔" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "Member", msg.server.roles)
        await client.add_roles(user, role)

    if reaction.emoji == "✔" and msg.id == testmsgid and user == testmsguser:
        await client.wait_for_message(timeout=3)
        role = discord.utils.find(lambda r: r.name == "NonVerified", msg.server.roles)
        await client.remove_roles(user, role)
        await client.send_message(chat, "✅ `FINISH`")

    if reaction.emoji == "❌" and msg.id == testmsgid and user == testmsguser:
        await client.send_message(chat, "❎")

@client.event
async def on_member_join(member):
        role = discord.utils.get(member.server.roles, name="NonVerified")
        await client.add_roles(member, role)

client.run("NTQ2MDc0OTEyMTAwNzEyNDQ4.XK8wGw.fS13t3uJeSwD055nvu3QJpSiies")
