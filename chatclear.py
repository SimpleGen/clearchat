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
                    "jeddfaughn@yahoo.com:jeff12199 | Subscription: Premium For Family | Renew: Unlimited | Country: US",
                    "fromgomel90@gmail.com:pa5510nAllMine | Subscription: Premium For Family | Renew: Unlimited | Country: US",
                    "simpson.wg@gmail.com:summer16 | Subscription: Premium For Family | Renew: Unlimited | Country: US",
                    "csugden92@gmail.com:CS448988 | Subscription: Premium For Family | Renew: Unlimited | Country: GB",
                    "benjamin.hiller@gmail.com:hotpack | Subscription: Family Owner | Renew: 4/16/19 | Country: DE",
                    "alinmar@globo.com:barbeito | Subscription: Premium For Family | Renew: Unlimited | Country: BR",
                    "racasale@bol.com.br:twxkihk1 | Subscription: Premium For Family | Renew: Unlimited | Country: BR",
                    "corrado.capriotti@alice.it:dariomatteo | Subscription: Premium For Family | Renew: Unlimited | Country: IT",
                    "boudin.luc@club-internet.fr:cblb2111 | Subscription: Premium For Family | Renew: Unlimited | Country: FR",
                    "t_willy86@yahoo.com:bothell86 | Subscription: Family Owner | Renew: 4/22/19 | Country: US",
                    "rhublein@imagen8sion.com:Epdowd50 | Subscription: Family Owner | Renew: 5/8/19 | Country: US",
                    "col.taylor4@gmail.com:Gompers22 | Subscription: Family Owner | Renew: 4/24/19 | Country: US",
                    "eric.faes@hotmail.com:Brecht01 | Subscription: Family Owner | Renew: 5/5/19 | Country: BE",
                    "ericacabutihan@yahoo.com:Up9545204 | Subscription: Family Owner | Renew: 5/6/19 | Country: SG",
                    "jennavuorela@hotmail.com:Legolina88 | Subscription: Family Owner | Renew: 4/16/19 | Country: FI",
                    "ckgenero@gmail.com:Sere4you | Subscription: Family Owner | Renew: 4/15/19 | Country: US",
                    "julie_227@hotmail.com:Jesus2207 | Subscription: Family Owner | Renew: 4/16/19 | Country: SG",
                    "nathaliedufoulon@hotmail.com:Password01 | Subscription: Family Owner | Renew: 4/13/19 | Country: AU",
                    "Jeffreyrclark@gmail.com:vanessa1 | Subscription: Family Owner | Renew: 4/10/19 | Country: US",
                    "kcmartyhonig@gmail.com:L8cydogs | Subscription: Family Owner | Renew: 4/14/19 | Country: US",
                    "burkhartnoah@yahoo.com:Garfunkle95 | Subscription: Family Owner | Renew: 4/14/19 | Country: US",
                    "janew111@hotmail.com:ETHAN111 | Subscription: Family Owner | Renew: 4/17/19 | Country: AU",
                    "mtgrady12@gmail.com:Alnwick69 | Subscription: Family Owner | Renew: 4/13/19 | Country: GB",
                    "Shaundacre@hotmail.com:Ethanda1 | Subscription: Family Owner | Renew: 4/16/19 | Country: GB",
                    "jonathanhammann7@gmail.com:JonHam77 | Subscription: Family Owner | Renew: 4/17/19 | Country: US",
                    "Hale75@hotmail.com:fishwater | Subscription: Family Owner | Renew: 4/18/19 | Country: US",
                    "jeanette.jpkc@yahoo.com:18790Wilson | Subscription: Family Owner | Renew: 4/17/19 | Country: US",
                    "crpnjean@aol.com:Britta1972 | Subscription: Family Owner | Renew: 4/21/19 | Country: US",
                    "PatriokRyan@outlook.com:Ohioboy88 | Subscription: Family Owner | Renew: 4/19/19 | Country: US",
                    "Jodiebass@aol.com:Kaluha17 | Subscription: Family Owner | Renew: 4/30/19 | Country: US",
                    "sirventpozo@hotmail.com:1961Toni | Subscription: Family Owner | Renew: 4/12/19 | Country: ES",
                    "MBWGIS@gmail.com:tycoon55 | Subscription: Family Owner | Renew: 4/25/19 | Country: CA",
                    "QueenRegina69@hotmail.com:murphy | Subscription: Family Owner | Renew: 4/20/19 | Country: US",
                    "andrew.c.brewster@gmail.com:GtowN011 | Subscription: Premium For Students | Renew: 5/8/19 | Country: US",
                    "djack07@gmail.com:wilD82Cats | Subscription: Family Owner | Renew: 5/5/19 | Country: US",
                    "darren.talcott@yahoo.com:Enigma359 | Subscription: Family Owner | Renew: 4/26/19 | Country: US",
                    "bentemolgaard@gmail.com:Erling55 | Subscription: Family Owner | Renew: 4/13/19 | Country: DK",
                    "neronysocrates@gmail.com:Ramiro78 | Subscription: Family Owner | Renew: 4/10/19 | Country: AR",
                    "jimcg72@gmail.com:Bomber72 | Subscription: Family Owner | Renew: 5/9/19 | Country: AU",
                    "kjpjmann1@gmail.com:Chicko11 | Subscription: Family Owner | Renew: 4/17/19 | Country: AU",
                    "thejerermyhucks@yahoo.com:Jesus001 | Subscription: Family Owner | Renew: 4/23/19 | Country: US",
                    "lolly1016@hotmail.com:Icloud1016 | Subscription: Family Owner | Renew: 4/24/19 | Country: GB",
                    "voigt.blaubeuren@t-online.de:yannick2001 | Subscription: Premium For Family | Renew: Unlimited | Country: DE",
                    "heine.n@t-online.de:sabine31 | Subscription: Premium For Family | Renew: Unlimited | Country: DE",
                    "fabian.babin@gmx.de:19Fabs88 | Subscription: Premium For Family | Renew: Unlimited | Country: DE",
                    "veri.simon@gmx.de:oscar5607 | Subscription: Premium For Family | Renew: Unlimited | Country: DE",
                    "janetca@gmx.de:Rostock1977 | Subscription: Premium For Family | Renew: Unlimited | Country: DE",
                    "",
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

client.run("NTY1NTY4Njk2NDAwMjE2MDg0.XK4VNA.ONgB-oZWw0qBM1E80AbunOV4gPE")
